from __future__ import annotations

import random

from pygame     import Surface
from typing     import TYPE_CHECKING, List, Literal, Optional

from ..objects  import DMMonster
from utilities  import *

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("DMInventory",)

################################################################################
class InventoryMonster:

    __slots__ = (
        "_parent",
        "_highlighted",
    )

################################################################################
    def __init__(self, parent: DMMonster):

        self._parent: DMMonster = parent
        self._highlighted: bool = False

################################################################################
    def highlight(self) -> None:

        self._highlighted = True

################################################################################
    def clear_highlight(self) -> None:

        self._highlighted = False

################################################################################
    @property
    def zoom_sprite(self) -> Surface:

        return self._parent.graphics.zoom  # type: ignore

################################################################################
class DMInventory:

    __slots__ = (
        "_game",
        "_gold",
        "monsters",
    )

################################################################################
    def __init__(self, game: DMGame):

        self._game: DMGame = game

        self.monsters: List[DMMonster] = []
        self._gold: int = 250

        self._init_starter_monsters()

################################################################################
    def _init_starter_monsters(self):

        # self.monsters = [self._game.spawn(
        #     spawn_type=SpawnType.Monster, end_rank=3)(self._game) for _ in range(10)
        # ]
        self.monsters = [self._game.spawn(
            obj_id="MON-XXX")(self._game) for _ in range(10)
        ]

################################################################################
    def get_random_inventory_monster(self, strongest: bool = True) -> Optional[DMMonster]:

        if not self.monsters:
            return

        if strongest:
            self.sort_monsters()
            return self.monsters.pop(0)
        else:
            monster = random.choice(self.monsters)
            self.monsters.remove(monster)
            return monster

################################################################################
    def sort_monsters(self, sort_type: Literal["strength"] = "strength") -> None:
        """Sorts the inventory by monster strength, from strongest to weakest."""

        def stat_score(monster):
            """Calculates the stat score of a monster."""
            return (monster.life + monster.attack + monster.defense) * monster.level + monster.experience

        if sort_type == "strength":
            self.monsters.sort(key=stat_score, reverse=True)

################################################################################
    def add_gold(self, amount: int) -> None:

        if not isinstance(amount, (int, float)):
            raise ArgumentTypeError(
                "DMInventory.add_gold()",
                type(amount),
                type(int), type(float)
            )

        self._gold += amount
        # self._game.publish_event("gold_acquired", amount=amount)

################################################################################
    def add_monster(self, monster: DMMonster) -> None:

        if not isinstance(monster, DMMonster):
            raise ArgumentTypeError("DMInventory.add_monster()", type(monster), type(DMMonster))

        self.monsters.append(monster)

################################################################################
