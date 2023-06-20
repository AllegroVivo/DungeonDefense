from __future__ import annotations

from typing     import TYPE_CHECKING

from ..menus import MonsterInventorySelectState, ConfirmCancelState
from utilities          import *

if TYPE_CHECKING:
    from pygame.event   import Event

    from ...core.game.game    import DMGame
################################################################################

__all__ = ("DungeonTrainFate",)

################################################################################
class DungeonTrainFate(MonsterInventorySelectState):

    def __init__(self, game: DMGame):

        super().__init__(game)

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

        super().handle_event(event)

        # Handle selection
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                self.handle_selection()

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
