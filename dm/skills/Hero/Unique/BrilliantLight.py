from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("BrilliantLight",)

################################################################################
class BrilliantLight(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-346",
            name="Brilliant Light",
            description=(
                "Apply 3 Blind to all enemies in the room."
            ),
            rank=3,
            cooldown=CooldownType.RoomWide
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # For each enemy in the room
        for unit in self.room.units_of_type(self.owner, inverse=True):
            # Apply Blind.
            unit.add_status("Blind", 3, self)

################################################################################
