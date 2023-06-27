from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Avalanche",)

################################################################################
class Avalanche(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-272",
            name="Avalanche",
            description=(
                "Inflict 54 (+0.8*ATK) damage and apply 3 Slow to all enemies "
                "in the dungeon. Apply extra 1 Stun to enemies in Slow state."
            ),
            rank=6,
            cooldown=CooldownType.DungeonWide
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        for hero in self.game.all_heroes:
            hero.damage(self.effect)
            slow = hero.get_status("Slow")
            stacks = 4 if slow is not None else 3
            hero.add_status("Slow", stacks, self)

################################################################################
