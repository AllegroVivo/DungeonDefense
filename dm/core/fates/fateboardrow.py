from __future__ import annotations

from pygame     import Surface
from typing     import TYPE_CHECKING, List, Optional

from utilities  import *

if TYPE_CHECKING:
    from dm.core        import DMGame
    from .fateboard     import DMFateBoard
    from .fatecard      import DMFateCard
################################################################################
class DMFateBoardRow:

    __slots__ = (
        "_parent",
        "_position",
        "_cards",
        "_surface",
    )

################################################################################
    def __init__(self, parent: DMFateBoard, position: int):

        self._parent: DMFateBoard = parent

        self._position: int = position

        self._cards: List[Optional[DMFateCard]] = []
        self._init_cards()

        self._surface: Surface = Surface((self._parent.width, self._parent.height / FATE_BOARD_HEIGHT + 1))

################################################################################
    def _init_cards(self) -> None:

        if self._position == 0:  # Boss row
            self._cards = [
                self.game.spawn(obj_id="FAT-104")(self.game, x=x, y=self._position)
                for x in range(FATE_BOARD_WIDTH)
            ]
        elif self._position == 1:  # Dungeon row
            self._cards = [
                self.game.spawn(obj_id="FAT-105")(self.game, x=x, y=self._position)
                for x in range(FATE_BOARD_WIDTH)
            ]
        elif self._position != 20:
            self._cards = [
                self.game.spawn(spawn_type=SpawnType.Fate)(self.game, x=x, y=self._position)
                for x in range(FATE_BOARD_WIDTH)
            ]
        else:
            row = [None for _ in range(FATE_BOARD_WIDTH)]
            row[5] = self.game.spawn(obj_id="ENTR-101")(self.game, x=5, y=self._position)  # type: ignore
            row[5].select(True)  # type: ignore
            self._cards = row

################################################################################
    @property
    def game(self) -> DMGame:

        return self._parent._state

################################################################################
    @property
    def cards(self) -> List[DMFateCard]:

        return self._cards

################################################################################
    def draw(self, board_surface: Surface, info_surface: Surface) -> None:

        self._surface.fill(BLACK)

        for card in self._cards:
            if card is not None:
                card.draw_small(self._surface, info_surface)

        y_offset = self._position * (FATE_CARD_HEIGHT_SMALL + 10)

        board_surface.blit(self._surface, (0, y_offset))

################################################################################
    def __getitem__(self, index: int) -> DMFateCard:

        return self._cards[index]

################################################################################
