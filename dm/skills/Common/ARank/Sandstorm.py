from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Sandstorm",)

################################################################################
class Sandstorm(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-168",
            name="Sandstorm",
            description=(
                "Inflict 16 (+1.5*ATK) damage and apply 2 Blind to all enemies "
                "in the room."
            ),
            rank=4,
            cooldown=CooldownType.RoomWide,
            effect=SkillEffect(base=16, scalar=1.5)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # For each enemy in the room
        for unit in ctx.room.units_of_type(self.owner, inverse=True):
            # Damage them.
            unit.damage(self.effect)
            # Apply Blind.
            unit.add_status("Blind", 2, self)

################################################################################
