from __future__ import annotations

import random

from pygame     import Surface, Vector2
from typing     import TYPE_CHECKING, Optional, Type, TypeVar

from dm.core.objects.unit import DMUnit
from ..graphics import HeroGraphical
from utilities  import *

if TYPE_CHECKING:
    from dm.core    import DMGame, DMRoom
################################################################################

__all__ = ("DMHero",)

H = TypeVar("H", bound="DMHero")

################################################################################
class DMHero(DMUnit):

    __slots__ = (
        "_target_pos",
        "_moving",
        "_direction",
        "_engaged",
        "counter",
        "_target_room"
    )

################################################################################
    def __init__(
        self,
        state: DMGame,
        room: Optional[DMRoom] = None,
        *,
        _id: str,
        name: str,
        rank: int,
        description: Optional[str] = None,
        unlock: Optional[UnlockPack] = None,
        num_frames: int = 5,
    ):

        super().__init__(
            state, _id, name, description, 1, 1, 1.0, 1.0, level=1, rank=rank,
            unlock=unlock, graphics=HeroGraphical(self, num_frames),
            start_cell=room.position if room is not None else None
        )

        self._screen_pos = (
            self.game.get_room_at(self._room).center
            if self._room is not None else None
        )
        self._moving: bool = True
        self._direction: Optional[Vector2] = Vector2(-1, 0)
        self._target_room: Optional[DMRoom] = None
        self._engaged: bool = False
        self.counter = 0

################################################################################
    def update(self, dt: float) -> None:

        super().update(dt)
        self.graphics.update(dt)

################################################################################
    def draw(self, screen: Surface) -> None:
        """Draws the hero on the screen."""

        self.graphics.draw(screen)

################################################################################
    def engage(self, unit: DMUnit) -> None:

        super().engage(unit)

################################################################################
    def arrived_in_cell(self) -> None:

        self._mover.cancel_movement()
        print(self._room)
        self._engaged = self.room.try_engage_monster(self)
        if self._engaged:
            print("Monster engaged!")

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
        new_obj._target_room = None
        new_obj._engaged = False

        return new_obj

################################################################################
