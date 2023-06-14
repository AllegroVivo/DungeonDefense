from __future__ import annotations

import random

from pygame     import Surface, Vector2
from typing     import TYPE_CHECKING, Optional, Type, TypeVar

from .fighter   import DMFighter
from ..graphics import HeroGraphical
from utilities  import *

if TYPE_CHECKING:
    from dm.core    import DMGame, DMRoom
################################################################################

__all__ = ("DMHero",)

H = TypeVar("H", bound="DMHero")

################################################################################
class DMHero(DMFighter):

    __slots__ = (
        "_screen_pos",
        "_target_pos",
        "_moving",
        # "_move_elapsed",
        "_direction",
        "_engaged",
        "counter",
        "_target_room"
    )

################################################################################
    def __init__(
        self,
        state: DMGame,
        room: Optional[DMRoom],
        *,
        _id: str,
        name: str,
        rank: int,
        description: Optional[str] = None,
        unlock: Optional[UnlockPack] = None,
        num_frames: int = 5,
    ):

        try:  # Will fail on initial load since the dungeon isn't loaded before the objspawner.
            room = room or self.game.dungeon.entrance
            start = room.position
            self._screen_pos: Vector2 = room.graphics.center()
        except AttributeError:
            start = None
            self._screen_pos: Vector2 = Vector2(0, 0)

        super().__init__(
            state, _id, name, description, 1, 1, 1.0, 1.0, level=1, rank=rank,
            unlock=unlock, graphics=HeroGraphical(self, num_frames),
            start_cell=start
        )

        self._target_pos: Optional[Vector2] = None

        self._moving: bool = True
        # self._move_elapsed: float = 0.0
        self._direction: Optional[Vector2] = Vector2(-1, 0)
        self._engaged: bool = False
        self.counter = 0

################################################################################
    def move(self, dt: float) -> None:

        # self._move_elapsed += dt
        self._screen_pos += self._direction * HERO_SPEED * dt
        # if self.counter % 10 == 0:
        #     print(f"screen pos: {self._screen_pos}")
        #     print(f"target pos: {self.target_position}")
        if self.arrived_at_target():
            self.stop_movement()
            self.arrived_in_cell()

################################################################################
    def update(self, dt: float) -> None:

        self.counter += 1
        self.move(dt)

        if not self._moving:
            if self.counter % 70 == 0:
                self.start_movement()
                self.counter = 0
        self.graphics.update(dt)

################################################################################
    def draw(self, screen: Surface) -> None:
        """Draws the hero on the screen."""

        self.graphics.draw(screen)

################################################################################
    @property
    def target_room(self) -> Optional[DMRoom]:

        if self._direction is None:
            return

        print(f"cur pos: {self.room.position}")
        print(f"cur dir: {self._direction}")
        x = self.room.position.x + self._direction.y
        y = self.room.position.y + self._direction.x

        room = self.game.get_room_at(Vector2(x, y))

        print(f"target grid: {room.position}")
        print(f"target pos: {room.center}")
        if room is None or room.__class__.__name__ == "EntranceRoom":
            self._direction = None
            return

        return room

################################################################################
    @property
    def direction(self) -> Optional[Vector2]:

        return self._direction

################################################################################
    @property
    def room(self) -> DMRoom:

        return self.game.get_room_at(pixel_to_grid(self._screen_pos))

################################################################################
    @property
    def screen_position(self) -> Vector2:

        return self._screen_pos

################################################################################
    @property
    def target_position(self) -> Optional[Vector2]:

        if self._direction is None:
            return

        # if self._target_pos is not None:
        #     return self._target_pos

        self._target_pos = self.target_room.center

        return self._target_pos

################################################################################
    @target_position.setter
    def target_position(self, value: Vector2) -> None:

        if not isinstance(value, Vector2):
            raise ArgumentTypeError("DMHero.target_position", type(value), type(Vector2))

        self._target_pos = value

################################################################################
    @property
    def is_moving(self) -> bool:

        return self._moving

################################################################################
    def arrived_at_target(self) -> bool:

        return (self.screen_position - self.target_position).length() < 2

################################################################################
    def start_movement(self) -> None:

        if self._direction is None:
            while self.target_room is None:
                # Pick a direction if not set.
                self._direction = Vector2(random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)]))
            self.target_position = self.target_room.center
        # Start movement.
        self._moving = True

################################################################################
    def stop_movement(self) -> None:

        self._moving = False
        self._direction = None

################################################################################
    def engage(self, unit: DMFighter) -> None:

        self.stop_movement()
        super().engage(unit)

################################################################################
    def arrived_in_cell(self) -> None:

        self._engaged = self.room.try_engage_monster(self)

        # Publish event
        # self.game.dispatch_event("on_room_change")

################################################################################
    def _copy(self, **kwargs) -> DMHero:
        """Returns a clean copy of the current hero type with any given
        kwargs substituted in.

        All parameters are optional.

        Parameters:
        -----------
        position: :class:`DMVector`
            The hero's starting position if not the dungeon entrance.

        Returns:
        --------
        :class:`DMHero`
            A fresh copy of the current DMHero with values substituted as defined.
        """

        new_obj: Type[H] = super()._copy(**kwargs)  # type: ignore

        new_obj._screen_position = self.game.dungeon.entrance.center
        new_obj._moving = True
        new_obj._move_elapsed = 0.0
        new_obj._direction = Vector2(-1, 0)
        new_obj._engaged = False

        return new_obj

################################################################################
