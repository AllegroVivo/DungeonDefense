from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("EyeOfMind",)

################################################################################
class EyeOfMind(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-154",
            name="Eye of Mind",
            description=(
                "Gain 15 Focus and 15 Defense at the beginning of the battle."
            ),
            rank=4,
            cooldown=CooldownType.Passive
        )

        # (Hidden effect: Attacks can't miss)

################################################################################
    def on_acquire(self) -> None:

        self.listen("hero_spawn")

################################################################################
    def notify(self, unit: DMUnit) -> None:

        if self.owner == unit:
            for status in ("Focus", "Defense"):
                self.owner.add_status(status, 15, self)

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # This execution logic, including the callback below, pertains to the
        # hidden effect of this skill, which is that attacks can't miss.
        if self.owner == ctx.source:
            ctx.register_post_execute(self.post_execute)

################################################################################
    @staticmethod
    def post_execute(ctx: AttackContext) -> None:

        # If the attack will not succeed
        if ctx.will_fail:
            # We can just bypass creation of another attack context and
            # apply the damage directly.
            ctx.target.direct_damage(ctx._damage.calculate())

################################################################################
