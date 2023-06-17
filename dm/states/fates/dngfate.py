from __future__ import annotations

from typing     import TYPE_CHECKING, List

from dm.fates.dng   import *
from dm.core.states      import DMState
from ..menus.confirmcancel import ConfirmCancelState
from utilities import *

if TYPE_CHECKING:
    from pygame         import Surface
    from pygame.event   import Event

    from ...core.game.game import DMGame
################################################################################

__all__ = ("DungeonFateState",)

################################################################################
class DungeonFateState(DMState):

    __slots__ = (
        "_selection",
        "_options"
    )

################################################################################
    def __init__(self, game: DMGame):

        super().__init__(game)

        self._options: List[DungeonFateCard] = []
        self._selection: int = 0

        # Just in case, since the events in this state rely on this attribute.
        self.game.state_machine.clear_previous_state()

        self._init_cards()

################################################################################
    def _init_cards(self) -> None:

        self._options = [
            RestFate(self.game),
            UpgradeFate(self.game),
            TrainFate(self.game),
            ReadingFate(self.game),
            TortureFate(self.game),
            RoomSwapFate(self.game)
        ]

################################################################################
    def handle_event(self, event: Event) -> None:

        # We clear the previous state on initialization so we can watch for
        # the exit from the ConfirmCancelState and check the result.
        previous_state = self.game.state_machine.previous_state
        if previous_state.__class__.__name__ == "ConfirmCancelState":
            # Index 0 is "Confirm"
            if previous_state.selection == 0:  # type: ignore
                self.game.state_machine.push_state(self.next_state)
            # Index 1 is "Cancel". 
            else:
                # Clear the state so we can continue watching.
                self.game.state_machine.clear_previous_state()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                self._selection = max(self._selection - 1, 0)
            elif event.key == K_RIGHT:
                self._selection = min(self._selection + 1, len(self._options) - 1)
            elif event.key == K_RETURN:
                for card in self._options:
                    if card.position.x == self._selection:
                        self.game.state_machine.push_state(
                            ConfirmCancelState(
                                self.game,
                                "Rest for a day?",
                                f"You will recover {self.game.dark_lord.max_life * 30} LIFE."
                            )
                        )

################################################################################
    def update(self, dt: float) -> None:

        pass

################################################################################
    def draw(self, screen: Surface) -> None:

        screen.fill(BLACK)

        for i, card in enumerate(self._options):
            card.draw_large(screen, self._selection == card.position.x)

################################################################################
