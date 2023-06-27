from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("DivineBlessing",)

################################################################################
class DivineBlessing(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-378",
            name="Divine Blessing",
            description=(
                "Apply 3 Shield and Immune to all heroes in the dungeon. Apply "
                "20 Corruption to all monsters upon death."
            ),
            rank=7,
            cooldown=CooldownType.DungeonWide
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # Apply 3 Shield and Immune to all heroes in the dungeon.
        for hero in self.game.all_heroes:
            for status in ("Shield", "Immune"):
                hero.add_status(status, 3, self)

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_death")

################################################################################
    def notify(self, unit: DMUnit) -> None:

        # When we die, apply 20 Corruption to all monsters.
        if self.owner == unit:
            for unit in self.game.all_monsters:
                unit.add_status("Corruption", 20, self)

################################################################################
