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

__all__ = ("FateBoardViewState",)

################################################################################
class FateBoardViewState(DMState):

    def __init__(self, game: DMGame):

        super().__init__(game)



################################################################################
    def handle_event(self, event: Event) -> None:

        if event.type == KEYDOWN:
            if event.key == K_UP:
                self.move_cursor(0, -1)
            elif event.key == K_DOWN:
                self.move_cursor(0, 1)
            elif event.key == K_LEFT:
                self.move_cursor(-1, 0)
            elif event.key == K_RIGHT:
                self.move_cursor(1, 0)
            elif event.key == K_SPACE:
                self.highlight_currently_selected_cell()
            elif event.key == K_END:
                self.quit = True

################################################################################
    def update(self, dt: float) -> None:

        pass

################################################################################
    def draw(self, screen: Surface) -> None:

        screen.fill(BLACK)

        self.game.fateboard.draw(screen)

################################################################################
    def move_cursor(self, dx: int, dy: int) -> None:

        self.game.fateboard.move_cursor(dx, dy)

################################################################################
    def highlight_currently_selected_cell(self) -> None:

        self.game.fateboard.highlight_selected_cell()

################################################################################
