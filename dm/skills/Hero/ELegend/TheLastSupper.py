from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("TheLastSupper",)

################################################################################
class TheLastSupper(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-374",
            name="The Last Supper",
            description=(
                "All heroes in the dungeon recover LIFE as much as 20 % of "
                "their LIFE lost, and gain 1 Absorption. Gain 5 Absorption "
                "upon entering the dungeon."
            ),
            rank=7,
            cooldown=CooldownType.DungeonWide
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # All heroes in the dungeon recover LIFE as much as 20 % of their LIFE
        # lost, and gain 1 Absorption.
        for hero in self.game.all_heroes:
            hero.heal(hero.max_life * 0.20)
            hero.add_status("Absorption", 1, self)

################################################################################
    def on_acquire(self) -> None:

        self.listen("hero_spawn")

################################################################################
    def notify(self, unit: DMUnit) -> None:

        # When we spawn, gain 5 Absorption.
        if self.owner == unit:
            unit.add_status("Absorption", 5, self)

################################################################################
