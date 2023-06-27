from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("BloodHunting",)

################################################################################
class BloodHunting(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-236",
            name="Blood Hunting",
            description=(
                "All allies in adjacent rooms gain 1 Acceleration, 1 Focus."
            ),
            rank=4,
            cooldown=CooldownType.AdjacentWide
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        units = self.room.units_of_type(self.owner)
        for room in self.room.adjacent_rooms:
            for unit in room.units_of_type(self.owner):
                if unit not in units:
                    units.append(unit)

        for unit in units:
            unit.add_status("Acceleration", 1, self)
            unit.add_status("Focus", 1, self)

################################################################################
