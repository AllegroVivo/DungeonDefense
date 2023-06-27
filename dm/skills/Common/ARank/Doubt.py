from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Doubt",)

################################################################################
class Doubt(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-150",
            name="Doubt",
            description=(
                "Inflict 16 (+1.5*ATK) damage and apply 3 Obey to all enemies "
                "in the room."
            ),
            rank=4,
            cooldown=CooldownType.RoomWide,
            effect=SkillEffect(base=16, scalar=1.5)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # For each enemy in the room
        for target in ctx.room.units_of_type(self.owner, inverse=True):
            # Deal damage.
            target.damage(self.effect)
            # Apply Obey.
            target.add_status("Obey", 3, self)

################################################################################
