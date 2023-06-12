from __future__ import annotations

from abc        import ABC, abstractmethod
from typing     import TYPE_CHECKING, Callable, List

from uuid       import UUID, uuid4

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("Context", )

################################################################################
class Context(ABC):

    __slots__ = (
        "_id",
        "_state",
        "_post_execution_callbacks"
    )

################################################################################
    def __init__(self, state: DMGame):

        self._id: UUID = uuid4()
        self._state: DMGame = state
        self._post_execution_callbacks: List[Callable] = []

################################################################################
    def __eq__(self, other: Context) -> bool:

        return self._id == other._id

################################################################################
    @abstractmethod
    def execute(self) -> None:

        raise NotImplementedError

################################################################################
    def register_after_execute(self, callback: Callable) -> None:

        self._post_execution_callbacks.append(callback)

################################################################################
