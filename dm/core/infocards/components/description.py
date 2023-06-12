from __future__ import annotations

import pygame

from pygame         import Surface, Vector2
from pygame.font    import Font
from typing         import TYPE_CHECKING, Optional

from ._component    import InfoCardComponent
from utilities      import *

if TYPE_CHECKING:
    from dm.core    import DMInfoCard
################################################################################

__all__ = ("InfoCardDescription",)

################################################################################
class InfoCardDescription(InfoCardComponent):

    __slots__ = (
        "_font",
    )

    BG_COLOR = ( 26,  17,  12, 255)

################################################################################
    def __init__(self, parent: DMInfoCard):

        super().__init__(
            parent,
            (parent.WIDTH * 0.88, parent.HEIGHT * 0.35),
            Vector2(parent.WIDTH * 0.06, parent.HEIGHT * 0.50)
        )
        self.prepare_surface()

        self._font = Font(None, 16)

################################################################################
    def prepare_surface(self) -> None:

        self._surface = rounded_rect(self._size, self.BG_COLOR)

################################################################################
    def render(self, surface: Surface) -> None:

        text_rect = self.text.get_rect()
        text_rect.center = self._surface.get_rect().center

        multicolor_text(self.parent_obj.description, self._surface, Font(None, 16), text_rect)

        surface.blit(self._surface, self._position)

################################################################################
    @property
    def text(self) -> Surface:

        text_surface = Surface((self._size[0] - 10, self._size[1] - 10))

        for i, line in enumerate(text_to_multiline_str(self.parent_obj.description, 40)):
            line_surface = self._font.render(line, True, WHITE)
            text_surface.blit(
                line_surface,
                (self._position.x, self._position.y + i * self._font.get_linesize())
            )

        return text_surface

################################################################################
