from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.states      import DMState
from .confirmcancel import ConfirmCancelState
from utilities          import *

if TYPE_CHECKING:
    from pygame         import Surface
    from pygame.event   import Event

    from ...core.game.game    import DMGame
################################################################################

__all__ = ("MonsterInventorySelectState",)

################################################################################
class MonsterInventorySelectState(DMState):

    __slots__ = (

    )

################################################################################
    def __init__(self, game: DMGame):

        super().__init__(game)

        # Just in case, since the events in this state rely on this attribute.
        self.game.state_machine.clear_previous_state()

        # Start the highlight box on the first monster.
        self.game.inventory.monsters[0].highlight(True)

################################################################################
    def handle_event(self, event: Event) -> None:

        # Make sure to clear the previous state if listening for Confirm/Cancel state.

        # Handle highlighting movement
        self.game.inventory.handle_event(event)

        # Override handle selection behavior in subclasses.
        if event.type == KEYDOWN:
            pass

################################################################################
    def update(self, dt: float) -> None:

        pass

################################################################################
    def draw(self, screen: Surface) -> None:

        screen.fill(BLACK)
        self.game.inventory.draw_monsters(screen)

################################################################################
    def handle_selection(self) -> None:

        monster = self.game.inventory.get_highlighted_monster()

        self.game.push_state(
            ConfirmCancelState(
                self.game,
                f"Upgrade {monster.name}?",
                f"This will increase {monster.name}'s ranking to {monster.rank}."
            )
        )

################################################################################
