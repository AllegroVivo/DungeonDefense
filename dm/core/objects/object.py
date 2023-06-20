from __future__ import annotations

from uuid       import UUID, uuid4
from typing     import TYPE_CHECKING, Optional, Type, TypeVar

from utilities  import *

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("DMObject", )

DMObj = TypeVar("DMObj", bound="DMObject")

################################################################################
class DMObject:

    __slots__ = (
        "_uuid",
        "_state",
        "_id",
        "name",
        "description",
        "rank",
        "unlock",
    )

################################################################################
    def __init__(
        self,
        state: DMGame,
        _id: str,
        name: str,
        description: Optional[str],
        rank: int = 0,
        unlock: Optional[UnlockPack] = None
    ):

        self._uuid: UUID = uuid4()
        self._state: DMGame = state

        self._id: str = _id
        self.name: str = name
        self.description: Optional[str] = description
        self.rank: int = rank
        self.unlock: Optional[UnlockPack] = unlock

################################################################################
    def _load_sprites(self) -> None:

        raise NotImplementedError

################################################################################
    def __eq__(self, other: DMObject) -> bool:

        return self._uuid == other._uuid

################################################################################
    @property
    def type(self) -> DMType:

        raise NotImplementedError

################################################################################
    @property
    def game(self) -> DMGame:

        return self._state

################################################################################
    def listen(self, event: str) -> None:
        """Automatically listens to the provided event with `self.notify`."""

        self.game.subscribe_event(event, self.notify)

################################################################################
    def notify(self, *args) -> None:

        pass

################################################################################
    def _copy(self, **kwargs) -> DMObject:
        """Returns a clean copy of the current room type with any given
        kwargs substituted in. The UUID **is** regenerated.

        Returns:
        --------
        :class:`DMObject`
            A fresh copy of the current DMObject.
        """

        cls: Type[DMObj] = type(self)
        new_obj = cls.__new__(cls)

        new_obj._uuid = uuid4()
        new_obj._state = self._state

        new_obj._id = self._id
        new_obj.name = self.name
        new_obj.description = self.description

        new_obj.rank = self.rank
        new_obj.unlock = self.unlock

        return new_obj

################################################################################
