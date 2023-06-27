from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("UltimateDance",)

################################################################################
class UltimateDance(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-363",
            name="Ultimate Dance",
            description=(
                "Gain 1 Dodge for every damage received."
            ),
            rank=5,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're being attacked, wait for damage.
        if self.owner == ctx.target:
            ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        # If damage was received
        if not ctx.will_fail:
            # Apply Dodge equal to that damage.
            self.owner.add_status("Dodge", ctx.damage, self)

################################################################################
