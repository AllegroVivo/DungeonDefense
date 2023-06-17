from __future__ import annotations

import pygame

from typing import TYPE_CHECKING, List, Optional, Union

from .state     import DMState
from dm.states  import STATE_MAPPINGS
from utilities  import *

if TYPE_CHECKING:
    from pygame         import Surface
    from pygame.event   import Event

    from dm.core.game   import DMGame
################################################################################

__all__ = ("DMStateMachine",)


################################################################################
class DMStateMachine:
    __slots__ = (
        "game",
        "_states",
        "_previous_state"
    )

################################################################################
    def __init__(self, game: DMGame):

        self.game: DMGame = game

        self._states: List[DMState] = []
        self._previous_state: Optional[DMState] = None

################################################################################
    def __repr__(self) -> str:

        ret = f"<StateStackManager -- Stack breakdown from current to last:"
        count = 1

        for state in reversed(self._states):
            ret += f"\n{count}. {state}"
            count += 1

        return ret + ">"

################################################################################
    @property
    def previous_state(self) -> Optional[DMState]:

        return self._previous_state

################################################################################
    @property
    def current_state(self) -> DMState:

        return self._states[-1]

################################################################################
    @property
    def states(self) -> List[DMState]:

        return self._states

################################################################################
    def push_state(self, state: Union[str, DMState]) -> None:

        if isinstance(state, str):
            cls = STATE_MAPPINGS.get(state)
            if cls:
                self._states.append(cls(self.game))
        elif isinstance(state, DMState):
            self._states.append(state)

################################################################################
    def pop_state(self) -> bool:

        if not self._states:
            return False

        self._previous_state = self._states.pop()

        return True

################################################################################
    def switch_state(self, state: Union[str, DMState]) -> None:

        if self._states:
            self._previous_state = self._states.pop()

        self.push_state(state)

################################################################################
    def clear_previous_state(self) -> None:

        self._previous_state = None

################################################################################
    def handle_event(self, event: Event) -> None:

        if self._states:
            self.current_state.handle_event(event)

################################################################################
    def update(self, dt: float) -> None:

        if self._states:
            state = self.current_state
            state.update(dt)

            if state.quit:
                self._previous_state = self._states.pop()
                if not self._states:
                    self.game.quit()
            elif state.next_state:
                self.push_state(state.next_state)
                state.next_state = None

################################################################################
    def draw(self, screen: Surface):

        if self._states:
            # screen.fill(BLACK)
            self.current_state.draw(screen)

            pygame.display.flip()

################################################################################
