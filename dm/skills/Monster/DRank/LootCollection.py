from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("LootCollection",)

################################################################################
class LootCollection(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-197",
            name="Loot Collection",
            description=(
                "50 % chance to Gain 1 Gold when killing an enemy."
            ),
            rank=1,
            cooldown=CooldownType.Passive,
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_death")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if self.owner == ctx.source:
            if self.random.chance(50):
                self.game.inventory.add_gold(1)

################################################################################
