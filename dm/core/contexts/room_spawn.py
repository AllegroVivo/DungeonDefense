from __future__ import annotations

from typing     import TYPE_CHECKING

from .context  import Context
from ..objects.room     import DMRoom
from utilities  import *

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("RoomSpawnContext",)

################################################################################
class RoomSpawnContext(Context):

    __slots__ = (
        "_result",
    )

################################################################################
    def __init__(self, state: DMGame, room: DMRoom):

        super().__init__(state)

        self._result: DMRoom = room

################################################################################
    @property
    def result(self) -> DMRoom:

        return self._result

################################################################################
    def set_result(self, result: DMRoom) -> None:

        if not isinstance(result, DMRoom):
            raise ArgumentTypeError("RoomSpawnCTX.set_result()", type(result), type(DMRoom))

        self._result = result

################################################################################
    def execute(self) -> None:

        pass  # for now?

################################################################################
