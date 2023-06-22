from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING

from .context       import Context
from ..objects.room import DMRoom
from utilities  import *

if TYPE_CHECKING:
    from dm.core    import DMUnit, DMGame
################################################################################

__all__ = ("RoomChangeContext",)

################################################################################
class RoomChangeContext(Context):

    __slots__ = (
        "_previous",
        "_target",
        "unit"
    )

################################################################################
    def __init__(self, state: DMGame, previous: DMRoom, target: DMRoom, unit: DMUnit):

        super().__init__(state)

        self._previous: DMRoom = previous
        self._target: DMRoom = target
        self.unit: DMUnit = unit

################################################################################
    def execute(self) -> None:

        pass

################################################################################
    @property
    def previous(self) -> DMRoom:

        return self._previous

################################################################################
    @property
    def room(self) -> DMRoom:

        return self._target

################################################################################
