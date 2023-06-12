from __future__ import annotations

import pygame

from pygame     import Surface, Vector2
from typing     import TYPE_CHECKING, Optional, Type, TypeVar

from utilities  import *

if TYPE_CHECKING:
    from dm.core    import DMFateCard
################################################################################

__all__ = ("FateCardGraphicalSm",)

FC = TypeVar("FC", bound="FateCardGraphical")

################################################################################
class FateCardGraphicalSm:

    __slots__ = (
        "_parent",
        "_sprite",
    )

################################################################################
    def __init__(self, parent: DMFateCard):

        self._parent: DMFateCard = parent
        self._sprite: Optional[Surface] = None

        self.load_sprites()

################################################################################
    def load_sprites(self) -> None:

        self._sprite = pygame.image.load(
            f"assets/sprites/fates/"
            f"small/{self._parent.__class__.__name__.lower()[:-4]}.png"
        )
        self._sprite = pygame.transform.scale(self._sprite, (40, 55))

################################################################################
    @property
    def position(self) -> Vector2:

        return self._parent.position

################################################################################
    def draw(self, surface: Surface) -> None:

        # Calculate position
        pos_x = (self.position.x * (FATE_CARD_WIDTH_SMALL + 10)) + 70

        if self._parent._highlighted or self._parent._cursor:
            # Calculate size of the red border rectangle
            border_width = self._sprite.get_width() + 6  # 6 pixels wider than the sprite
            border_height = self._sprite.get_height() + 6  # 6 pixels taller than the sprite

            # Calculate position of the red border rectangle
            border_x = pos_x - 3  # 3 pixels to the left of the sprite

            # Draw the border rectangle if applicable
            pygame.draw.rect(
                surface,
                YELLOW if self._parent._cursor else GREEN,
                pygame.Rect(border_x, 0, border_width, border_height)
            )

        # Draw the card to the screen
        surface.blit(self._sprite, (pos_x, 3))

################################################################################
    def update(self, dt: float) -> None:

        pass

################################################################################
    def _copy(self, parent: DMFateCard) -> FateCardGraphicalSm:
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

        return new_obj

################################################################################
