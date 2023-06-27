from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("CurseAura",)

################################################################################
class CurseAura(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-149",
            name="Curse Aura",
            description=(
                "Apply 1 Curse to enemies that have attacked you or received "
                "damage from you."
            ),
            rank=4,
            cooldown=CooldownType.Passive
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        ctx.register_post_execute(self.post_execute)

################################################################################
    def post_execute(self, ctx: AttackContext) -> None:

        # If damage was dealt
        if ctx.damage > 0:
            # Apply Curse to the enemy.
            target = ctx.target if self.owner == ctx.source else ctx.source
            target.add_status("Curse", 1, self)

################################################################################
