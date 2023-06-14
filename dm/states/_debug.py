from __future__ import annotations

from pygame         import Surface
from typing         import TYPE_CHECKING

from ..core.states      import DMState
from utilities          import *

if TYPE_CHECKING:
    from pygame.event   import Event

    from dm.core    import DMBattleManager, DMGame
################################################################################

__all__ = ("_DebugState",)

################################################################################
class _DebugState(DMState):

    def __init__(self, game: DMGame):

        super().__init__(game)

################################################################################
    def handle_event(self, event: Event) -> None:

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                # Pause
                pass

################################################################################
    def draw(self, screen: Surface) -> None:

        screen.fill(BLACK)

        self.game.battle_mgr.draw(screen)

################################################################################
    def update(self, dt: float) -> None:

        self.game.battle_mgr.update(dt)

################################################################################
