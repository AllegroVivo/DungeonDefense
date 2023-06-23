from __future__ import annotations

from abc        import ABC, abstractmethod
from typing     import TYPE_CHECKING, Any, Callable, List, Optional
from uuid       import UUID, uuid4

if TYPE_CHECKING:
    from dm.core.game.game    import DMGame
    from dm.core.objects.room import DMRoom
################################################################################

__all__ = ("Context", )

################################################################################
class Context(ABC):

    __slots__ = (
        "_id",
        "_state",
        "_late_callback",
        "_post_execution_callbacks"
    )

################################################################################
    def __init__(self, state: DMGame):

        self._id: UUID = uuid4()
        self._state: DMGame = state

        self._late_callback: Optional[Callable] = None
        self._post_execution_callbacks: List[Callable] = []

################################################################################
    def __eq__(self, other: Context) -> bool:

        return self._id == other._id

################################################################################
    @property
    def game(self) -> DMGame:

        return self._state

################################################################################
    @property
    @abstractmethod
    def room(self) -> DMRoom:
        """Returns the room in which this context is taking place."""

        raise NotImplementedError

################################################################################
    @abstractmethod
    def execute(self) -> Optional[Any]:
        """Executes the context and returns the result of the execution."""

        raise NotImplementedError

################################################################################
    def register_late_callback(self, callback: Callable) -> None:

        if self._late_callback is not None:
            raise RuntimeError("Late callback already registered.")

        self._late_callback = callback

################################################################################
    def register_post_execute(self, callback: Callable) -> None:

        self._post_execution_callbacks.append(callback)

################################################################################
