from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext, StatusExecutionContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ElectricShield",)

################################################################################
class ElectricShield(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-393",
            name="Electric Shield",
            description=(
                "Does not receive damage from Shock. Deals damage equal to "
                "25 % of Shock given to self to all adjacent enemies when "
                "receiving damage."
            ),
            rank=9,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_execute")

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're being attacked, wait for damage.
        if self.owner == ctx.target:
            ctx.register_post_execute(self.callback)

################################################################################
    @staticmethod
    def callback(ctx: AttackContext) -> None:

        # If damage was received
        if ctx.damage > 0:
            # Check for Shock and deal additional damage if present.
            shock = ctx.target.get_status("Shock")
            if shock:
                ctx.amplify_flat(int(shock.stacks * 0.25))

################################################################################
    def notify(self, ctx: StatusExecutionContext) -> None:

        # Nullify Shock if we're the target.
        if self.owner == ctx.target:
            if ctx.status.name == "Shock":
                ctx.will_fail = True

################################################################################
