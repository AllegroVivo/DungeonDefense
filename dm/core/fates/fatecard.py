from __future__ import annotations

import pygame.draw
from pygame     import Rect, Surface, Vector2
from typing     import TYPE_CHECKING, Type, TypeVar

from ..graphics     import FateCardGraphicalSm, FateCardGraphicalLg
from ..objects      import DMObject
from utilities      import *

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("DMFateCard",)

FC = TypeVar("FC", bound="DMFateCard")

################################################################################
class DMFateCard(DMObject):

    __slots__ = (
        "_small_sprite",
        "_large_sprite",
        "_position",
        "_cursor",
        "_highlighted",
        "_selected",
        "next_state"
    )

    FTYPE: FateType = None

################################################################################
    def __init__(
        self,
        state: DMGame,
        _id: str,
        name: str,
        description: str,
        position: Vector2,
        rank: int,
        next_state: str
    ):

        super().__init__(state, _id, name, description, rank)

        self._small_sprite: FateCardGraphicalSm = None  # Type: ignore
        self._large_sprite: FateCardGraphicalLg = None  # Type: ignore

        self._load_sprites()

        self._position: Vector2 = position
        self._highlighted: bool = False
        self._cursor: bool = False
        self._selected: bool = False

        self.next_state: str = next_state

################################################################################
    def _load_sprites(self) -> None:

        self._small_sprite = FateCardGraphicalSm(self)
        self._large_sprite = FateCardGraphicalLg(self)

################################################################################
    def highlight(self, state: bool) -> None:

        self._highlighted = state

################################################################################
    def select(self, state: bool) -> None:

        self._cursor = state

################################################################################
    @property
    def position(self) -> Vector2:

        return self._position

################################################################################
    def draw_small(self, row_surface: Surface, info_surface: Surface) -> None:

        self._small_sprite.draw(row_surface)
        if self._cursor:
            self._large_sprite.draw_info_section(info_surface)

################################################################################
    def draw_large(self, surface: Surface, selected: bool) -> None:

        if self.game.fateboard._player_pos.x > self.position.x:
            index = 0
        elif self.game.fateboard._player_pos.x == self.position.x:
            index = 1
        else:
            index = 2

        card_pos = Vector2(EDGE_PADDING + (index * (FATE_CARD_WIDTH + 200)), 100)

        if self._highlighted or selected:
            color = YELLOW if self._highlighted else RED
            pygame.draw.rect(
                surface,
                color,
                Rect(
                    card_pos.x - 3,
                    card_pos.y - 3,
                    self._large_sprite._sprite.get_width() + 6,
                    self._large_sprite._sprite.get_height() + 6
                )
            )

        self._large_sprite.draw(surface, card_pos)

################################################################################
    def _copy(self, **kwargs) -> DMFateCard:
        """Returns a clean copy of the current fate card type with any given
        kwargs substituted in.

        Parameters:
        -----------
        x: :class:`int`
            The new card's x-location within the Fate Card grid.
        y: :class:`int`
            The new card's y-location within the Fate Card grid.

        Returns:
        --------
        :class:`DMFateCard`
            A fresh copy of the current FateCard object at the given position.
        """

        new_obj: Type[FC]  = super()._copy()  # type: ignore

        new_obj._small_sprite = self._small_sprite._copy(new_obj)
        new_obj._large_sprite = self._large_sprite._copy(new_obj)

        new_obj._position = Vector2(kwargs.pop("x"), kwargs.pop("y"))

        new_obj._highlighted = False
        new_obj._cursor = False
        new_obj._selected = False

        new_obj.next_state = self.next_state

        new_obj._alpha = 0

        return new_obj

################################################################################
