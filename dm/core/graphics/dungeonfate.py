from __future__ import annotations

import pygame

from pygame         import Surface, Vector2
from pygame.font    import Font
from typing         import TYPE_CHECKING

from .fatecardlg import FateCardGraphicalLg
from utilities  import *

if TYPE_CHECKING:
    from dm.core.fates import DMFateCard
################################################################################

__all__ = ("DungeonFateGraphical",)

################################################################################
class DungeonFateGraphical(FateCardGraphicalLg):

    def __init__(self, parent: DMFateCard):

        super().__init__(parent)

        self._font: Font = Font("assets/fonts/raleway.ttf", 24)

################################################################################
    def load_sprites(self) -> None:

        self._sprite = pygame.image.load(
            f"assets/sprites/fates/"
            f"dungeon/{self._parent.__class__.__name__.lower()[:-4]}.png"
        )
        # self._sprite = pygame.transform.scale(self._sprite, (40, 55))

################################################################################
    def draw(self, surface: Surface, position: Vector2) -> None:

        super().draw(surface, position)

        title_rect = self.title.get_rect()
        title_rect.center = position
        title_rect.x += 64
        title_rect.y += 165  # just go with the magic number.

        surface.blit(self.title, title_rect)

################################################################################
    @property
    def title(self) -> Surface:

        return Font("assets/fonts/raleway.ttf", 14).render(self._parent.name, True, WHITE)

################################################################################
