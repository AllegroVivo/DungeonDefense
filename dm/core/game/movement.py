from __future__ import annotations

import random

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional, TypeVar

from utilities  import *

if TYPE_CHECKING:
    from dm.core    import DMGame, DMRoom, DMUnit
################################################################################

__all__ = ("MovementComponent",)

MC = TypeVar("MC", bound="MovementComponent")

################################################################################
class MovementComponent:

    __slots__ = (
        "_parent",
        "_moving",
        "_direction",
        "counter",
        "_target_room",
        "_start_pos"
    )

################################################################################
    def __init__(self, parent: DMUnit):

        self._parent: DMUnit = parent

        self._moving: bool = True
        self._direction: Optional[Vector2] = Vector2(-1, 0)
        self._target_room: Optional[DMRoom] = None
        self.counter = 0
        self._start_pos = None

################################################################################
    @property
    def game(self) -> DMGame:

        return self._parent.game

################################################################################
    def update(self, dt: float) -> None:

        self.counter += 1

        if self._moving:
            self.move(dt)
        else:
            if self.counter % 100 == 0:
                self.start_movement()

################################################################################
    def move(self, dt: float) -> None:

        if self._direction is None:
            return

        if self._direction.x != 0:
            self._parent._screen_pos.x += self._direction.x * HERO_SPEED * dt
        elif self._direction.y != 0:
            self._parent._screen_pos.y += self._direction.y * HERO_SPEED * dt

        if self.arrived_at_target():
            self.cancel_movement()
            self.arrived_in_cell()

################################################################################
    def arrived_at_target(self) -> bool:

        return (self.screen_position - self.target_room.center).length() < EPSILON

################################################################################
    @property
    def target_room(self) -> Optional[DMRoom]:

        if self._direction is None:
            return

        if self._target_room is not None:
            return self._target_room

        self.calculate_target_room()

        return self._target_room

################################################################################
    def calculate_target_room(self) -> None:

        room = None
        while room is None:
            room = self.game.get_room_at(self.room.position + self._direction, debug=True)
            if room is None or room.name == "Entrance" or room.__class__.__name__ == "BossRoom" or room.center.y < 0:
                room = None
                self.choose_direction()

        self._target_room = room

################################################################################
    @property
    def direction(self) -> Optional[Vector2]:

        return self._direction

################################################################################
    @property
    def room(self) -> DMRoom:

        return self.game.get_room_at(pixel_to_grid(self._parent._screen_pos))

################################################################################
    @property
    def screen_position(self) -> Vector2:

        return self._parent._screen_pos

################################################################################
    @property
    def target_position(self) -> Optional[Vector2]:

        if self.target_room is None:
            return

        return self.target_room.center

################################################################################
    @property
    def is_moving(self) -> bool:

        return self._moving

################################################################################
    def choose_direction(self) -> None:

        self._direction = Vector2(random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)]))

################################################################################
    def start_movement(self) -> None:

        # Pick a direction
        self.choose_direction()

        # Start movement.
        self._moving = True

################################################################################
    def cancel_movement(self) -> None:

        self._moving = False
        self._direction = None
        self._target_room = None

################################################################################
    def arrived_in_cell(self) -> None:

        self._start_pos = self.room.center
        print("Arrived!")

################################################################################
    def _copy(self, parent: DMUnit) -> MovementComponent:
        """Returns a clean copy of the current unit's movement component.

        Parameters:
        -----------
        parent: :class:`DMUnit`
            The object for the fresh instance to be attached to.

        Returns:
        --------
        :class:`DMHero`
            A fresh copy of the current DMHero with values substituted as defined.
        """

        cls = type(self)
        new_obj = cls.__new__(cls)

        new_obj._parent = parent

        new_obj._moving = True
        new_obj._direction = Vector2(-1, 0)
        new_obj._target_room = None
        new_obj._start_pos = None

        new_obj.counter = 0

        return new_obj

################################################################################
