from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

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
            rank=2,
            cooldown=0,
            passive=True
        )

        # (Hidden effect: Attacks can't miss)

################################################################################
    def on_acquire(self) -> None:

        self.listen("battle_start")

################################################################################
    def notify(self) -> None:

        self.owner.add_status("Focus", 15, self)
        self.owner.add_status("Defense", 15, self)

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # This execution logic, including the callback below, pertains to the
        # hidden effect of this skill, which is that attacks can't miss.
        if self.owner == ctx.source:
            ctx.register_post_execute(self.callback)

################################################################################
    @staticmethod
    def callback(ctx: AttackContext) -> None:

        # If we've failed the attack, meaning it will miss, then we can just
        # use some of the internal methods to apply the original damage directly.
        if ctx.will_fail:
            # `target._damage()` is the method to bypass creating an AttackCTX
            # and `ctx._damage` is the private damage component attached to
            # the AttackCTX, which we're modifying directly to avoid the `will_fail`
            # condition.
            ctx.target._damage(ctx._damage.calculate())

################################################################################
