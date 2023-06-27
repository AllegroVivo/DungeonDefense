from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("AncientPotion",)

################################################################################
class AncientPotion(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-285",
            name="Ancient Potion",
            description=(
                "Apply 12 % of max LIFE + Regeneration, Armor, Fury as much "
                "as 100 % of LIFE lost to all monsters in the dungeon."
            ),
            rank=6,
            cooldown=CooldownType.DungeonWide
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        regeneration = self.owner.get_status("Regeneration")
        armor        = self.owner.get_status("Armor")
        fury         = self.owner.get_status("Fury")
        effect = self.owner.max_life * (regeneration.stacks + armor.stacks + fury.stacks)

        for monster in self.game.all_monsters:
            monster.heal(effect)  # `heal()` automatically clamps the amount of life restored.

################################################################################
