from __future__ import annotations

from typing     import TYPE_CHECKING, Callable, Dict, List

from utilities  import _EVENT_REFERENCE

if TYPE_CHECKING:
    from .game  import DMGame
################################################################################

__all__ = ("DMEventManager", )

################################################################################
class DMEventManager:

    __slots__ = (
        "_state",
        "subscribers",
    )

################################################################################
    def __init__(self, game: DMGame):

        self._state: DMGame = game

        self.subscribers: Dict[str, List[Callable]] = {}
        self._init_subscriber_dict()

################################################################################
    def _init_subscriber_dict(self) -> None:

        for event in _EVENT_REFERENCE:
            self.subscribers[event] = []

################################################################################
    def subscribe(self, event_type: str, callback: Callable) -> None:

        if event_type not in self.subscribers:
            raise TypeError(f"Invalid event name [{event_type}] passed to EventManager.subscribe().")

        if not callable(callback):
            raise TypeError("Invalid observer passed to EventManager.subscribe().")

        if callback in self.subscribers[event_type]:
            return

        self.subscribers[event_type].append(callback)

################################################################################
    def unsubscribe(self, event_type: str, callback: Callable) -> None:

        if event_type not in self.subscribers:
            raise TypeError("Invalid event name passed to EventManager.unsubscribe().")

        self.subscribers[event_type].remove(callback)

################################################################################
    def dispatch(self, event_type: str, *context) -> None:

        # Might just make this a pass depending on if I go crazy making event types
        if event_type not in self.subscribers:
            raise TypeError(f"Invalid event name `{event_type}` passed to EventManager.dispatch().")

        for callback in self.subscribers[event_type]:
            callback(*context)

################################################################################
