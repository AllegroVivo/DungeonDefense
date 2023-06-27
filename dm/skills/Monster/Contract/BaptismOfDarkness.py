from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("BaptismOfDarkness",)

################################################################################
class BaptismOfDarkness(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-293",
            name="Baptism of Darkness",
            description=(
                "Apply 4 Immortality and Immortal Rage to all allies in "
                "the dungeon."
            ),
            rank=8,
            cooldown=CooldownType.DungeonWide
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        for monster in self.game.all_monsters:
            for status in ("Immortality", "Immortal Rage"):
                monster.add_status(status, 4, self)

################################################################################
