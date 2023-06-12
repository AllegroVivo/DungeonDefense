from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.states._vert_menu import VerticalMenuState
from utilities      import *

if TYPE_CHECKING:
    from pygame         import Surface
    from pygame.event   import Event

    from dm.core.game import DMGame
################################################################################

__all__ = ("NewGameState",)

################################################################################
class NewGameState(VerticalMenuState):

    def __init__(self, game: DMGame):

        super().__init__(
            game,
            title="New Game",
            options=[
                "Deploy Monsters",
                "Quit"
            ]
        )

################################################################################
    def handle_event(self, event: Event) -> Optional[str]:

        super().handle_event(event)

        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                if self.selection == 0:
                    self.next_state = "auto_deploy"
                elif self.selection == 1:
                    self.quit = True
        return

################################################################################
    def update(self, dt: float) -> bool:

        pass

################################################################################
    def draw(self, screen: Surface) -> None:

        screen.fill(BLACK)

        super().draw(screen)

################################################################################
