from __future__ import annotations

from abc        import abstractmethod
from pygame     import Rect, Surface, Vector2
from typing     import (
    TYPE_CHECKING,
    Any,
    List,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union
)

from utilities  import *

from .chargeable import DMChargeable
from ..graphics import RoomGraphical
from .levelable import DMLevelable

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.game.game import DMGame
    from dm.core.objects.hero import DMHero
    from dm.core.objects.monster import DMMonster
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("DMRoom",)

R = TypeVar("R", bound="DMRoom")

################################################################################
class DMRoom(DMLevelable, DMChargeable):

    __slots__ = (
        "_position",
        "_graphics",
    )

################################################################################
    def __init__(
        self,
        state: DMGame,
        position: Optional[Vector2],
        _id: str,
        name: str,
        description: str,
        rank: int,
        level: int,
        unlock: Optional[UnlockPack]
    ):

        super().__init__(state, _id, name, description, level, rank, unlock=unlock)
        DMChargeable.__init__(self)

        self._position: Vector2 = position or Vector2(-1, -1)
        self._graphics: RoomGraphical = RoomGraphical(self)

################################################################################
    def __repr__(self) -> str:

        return (
            f"<DMRoom: cls={self.__class__.__name__}, "
            f"grid pos: {self._position}, "
            f"center: {self.center}, "
            f"type: {self.room_type}>"
        )

################################################################################
    @property
    def type(self) -> DMType:

        return DMType.Room

################################################################################
    @property
    def graphics(self) -> RoomGraphical:

        return self._graphics

################################################################################
    @property
    @abstractmethod
    def room_type(self) -> DMRoomType:

        raise DMRoomType.Empty

################################################################################
    @property
    def position(self) -> Vector2:

        return self._position

################################################################################
    @property
    def x(self) -> int:

        return self._position.x

################################################################################
    @property
    def y(self) -> int:

        return self._position.y

################################################################################
    @property
    def rect(self) -> Rect:

        return self.graphics.calculate_rect()

################################################################################
    @property
    def heroes(self) -> List[DMHero]:

        return [h for h in self.game.dungeon.heroes if h.room == self]

################################################################################
    @property
    def monsters(self) -> List[DMMonster]:

        return [m for m in self.game.inventory.deployed_monsters if m.room == self]

################################################################################
    @property
    def center(self) -> Vector2:

        return self.graphics.center()

################################################################################
    def _copy(self, **kwargs) -> DMRoom:
        """Returns a clean copy of the current room type with any given
        kwargs substituted in.

        All parameters are optional.

        Parameters:
        -----------
        level: :class:`int`
            The object's level

        experience: :class:`int`
            The initial amount of experience to give the object.

        position: Union[:class:`DMVector`, Tuple[:class:`int`, :class:`int`]]
            The room's initial position in the dng_options grid.

        Returns:
        --------
        :class:`DMRoom`
            A fresh copy of the current DMObject with values substituted as defined.

        """

        new_obj: Type[R] = super()._copy()  # type: ignore

        new_obj.level = kwargs.pop("level", self.level)
        new_obj.experience = kwargs.pop("experience", None) or kwargs.pop("exp", 0)

        new_obj.graphics = self.graphics._copy()
        # new_obj.highlighted = False
        new_obj._monsters = []

        # Dummy coordinates until it's placed.
        new_obj.position = kwargs.pop("position", None) or Vector2(-1, -1)

        return new_obj

# ################################################################################
#     @property
#     def color(self) -> Tuple[int, int, int]:
#
#         class_name = type(self).__name__
#
#         if class_name == "EntranceRoom":
#             return GREEN
#         if class_name == "BossRoom":
#             return RED
#         if class_name == "Battle":
#             return BLUE
#
#         return ROOM_BG

################################################################################
    def draw(self, screen: Surface) -> None:
        """Draws the room and any monsters therein."""

        self.graphics.draw(screen)

################################################################################
    def update(self, dt: float) -> None:

        DMChargeable.update(self, dt)

################################################################################
    @property
    def highlighted(self) -> bool:

        return self.graphics._highlighted

################################################################################
    def toggle_highlighting(self, value: bool) -> None:

        self.graphics.toggle_highlighting(value)

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when this room is added to the map."""

        pass

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        pass

################################################################################
    def notify(self, *args) -> None:
        """A general event response function."""

        pass

################################################################################
    def effect_value(self) -> Any:
        """The value(s) of this room's effect.

        A random value from the base effectiveness range is chosen, then a random
        value from the additional effectiveness range is added to the total for
        each level of this room.

        Breakdown:
        ----------
        **effect = (a to b) + ((x to y) * LV)**

        In this function:

        - (a to b) is the base effectiveness will be chosen.
        - (x to y) is the additional effectiveness per level.
        - LV is the level of this room.
        """

        pass

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        pass

################################################################################
    def get_adjacent_room(self, direction: Union[str, Vector2]) -> Optional[DMRoom]:

        if direction not in (
            "up", "down", "left", "right", "north", "south", "east", "west"
        ):
            raise ValueError(
                f"Invalid direction {direction} provided to DMRoom.get_adjacent_room()."
            )

        return self.game.dungeon.get_adjacent_rooms(
            pos=self.position,
            all_rooms=False,
            show_west=direction in ("west", "left"),
            show_east=direction in ("east", "right"),
            show_north=direction in ("north", "up"),
            show_south=direction in ("south", "down"),
        )[0]

################################################################################
    def try_engage_monster(self, unit: DMUnit) -> bool:

        return False

################################################################################
    def remove(self) -> None:

        empty = self.game.spawn(obj_id="ROOM-000", init_obj=True, position=self.position)
        self.game.dungeon.replace_room(self, empty)  # type: ignore

################################################################################
    @property
    def adjacent_rooms(self) -> List[DMRoom]:

        return self.game.dungeon.get_adjacent_rooms(self.position)

################################################################################
