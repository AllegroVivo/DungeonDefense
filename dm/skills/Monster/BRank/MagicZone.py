from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("MagicZone",)

################################################################################
class MagicZone(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-221",
            name="Magic Zone",
            description=(
                "Apply 2 Shield, 2 Immune to all allies in the room."
            ),
            rank=3,
            cooldown=CooldownType.RoomWide
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        targets = self.room.units_of_type(self.owner)
        for target in targets:
            target.add_status("Shield", 2, self)
            target.add_status("Immune", 2, self)

################################################################################
