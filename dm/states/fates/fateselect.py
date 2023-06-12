from __future__ import annotations

import pygame

from typing     import TYPE_CHECKING, Optional

from ...core.states import DMState
from utilities      import *

if TYPE_CHECKING:
    from dm.core        import DMGame
    from pygame         import Surface
    from pygame.event   import Event
################################################################################

__all__ = ("FateCardSelectState",)

################################################################################
class FateCardSelectState(DMState):

    __slots__ = (
        "_selection",
    )

################################################################################
    def __init__(self, game: DMGame):

        super().__init__(game)

        self._selection = 0

################################################################################
    def handle_event(self, event: Event) -> None:

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                self._selection = min(self._selection + 1, 2)
            elif event.key == K_RIGHT:
                self._selection = max(self._selection - 1, 0)
            elif event.key == K_END:
                self.next_state = "fate_board_view"

################################################################################
    def update(self, dt: float) -> None:

        pass

################################################################################
    def draw(self, screen: Surface) -> None:

        screen.fill(BLACK)

        self.game.fateboard.draw(screen)

################################################################################
