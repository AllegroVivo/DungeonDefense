from __future__ import annotations

import random

from pygame     import Surface
from typing     import TYPE_CHECKING, List, Literal, Optional

from ..contexts.gold import GoldAcquiredContext
from ..objects.monster  import DMMonster
from ..objects.object import DMObject
from utilities  import *

if TYPE_CHECKING:
    from pygame.event  import Event
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("DMInventory",)

################################################################################
class DMInventory:

    __slots__ = (
        "_game",
        "_gold",
        "_soul",
        "monsters",
    )

    MONSTERS_PER_ROW = 8

################################################################################
    def __init__(self, game: DMGame):

        self._game: DMGame = game

        self.monsters: List[DMMonster] = []
        self._gold: int = 250
        self._soul: int = 0

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
    def handle_event(self, event: Event) -> None:

        if event.type == KEYDOWN:
            if self.get_highlighted_monster() is None:
                return

            current_highlight = self.get_highlighted_monster()
            idx = self.monsters.index(current_highlight)

            if event.key == K_UP:
                # Keeps the cursor from moving above the grid
                idx = max(idx - self.MONSTERS_PER_ROW, 0)
            elif event.key == K_DOWN:
                # Keeps the cursor from moving below the grid
                idx = min(idx + self.MONSTERS_PER_ROW, len(self.monsters) - 1)
            elif event.key == K_LEFT:
                # Keeps the cursor from wrapping around to the previous row
                if (idx - 1) % self.MONSTERS_PER_ROW != 0 or idx == 1:
                    idx = max(0, idx - 1)
            elif event.key == K_RIGHT:
                # Keeps the cursor from wrapping around to the next row
                if (idx + 1) % self.MONSTERS_PER_ROW != 0 or idx == 0:
                    idx = min(idx + 1, len(self.monsters) - 1)

            current_highlight.highlight(False)
            self.monsters[idx].highlight(True)

################################################################################
    def draw_monsters(self, screen: Surface) -> None:

        for monster in self.monsters:
            monster.draw_zoom(screen)

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
    def get_highlighted_monster(self) -> Optional[DMMonster]:

        for monster in self.monsters:
            if monster.highlighted:
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

        # Dispatch the event so the other game elements can edit the amount
        ctx = GoldAcquiredContext(self._game, amount)
        self._game.dispatch_event("gold_acquired", ctx=ctx)

        # Then add the gold to the inventory.
        self._gold += int(ctx.calculate())

################################################################################
    def add_soul(self, amount: int) -> None:

        if not isinstance(amount, (int, float)):
            raise ArgumentTypeError(
                "DMInventory.add_soul()",
                type(amount),
                type(int), type(float)
            )

        self._soul += int(amount)
        # self._game.publish_event("soul_acquired", amount=amount)

################################################################################
    def add_monster(self, monster: DMMonster) -> None:

        if not isinstance(monster, DMMonster):
            raise ArgumentTypeError("DMInventory.add_monster()", type(monster), type(DMMonster))

        self.monsters.append(monster)

################################################################################
    def add_item(self, item: DMObject) -> None:

        if not isinstance(item, DMObject):
            raise ArgumentTypeError("DMInventory.add_item()", type(item), type(DMObject))

        # Depending on the kind of item, add it to the appropriate manager.
        if isinstance(item, DMMonster):
            self.add_monster(item)
        # etc...

################################################################################
