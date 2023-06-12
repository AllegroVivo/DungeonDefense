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

__all__ = ("InfoCardLevel",)

################################################################################
class InfoCardLevel(InfoCardComponent):

    __slots__ = (
        "_font",
    )

################################################################################
    def __init__(self, parent: DMInfoCard):

        super().__init__(parent, (parent.WIDTH, parent.HEIGHT // 7), Vector2(0, 125))

        self._font: Font = Font("assets/fonts/raleway.ttf", 14)

################################################################################
    def render(self, surface: Surface) -> None:

        text_rect = self.text.get_rect(
            center=(self._surface.get_width() // 2, (self._surface.get_height() // 2) + 2)
        )
        self._surface.blit(self.text, text_rect)

        surface.blit(self._surface, self._position)

################################################################################
    @property
    def text(self) -> Surface:

        return self._font.render(f"Lv.{self.parent_obj.level}(0.0%)", True, WHITE)  # type: ignore

################################################################################
