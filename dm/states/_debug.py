from __future__ import annotations

from typing     import TYPE_CHECKING

from .menus.confirmcancel import ConfirmCancelState
from .menus.popup import PopupDialogState
from ._dng_select import DungeonSelectState
from utilities          import *

if TYPE_CHECKING:
    from pygame         import Surface
    from pygame.event   import Event

    from ..core.game.game    import DMGame
################################################################################

__all__ = ("_DebugState",)

################################################################################
class _DebugState(DungeonSelectState):

    def __init__(self, game: DMGame):

        super().__init__(game)

        # We need this to check for the confirm/cancel response.
        self.game.state_machine.clear_previous_state()

################################################################################
    def handle_event(self, event: Event) -> None:

        previous_state = self.game.state_machine.previous_state
        if previous_state is not None:
            if previous_state.selection == 0:  # type: ignore
                self.process_upgrade()
                self.game.switch_state("fate_select")
            else:
                self.game.state_machine.clear_previous_state()

        super().handle_event(event)

        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                self.handle_selection()

################################################################################
    def update(self, dt: float) -> None:

        super().update(dt)

################################################################################
    def draw(self, screen: Surface) -> None:

        super().draw(screen)

################################################################################
    def handle_selection(self) -> None:

        room = self.game.dungeon.get_highlighted_room()

        if room.room_type in (DMRoomType.Empty, DMRoomType.Entrance, DMRoomType.Boss):
            return

        if room.upgrades == 10:
            self.game.push_state(
                PopupDialogState(
                    self.game,
                    "Unable to Upgrade",
                    "This room is already at the maximum rank."
                )
            )
            return

        self.game.push_state(
            ConfirmCancelState(
                self.game,
                f"Upgrade {room.name}?",
                f"This will increase {room.name}'s ranking to {room.rank + 1}."
            )
        )

################################################################################
    def process_upgrade(self) -> None:

        room = self.game.dungeon.get_highlighted_room()
        room.upgrade()

################################################################################
