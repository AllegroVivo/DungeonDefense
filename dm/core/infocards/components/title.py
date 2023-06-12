from __future__ import annotations

import pygame

from pygame         import Surface, Vector2
from pygame.font    import Font
from typing         import TYPE_CHECKING

from ._component    import InfoCardComponent
from utilities      import *

if TYPE_CHECKING:
    from dm.core    import DMInfoCard
################################################################################

__all__ = ("InfoCardTitle",)

################################################################################
class InfoCardTitle(InfoCardComponent):

    __slots__ = (
        "_font",
    )

    LINE_COLOR = (126, 60, 0, 255)

################################################################################
    def __init__(self, parent: DMInfoCard):

        super().__init__(parent, (parent.WIDTH, parent.HEIGHT // 5), Vector2(0, 0))

        self._font: Font = Font("assets/fonts/raleway.ttf", 18)

################################################################################
    def render(self, surface: Surface) -> None:

        text_rect = self.text.get_rect(
            center=(self._surface.get_width() // 2, (self._surface.get_height() // 2) + 2)
        )
        self._surface.blit(self.text, text_rect)
        self._surface.set_colorkey(BLACK)

        # Then a horizontal rule under that for looks.
        pygame.draw.line(
            self._surface,
            self.LINE_COLOR,
            (self._size[0] * 0.12, self._surface.get_height() - 3),
            (self._size[0] - (self._size[0] * 0.12), self._surface.get_height() - 3)
        )

        surface.blit(self._surface, self._position)

################################################################################
    @property
    def text(self) -> Surface:

        return self._font.render(self._parent._obj.name, True, WHITE)

################################################################################
