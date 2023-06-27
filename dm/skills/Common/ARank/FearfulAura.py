from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("FearfulAura",)

################################################################################
class FearfulAura(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-155",
            name="Fearful Aura",
            description=(
                "Apply 1 Panic to enemies that have attacked you or received "
                "damage from you."
            ),
            rank=4,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        if self.owner in (ctx.source, ctx.target):
            ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        # If damage was applied
        if ctx.damage > 0:
            # Apply Panic to the enemy.
            target = ctx.target if self.owner == ctx.source else ctx.source
            target.add_status("Panic", 1, self)

################################################################################
