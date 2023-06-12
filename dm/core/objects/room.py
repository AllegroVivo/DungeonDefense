from __future__ import annotations

from abc        import abstractmethod
from pygame     import Rect, Surface, Vector2
from typing     import TYPE_CHECKING, List, Optional, Tuple, Type, TypeVar

from utilities  import *

from dm.core.graphics import RoomGraphical
from dm.core.objects.levelable import DMLevelable

if TYPE_CHECKING:
    from dm.core    import DMGame, DMHero, DMMonster
################################################################################

__all__ = ("DMRoom",)

R = TypeVar("R", bound="DMRoom")

################################################################################
class DMRoom(DMLevelable):

    __slots__ = (
        "position",
        "_heroes",
        "graphics",
    )

################################################################################
    def __init__(
        self,
        state: DMGame,
        row: int,
        col: int,
        _id: str,
        name: str,
        description: str,
        rank: int,
        level: int,
        unlock: Optional[UnlockPack]
    ):

        super().__init__(state, _id, name, description, level, rank, unlock=unlock)

        self.position: Vector2 = Vector2(row, col)
        self.graphics: RoomGraphical = RoomGraphical(self)

        self._heroes: List[DMHero] = []

################################################################################
    @property
    @abstractmethod
    def room_type(self) -> DMRoomType:

        raise DMRoomType.Empty

################################################################################
    @property
    def heroes(self) -> List[DMHero]:

        return self._heroes

################################################################################
    def add_hero(self, hero: DMHero) -> None:

        self._heroes.append(hero)

################################################################################
    def remove_hero(self, hero: DMHero) -> DMHero:

        for i, h in enumerate(self._heroes):
            if h == hero:
                return self._heroes.pop(i)

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

        # Heroes can't be in a new room yet.
        # new_obj.heroes = []

        new_obj.level = kwargs.pop("level", self.level)
        new_obj.experience = kwargs.pop("experience", None) or kwargs.pop("exp", 0)

        new_obj.graphics = self.graphics._copy()
        # new_obj.highlighted = False

        # Dummy coordinates until it's placed.
        new_obj.position = Vector2(kwargs.pop("row", -1), kwargs.pop("col", -1))

        return new_obj

################################################################################
    @property
    def color(self) -> Tuple[int, int, int]:

        class_name = type(self).__name__

        if class_name == "EntranceRoom":
            return GREEN
        if class_name == "BossRoom":
            return RED
        if class_name == "Battle":
            return BLUE

        return ROOM_BG

################################################################################
    def draw(self, screen: Surface) -> None:
        """Draws the room and any monsters therein."""

        self.graphics.draw(screen)

################################################################################
    def update(self, dt: float) -> None:

        if self.room_type is DMRoomType.Battle:
            for monster in self.monsters:  # type: ignore
                monster.update(dt)

################################################################################
    @property
    def highlighted(self) -> bool:

        return self.graphics._highlighted

################################################################################
    def toggle_highlighting(self, value: bool) -> None:

        self.graphics.toggle_highlighting(value)

################################################################################
    def get_rect(self) -> Rect:

        return self.graphics.calculate_rect()

################################################################################
    def on_acquire(self) -> None:

        # self.game.subscribe_event("", self.notify)
        raise NotImplementedError

################################################################################
    def notify(self, **kwargs) -> None:

        raise NotImplementedError

################################################################################
    def effect_value(self) -> int:

        return -1

################################################################################
