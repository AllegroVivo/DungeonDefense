from __future__ import annotations

import pygame

from pygame         import Surface, Vector2
from pygame.font    import Font
from typing         import TYPE_CHECKING, Optional, Type, TypeVar

from utilities  import *

if TYPE_CHECKING:
    from dm.core    import DMFateCard, DMGame
################################################################################

__all__ = ("FateCardGraphicalLg",)

FC = TypeVar("FC", bound="FateCardGraphicalLg")

################################################################################
class FateCardGraphicalLg:

    __slots__ = (
        "_parent",
        "_sprite",
        "_info_text",
    )

################################################################################
    def __init__(self, parent: DMFateCard):

        self._parent: DMFateCard = parent
        self._sprite: Optional[Surface] = None
        self._info_text: Optional[Surface] = None

        self.load_sprites()

################################################################################
    def load_sprites(self) -> None:

        self._sprite = pygame.image.load(
            f"assets/sprites/fates/"
            f"large/{self._parent.__class__.__name__.lower()[:-4]}.png"
        )
        # self._sprite = pygame.transform.scale(self._sprite, (40, 55))

        self._info_text = Surface((SCREEN_WIDTH * 0.35, SCREEN_HEIGHT * 0.25))

################################################################################
    @property
    def game(self) -> DMGame:

        return self._parent.game

################################################################################
    @property
    def position(self) -> Vector2:

        return self._parent.position

################################################################################
    @property
    def title(self) -> Surface:

        return Font("assets/fonts/raleway.ttf", 48).render(self._parent.name, True, WHITE)

################################################################################
    def draw(self, surface: Surface, position: Vector2) -> None:

        surface.blit(self._sprite, position)

################################################################################
    def draw_info_section(self, surface: Surface) -> None:

        if self._parent.__class__.__name__ == "EntranceFate":
            return

        title_rect = self.title.get_rect()
        title_rect.center = Vector2(surface.get_width() // 2, SCREEN_HEIGHT * 0.15)

        sprite_rect = self._sprite.get_rect()
        sprite_rect.center = Vector2(surface.get_width() // 2, SCREEN_HEIGHT * 0.40)

        self.draw_text()
        text_rect = self._info_text.get_rect()
        text_rect.center = Vector2(surface.get_width() // 2, SCREEN_HEIGHT * 0.70)
        text_rect.y += 40

        surface.blit(self.title, title_rect)
        surface.blit(self._sprite, sprite_rect)
        surface.blit(self._info_text, text_rect)

################################################################################
    def draw_text(self) -> None:

        text_dict = text_to_multiline_rect(
            self._parent.description,
            self._info_text.get_rect(),
            25,
            self._font.render("X", True, WHITE).get_height()
        )

        for text, text_rect in text_dict.items():
            text_surface = self._font.render(text, True, WHITE)

            # Center the text within its rectangle by adjusting its x position
            text_pos = text_surface.get_rect(center=text_rect.center)

            self._info_text.blit(text_surface, text_pos)

################################################################################
    def update(self, dt: float) -> None:

        pass

################################################################################
    def _copy(self, parent: DMFateCard) -> FateCardGraphicalLg:
        """Returns a clean copy of the current Fate Card's small graphics data.

        Parameters:
        -----------
        parent: :class:`DMFateCard`
            The instance of :class:`DMFateCard` that this will be attached to.
            Note: This is required.

        Returns:
        --------
        :class:`FateCardGraphicalSM`
            A fresh copy of the current Graphical component.
        """

        cls: Type[FC] = type(self)
        new_obj = cls.__new__(cls)

        new_obj._parent = parent
        new_obj._sprite = self._sprite.copy()
        new_obj._info_text = self._info_text
        new_obj._font = self._font

        return new_obj

################################################################################
