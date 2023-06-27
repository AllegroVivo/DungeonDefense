from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("PetrifyingCurse",)

################################################################################
class PetrifyingCurse(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-261",
            name="Petrifying Curse",
            description=(
                "Apply 1 Stun, 3 Vulnerable to all enemies in the room."
            ),
            rank=5,
            cooldown=CooldownType.RoomWide
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        for unit in self.room.units_of_type(self.owner, inverse=True):
            unit.add_status("Stun", 1, self)
            unit.add_status("Vulnerable", 3, self)

################################################################################
