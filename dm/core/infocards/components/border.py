from __future__ import annotations

import pygame

from pygame         import Surface, Vector2
from typing         import TYPE_CHECKING, Optional

from ._component    import InfoCardComponent
from utilities      import *

if TYPE_CHECKING:
    from dm.core    import DMInfoCard
################################################################################

__all__ = ("InfoCardBorder",)

################################################################################
class InfoCardBorder(InfoCardComponent):

    __slots__ = (
        "_sprite",
    )

################################################################################
    def __init__(self, parent: DMInfoCard):

        super().__init__(parent, (parent.WIDTH, parent.HEIGHT), Vector2(0, 0))

        self._sprite: Optional[Surface] = None
        self.prepare_surface()

################################################################################
    def prepare_surface(self) -> None:

        sprite = pygame.image.load("assets/sprites/misc/cardborder.png")

        self._sprite = pygame.transform.scale(sprite, self._size)
        self._sprite.set_colorkey(BLACK)

        self._surface.blit(self._sprite, (0, 0))

################################################################################
    def render(self, surface: Surface) -> None:

        surface.blit(self._surface, self._position)

################################################################################
