from __future__ import annotations

from pygame         import Vector2
from pygame.font    import Font
from typing         import TYPE_CHECKING, List, Optional, Tuple

from ..core.states   import DMState
from utilities      import *

if TYPE_CHECKING:
    from pygame         import Surface
    from pygame.event   import Event

    from ..core.game    import DMGame
################################################################################

__all__ = ("DungeonSelectState",)

################################################################################
class DungeonSelectState(DMState):
    __slots__ = (
        "_boss",
    )

################################################################################
    def __init__(self, game: DMGame, select_boss_room: bool = False):

        super().__init__(game)

        self._boss = select_boss_room
        self.game.dungeon.toggle_highlighting(True)

################################################################################
    def handle_event(self, event: Event) -> None:

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                self.move_cursor(0, -1)
            elif event.key == K_RIGHT:
                self.move_cursor(0, 1)
            elif event.key == K_UP:
                self.move_cursor(-1, 0)
            elif event.key == K_DOWN:
                self.move_cursor(1, 0)

################################################################################
    def update(self, dt: float) -> None:

        pass

################################################################################
    def draw(self, screen: Surface) -> None:

        screen.fill(BLACK)

        self.game.draw_dungeon()

################################################################################
    def move_cursor(self, dx: int, dy: int) -> None:

        cur_room = self.game.dungeon.get_highlighted_room()
        if cur_room is None:
            return

        position = cur_room.position
        target = Vector2(position.x + dx, position.y + dy)
        if target.y in {0 if self._boss else -1, self.game.map.width - 1}:
            return

        room = self.game.get_room_at(target)
        if room is not None:
            self.game.dungeon.reset_highlighting()
            room.toggle_highlighting(True)

################################################################################
