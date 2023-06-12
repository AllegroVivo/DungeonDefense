from __future__ import annotations

from pygame         import Vector2
from pygame.font    import Font
from typing         import TYPE_CHECKING, Optional

from dm.states._dng_select import DungeonSelectState
from .manual_deploy_b   import ManualDeployStateB
from utilities      import *

if TYPE_CHECKING:
    from pygame         import Surface
    from pygame.event   import Event

    from dm.core    import DMGame, DMRoom
################################################################################

__all__ = ("ManualDeployStateA",)

################################################################################
class ManualDeployStateA(DungeonSelectState):
    __slots__ = (
        "_prev",
    )

################################################################################
    def __init__(self, game: DMGame):

        super().__init__(game)

        self._prev: Optional[DMRoom] = None

################################################################################
    def handle_event(self, event: Event) -> None:

        super().handle_event(event)

        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                if self._prev is not None:
                    self.quit = True
                else:
                    self.next_state = "manual_deploy_b"

################################################################################
    def update(self, dt: float) -> None:

        pass

################################################################################
    def draw(self, screen: Surface) -> None:

        super().draw(screen)

        color = RED if self._prev is not None else WHITE
        text = self.font.render("Go Back", True, color)

        text_rect = text.get_rect()
        text_rect.center = (575, 600)

        screen.blit(text, text_rect)

################################################################################
    @property
    def font(self) -> Font:

        return Font(None, 48)

################################################################################
    def move_cursor(self, dx: int, dy: int) -> None:

        # If the previous room is set, (ie. the text is selected), then the
        # only direction we can move is up.
        if self._prev is not None:
            if dx == -1:
                self._prev.toggle_highlighting(True)
                self._prev = None
            return

        # Get the current room
        cur_room = self.game.dungeon.get_highlighted_room()
        if cur_room is None:
            return

        # Calculate desired target position.
        position = cur_room.position
        target = Vector2(position.x + dx, position.y + dy)

        # Disallow movement into entry and boss tiles (as toggled)
        if target.y in {0 if self._boss else -1, self.game.map.width - 1}:
            return

        # If we're moving to the text, set the previous location so we can
        # move back to it, and clear all highlighting.
        if target.x == self.game.map.height:
            self._prev = cur_room
            self.game.dungeon.reset_highlighting()

            # Then select the text

        # Otherwise highlight as normal if the cell is present.
        room = self.game.get_room_at(target)
        if room is not None:
            self.game.dungeon.reset_highlighting()
            room.toggle_highlighting(True)

################################################################################
