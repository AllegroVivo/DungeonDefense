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
        "_current",
        "_target",
        "unit"
    )

################################################################################
    def __init__(self, state: DMGame, current: DMRoom, target: DMRoom, unit: DMUnit):

        super().__init__(state)

        self._current: DMRoom = current
        self._target: DMRoom = target
        self.unit: DMUnit = unit

################################################################################
    def execute(self) -> None:

        self._target.add_hero(self.unit)  # type: ignore

        if self.current_position.x < self.target_position.x:  # Left
            self.unit.position.x = self._target.get_rect().right + GRID_PADDING
        elif self.current_position.x > self.target_position.x:  # Right
            self.unit.position.x = self._target.get_rect().left - GRID_PADDING
        elif self.current_position.y < self.target_position.y:  # Up
            self.unit.position.y = self._target.get_rect().bottom + GRID_PADDING
        elif self.current_position.y < self.target_position.y:  # Down
            self.unit.position.y = self._target.get_rect().top - GRID_PADDING

        self._current.remove_hero(self.unit)  # type: ignore

################################################################################
    @property
    def current_room(self) -> DMRoom:

        return self._current

################################################################################
    @property
    def current_position(self) -> Vector2:

        return self._current.position

################################################################################
    @property
    def target_room(self) -> DMRoom:

        return self._target

################################################################################
    @property
    def target_position(self) -> Vector2:

        return self._target.position

################################################################################
