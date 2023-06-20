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

    def __init__(self, game: DMGame):

        super().__init__(game)

        # Just in case, since the events in this state rely on this attribute.
        self.game.state_machine.clear_previous_state()

        # Start the highlight box on the first monster.
        self.game.inventory.monsters[0].highlight(True)

################################################################################
    def handle_event(self, event: Event) -> None:

        # We clear the previous state on initialization so we can watch for
        # the exit from the ConfirmCancelState and check the result.
        previous_state = self.game.state_machine.previous_state
        if previous_state.__class__.__name__ == "ConfirmCancelState":
            # Index 0 is "Confirm"
            if previous_state.selection == 0:  # type: ignore
                # Do the upgrade
                monster = self.game.inventory.get_highlighted_monster()
                monster.upgrade()
                # And clear the highlight.
                monster.highlight(False)
                # Proceed to the next state.
                self.game.push_state("fate_select")
            # Index 1 is "Cancel".
            else:
                # Clear the state so we can continue watching.
                self.game.state_machine.clear_previous_state()

        # Handle highlighting movement
        self.game.inventory.handle_event(event)

        # Handle selection
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                self.handle_selection()

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
