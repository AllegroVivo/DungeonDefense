from __future__ import annotations

from abc        import abstractmethod
from pygame     import Rect, Surface, Vector2
from typing     import (
    TYPE_CHECKING,
    Any,
    Dict,
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
    from dm.core.objects.unit import DMUnit
    from .hero import DMHero
    from .monster import DMMonster
################################################################################

__all__ = ("DMRoom",)

R = TypeVar("R", bound="DMRoom")

################################################################################
class DMRoom(DMLevelable, DMChargeable):

    __slots__ = (
        "_position",
        "_graphics",
        "_damage_range",
        "_effects",
    )

################################################################################
    def __init__(
        self,
        state: DMGame,
        position: Optional[Vector2],
        effects: Optional[List[Effect]],
        base_dmg: Optional[int],
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

        self._damage_range: Optional[int] = base_dmg
        self._effects: List[Effect] = effects or []

        # Subscribe to relevant events.
        self.listen("room_enter", self._room_entered)
        self.listen("on_attack", self._on_attack)
        self.listen("stat_refresh", self.stat_adjust)

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
    def room_type(self) -> RoomType:

        raise RoomType.Empty

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
    @property
    def dmg(self) -> Optional[int]:
        """Don't change this name, it's called `dmg` so it doesn't conflict with
        DMUnit's `damage` method. (They conflict in the AttackContext class.)"""

        if self._damage_range is None:
            return

        return self.random.scaling_damage(self)

################################################################################
    @property
    def effects(self) -> Optional[Dict[str, int]]:
        """Returns a dictionary of this room's outgoing status effects and
        their stack values."""

        if not self._effects:
            return

        return {e.name: e.base + (e.per_lv * self.level) for e in self._effects}

################################################################################
    def _room_entered(self, unit: DMUnit) -> None:
        """Called when the "room_enter" event is fired and fires this object's
        `on_enter()` method if the room entered was this one."""

        if unit.room == self:
            self.on_enter(unit)

################################################################################
    def _on_attack(self, ctx: AttackContext) -> None:
        """Called when the "on_attack" event is fired and fires this object's
        `on_attack()` method if this is the room where the attack took place."""

        if ctx.room == self:
            self.on_attack(ctx)

################################################################################
    def on_enter(self, unit: DMUnit) -> None:
        """Called when a unit enters this room specifically. Intended to be
        overridden by subclasses.

        Parameters:
        -----------
        unit: :class:`DMUnit`
           The unit that entered this room.
        """

        pass

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:
        """Called when an attack is made in this room specifically. Intended to be
        overridden by subclasses.

        Parameters:
        -----------
        ctx: :class:`AttackContext`
            The context of the attack.
        """

        pass

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

        new_obj._damage_range = self._damage_range
        new_obj._statuses = self._effects

        return new_obj

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
    def units_of_type(self, unit: DMUnit, inverse: bool = False) -> List[DMUnit]:
        """Returns the room's heroes or monsters depending on the type of unit
        provided.

        Parameters:
        -----------
        unit: :class:`DMUnit`
            The unit whose type is to be returned.

        Returns:
        --------
        List[:class:`DMUnit`]
            The list of units of the same type as the given unit.
        """

        if unit.is_hero():
            return self.heroes if not inverse else self.monsters
        elif unit.is_monster():
            return self.monsters if not inverse else self.heroes
        else:
            return []

################################################################################
