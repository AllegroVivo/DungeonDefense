from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType, StatusType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("CleansingWave",)

################################################################################
class CleansingWave(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-213",
            name="Cleansing Wave",
            description=(
                "Remove all of allies' unfavorable states."
            ),
            rank=3,
            cooldown=CooldownType.RoomWide
        )

        # This doesn't specify which allies, so I'm going to assume it's all
        # allies on the same tile.

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        for unit in ctx.room.units_of_type(self.owner):
            for status in unit.statuses:
                if status._type in (StatusType.Debuff, StatusType.AntiBuff):
                    status.deplete_all_stacks()

        # Depleting the stacks should be sufficient since empty statuses will
        # get culled at the conclusion of the attack loop.

################################################################################
