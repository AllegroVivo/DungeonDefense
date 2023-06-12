from __future__ import annotations

from pygame     import Surface, Vector2
from typing     import TYPE_CHECKING, List, Optional

from .fateboardrow  import DMFateBoardRow
from utilities      import *

if TYPE_CHECKING:
    from dm.core        import DMFateCard, DMGame
################################################################################
class DMFateBoard:

    __slots__ = (
        "_state",
        "_surface",
        "_info_surface",
        "_grid",
        "_player_pos",
        "_cursor_pos",
        "_y_offset"
    )

################################################################################
    def __init__(self, game: DMGame):

        self._state: DMGame = game

        self._grid: List[DMFateBoardRow] = [DMFateBoardRow(self, y) for y in range(FATE_BOARD_HEIGHT + 1)]
        self._surface: Surface = Surface((self.width, self.height))
        self._info_surface: Surface = Surface((SCREEN_WIDTH * 0.50, self.height))

        # Don't try to calculate this and be fancy. You fucked
        # it up like 7 times. Just use the magic number.
        self._y_offset: int = -560
        self._player_pos: Vector2 = Vector2(5, 20)  # Start at bottom-center
        self._cursor_pos: Vector2 = Vector2(5, 20)  # Start at bottom-center

################################################################################
    def __getitem__(self, index: int) -> DMFateBoardRow:

        return self._grid[index]

################################################################################
    @property
    def height(self) -> int:

        return (21 * (FATE_CARD_HEIGHT + FATE_PADDING)) + EDGE_PADDING // 2

################################################################################
    @property
    def width(self) -> int:

        return SCREEN_WIDTH - (SCREEN_WIDTH * 0.5)

################################################################################
    def draw(self, screen: Surface) -> None:

        self._surface.fill(BLACK)
        self._info_surface.fill(BLACK)

        for row in self._grid:
            row.draw(self._surface, self._info_surface)

        screen.blit(self._info_surface, (SCREEN_WIDTH * 0.50, 0))
        screen.blit(self._surface, (0, self._y_offset))

################################################################################
    def get_card(self, pos: Vector2) -> Optional[DMFateCard]:

        try:
            return self._grid[int(pos.y)][int(pos.x)]
        except IndexError:
            return

################################################################################
    def move_cursor(self, dx: int, dy: int) -> None:

        new_pos = self._cursor_pos + Vector2(dx, dy)

        # Check bounds and see if the new position is valid
        if (0 <= new_pos.x < FATE_BOARD_WIDTH) and (0 <= new_pos.y < FATE_BOARD_HEIGHT + 1):
            # Reset highlight of the old position
            old_card = self.get_card(self._cursor_pos)
            if old_card is not None:
                old_card.select(False)

            # Update cursor position
            self._cursor_pos = new_pos

            # Highlight the new position
            new_card = self.get_card(new_pos)
            if new_card is not None:
                new_card.select(True)

            # Adjust y-offset and account for edge of board. The offset amounts magical. Just leave them.
            if dy > 0 and self._cursor_pos.y > 5 and self._y_offset > -560:
                self._y_offset -= 60
            elif dy < 0 and self._cursor_pos.y < 14 and self._y_offset < 40:
                self._y_offset += 60

################################################################################
    def reset_row_highlights(self, row: int) -> None:

        for card in self._grid[int(row)]:
            card.highlight(False)

################################################################################
    def get_highlighted_card_by_row(self, row: int) -> Optional[DMFateCard]:

        for card in self._grid[int(row)]:
            if card._highlighted:
                return card

################################################################################
    def highlight_selected_cell(self) -> None:

        previous_highlight = self.get_highlighted_card_by_row(self._cursor_pos.y)
        if previous_highlight is not None:
            self.reset_row_highlights(self._cursor_pos.y)

        new_card = self.get_card(self._cursor_pos)
        new_card.highlight(True)

################################################################################
    def get_next_three_cards(self) -> List[DMFateCard]:

        x = self._player_pos.x
        y = self._player_pos.y

        return [
            self.get_card(Vector2(x - 1, y - 1)),
            self.get_card(Vector2(x, y - 1)),
            self.get_card(Vector2(x + 1, y - 1))
        ]

################################################################################
