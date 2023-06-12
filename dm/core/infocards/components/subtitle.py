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

__all__ = ("InfoCardSubtitle",)

################################################################################
class InfoCardSubtitle(InfoCardComponent):

    __slots__ = (
        "_font",
    )

################################################################################
    def __init__(self, parent: DMInfoCard):

        super().__init__(parent, (parent.WIDTH, parent.HEIGHT // 7), Vector2(0, 52))

        self._font: Font = Font("assets/fonts/raleway.ttf", 12)

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

        text = ""
        if isinstance(self.parent_obj, self.game.generate_type("monster")):
            text = "Monster"
        elif isinstance(self.parent_obj, self.game.generate_type("room")):
            text = "Room"

        return self._font.render(text, True, WHITE)

################################################################################
