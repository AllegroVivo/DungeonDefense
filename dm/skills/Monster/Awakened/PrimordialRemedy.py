from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("PrimordialRemedy",)

################################################################################
class PrimordialRemedy(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-323",
            name="Primordial Remedy",
            description=(
                "Applies 10 Focus and 5 Nature's Power to all monsters in "
                "the dungeon."
            ),
            rank=10,
            cooldown=CooldownType.DungeonWide
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        for monster in self.game.all_monsters:
            monster.add_status("Focus", 10, self)
            monster.add_status("Nature's Power", 5, self)

################################################################################
