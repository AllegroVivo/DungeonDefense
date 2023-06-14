from __future__ import annotations

from pygame     import Surface, Vector2
from typing     import (
    TYPE_CHECKING,
    List,
    Optional,
    Type,
    TypeVar,
    Union
)

from dm.core.game.movement import MovementComponent
from dm.core.graphics._graphical import GraphicalComponent
from dm.core.objects.levelable import DMLevelable
from dm.core.battle.stats import BaseStats
from dm.core.objects.status import DMStatus
from utilities              import *

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.room import DMRoom
################################################################################

__all__ = ("DMUnit",)

U = TypeVar("U", bound="DMUnit")

################################################################################
class DMUnit(DMLevelable):

    __slots__ = (
        "stats",
        "_skills",
        "_equip",
        "_graphics",
        "_statuses",
        "_room",
        "_action_timer",
        "_move_penalty",
        "_engaged",
        "_screen_pos",
        "_mover"
    )

################################################################################
    def __init__(
        self,
        state: DMGame,
        _id: str,
        name: str,
        description: Optional[str],
        life: int,
        attack: int,
        defense: float,
        dex: float,
        level: int,
        graphics: GraphicalComponent,
        skills: Optional[List] = None,
        rank: int = 0,
        unlock: Optional[UnlockPack] = None,
        start_cell: Optional[Vector2] = None
    ):

        super().__init__(state, _id, name, description, level, rank, unlock=unlock)

        self.stats = BaseStats(life, attack, defense, dex)

        self._room: Optional[Vector2] = start_cell

        self._skills: List = skills or []
        self._equip = None

        self._statuses: List[DMStatus] = []
        self._action_timer: float = 1.0
        self._move_penalty: float = 0.0  # this needs to be factored in as a flat amount of seconds that the unit is immobilized for.

        self._graphics: GraphicalComponent = graphics
        self._screen_pos: Optional[Vector2] = None
        self._mover: MovementComponent = MovementComponent(self)

        self._engaged: bool = False

################################################################################
    def __iadd__(self, other: DMStatus) -> DMUnit:

        if isinstance(other, DMStatus):
            self._add_status(other)
        else:
            raise ValueError("Unexpected type passed to DMFighter.__iadd__().")

        return self

################################################################################
    @property
    def room(self) -> DMRoom:

        return self.game.get_room_at(self._room)

################################################################################
    @room.setter
    def room(self, value: Union[Vector2, DMRoom]) -> None:

        if isinstance(value, Vector2):
            self._room = value
        elif isinstance(value, DMRoom):
            self._room = value.position
        else:
            raise ArgumentTypeError(
                "DMFighter.room.setter",
                type(value),
                type(Vector2), type(DMRoom)
            )

################################################################################
    @property
    def screen_pos(self) -> Vector2:

        return self._screen_pos

################################################################################
    @property
    def action_timer(self) -> float:

        return self._action_timer

################################################################################
    def reset_action_timer(self) -> None:

        self._action_timer = 0.0

################################################################################
    @property
    def graphics(self) -> GraphicalComponent:

        return self._graphics

################################################################################
    def _add_status(self, status: DMStatus) -> None:

        # Only apply Curse for buffs.
        if status.type == DMStatusType.Buff:
            # Before adding a status, check for Curse and resist
            curse = self.get_status("Curse")
            if curse is not None:
                resist = self.get_status("Curse Resist")
                if resist is not None:
                    # If curse stacks exceed resist stacks
                    if resist < curse:
                        curse -= 1  # Remove a stack due to activation
                        status = self.game.spawn(
                            _n="Curse Resist")  # Just swap the buff for Curse Resist so the flow can continue.

        found = False
        for s in self._statuses:
            if type(s) == type(status):
                s += status
                status = s
                found = True

        # Append the status if it wasn't already there.
        if not found:
            self._statuses.append(status)

################################################################################
    @property
    def is_alive(self) -> bool:

        return self.life > 0

################################################################################
    @property
    def game(self) -> DMGame:

        return self._state

################################################################################
    @property
    def life(self) -> int:

        return self.stats.life

################################################################################
    @property
    def max_life(self) -> int:

        return int(self.stats._life.calculate())

################################################################################
    @property
    def attack(self) -> int:

        return self.stats.attack

################################################################################
    @property
    def defense(self) -> float:

        return self.stats.defense

################################################################################
    @property
    def dex(self) -> float:

        return self.stats.dex

################################################################################
    @property
    def combat_ability(self) -> float:

        return self.stats.combat_ability

################################################################################
    @property
    def num_attacks(self) -> int:

        return self.stats.num_attacks

################################################################################
    @property
    def speed(self) -> float:

        return self.stats.speed

################################################################################
    @property
    def stat_score(self) -> float:

        return (self.life + self.attack + self.defense) * self.level + self.experience

################################################################################
    @property
    def engaged(self) -> bool:

        return self._engaged

################################################################################
    def engage(self, unit: DMUnit) -> None:

        self._engaged = True
        print("Engaging Monster")
        self.game.battle_mgr.engage(unit, self)

################################################################################
    def disengage(self) -> None:

        self._engaged = False

################################################################################
    def increase_stat_flat(self, stat: str, amount: int) -> None:

        if not isinstance(amount, int):
            raise ArgumentTypeError(
                "Invalid type passed to DMFighter.increase_stat_flat().",
                type(amount),
                type(int)
            )

        self.stats.mutate_stat(stat, amount)

################################################################################
    def increase_stat_pct(self, stat: str, amount: float) -> None:

        if not isinstance(amount, int):
            raise ArgumentTypeError(
                "Invalid type passed to DMFighter.increase_stat_pct().",
                type(amount),
                type(float)
            )

        self.stats.mutate_stat(stat, amount)

################################################################################
    def reduce_stat_flat(self, stat: str, amount: int) -> None:

        if not isinstance(amount, int):
            raise ArgumentTypeError(
                "Invalid type passed to DMFighter.decrease_stat_flat().",
                type(amount),
                type(int)
            )

        self.stats.mutate_stat(stat, -amount)

################################################################################
    def reduce_stat_pct(self, stat: str, amount: float) -> None:

        if not isinstance(amount, int):
            raise ArgumentTypeError(
                "Invalid type passed to DMFighter.decrease_stat_pct().",
                type(amount),
                type(float)
            )

        self.stats.mutate_stat(stat, -amount)

################################################################################
    def draw(self, screen: Surface) -> None:

        self.graphics.draw(screen)

################################################################################
    def update(self, dt: float) -> None:

        self._action_timer -= dt
        if self._mover is not None:
            self._mover.update(dt)
        self.graphics.update(dt)

################################################################################
    def entered_room(self) -> None:

        engaged = self.room.try_engage_monster(self)
        if not engaged:
            self._mover.start_movement()

################################################################################
    def _copy(self, **kwargs) -> DMUnit:
        """Returns a clean copy of the current fighter class type with any given
        kwargs substituted in.

        All parameters are optional.

        Parameters:
        -----------
        level: :class:`int`
            The object's level

        experience: :class:`int`
            The initial amount of experience to give the object.

        skills: List[:class:`DMSkill`]
            The list of initial skills to give the fighter.

        equipment: :class:`DMEquipment`
            The starting piece of equipment to give the fighter.

        upgrades: :class:`int`
            How many upgrade levels to start the fighter at.

        opponent: :class:`DMFighter`
            The newly created fighter's initial opponent.

        statuses: List[:class:`DMStatus`]
            An initial list of status conditions afflicting the fighter.

        Returns:
        --------
        :class:`DMFighter`
            A fresh copy of the current DMObject with values substituted as defined.

        """

        new_obj: Type[U] = super()._copy()  # type: ignore

        new_obj.stats = self.stats._copy()

        new_obj._level = kwargs.pop("level", 1)
        new_obj._exp = kwargs.pop("experience", None) or kwargs.pop("exp", 0)
        new_obj._upgrades = kwargs.pop("upgrades", 0)

        new_obj._skills = kwargs.pop("skills", self._skills.copy())
        new_obj._equip = kwargs.pop("equipment", None)

        new_obj._room = kwargs.pop("room", None)
        new_obj._graphics = self._graphics._copy()
        new_obj._mover = self._mover._copy(new_obj)

        new_obj._statuses = kwargs.pop("statuses", None) or []
        new_obj._action_timer = 1.0
        new_obj._move_penalty = 0.0

        new_obj._engaged = False

        return new_obj

################################################################################
    def get_status(self, name: str) -> Optional[DMStatus]:

        for status in self._statuses:
            if status.name == name:
                return status

################################################################################
    def heal(self, amount: Union[int, float]) -> None:

        self.stats.damage(-int(amount))

################################################################################
    def damage(self, amount: Union[int, float]) -> None:

        self.stats.damage(int(amount))

################################################################################
    def immobilize(self, duration: float) -> None:
        """Adds `duration` amount of time to the unit's move_penalty. Duration is
        a float representing the total duration of a second. (1.0 = 100%)
        """

        self._move_penalty += duration

################################################################################
