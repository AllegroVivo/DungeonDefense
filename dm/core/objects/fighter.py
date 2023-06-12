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

from dm.core.graphics._graphical import GraphicalComponent
from dm.core.objects.levelable import DMLevelable
from dm.core.battle.stats import BaseStats
from dm.core.objects.status import DMStatus
from utilities      import *

if TYPE_CHECKING:
    from dm.core    import DMGame, DMRoom
################################################################################

__all__ = ("DMFighter",)

F = TypeVar("F", bound="DMFighter")

################################################################################
class DMFighter(DMLevelable):

    __slots__ = (
        "stats",
        "skills",
        "equipment",
        "graphics",
        "statuses",
        "_room",
        "position",
        "action_delay",
        "_move_penalty"
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
        unlock: Optional[UnlockPack] = None
    ):

        super().__init__(state, _id, name, description, level, rank, unlock=unlock)

        self.stats = BaseStats(life, attack, defense, dex)

        self._room: Optional[Vector2] = None
        self.position: Optional[Vector2] = None

        self.skills: List = skills or []
        self.equipment = None

        self.statuses: List[DMStatus] = []
        self.action_delay: float = 1.0
        self._move_penalty: float = 0.0  # this needs to be factored in as a flat amount of seconds that the unit is immobilized for.

        self.graphics: GraphicalComponent = graphics

################################################################################
    def __iadd__(self, other: DMStatus) -> DMFighter:

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
        for s in self.statuses:
            if type(s) == type(status):
                s += status
                status = s
                found = True

        # Append the status if it wasn't already there.
        if not found:
            self.statuses.append(status)

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

        self.graphics.update(dt)

################################################################################
    def _copy(self, **kwargs) -> DMFighter:
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

        position: :class:`DMVector`
            The new position of the fighter. `None` if not passed.

        Returns:
        --------
        :class:`DMFighter`
            A fresh copy of the current DMObject with values substituted as defined.

        """

        new_obj: Type[F] = super()._copy()  # type: ignore

        new_obj.stats = self.stats._copy()

        new_obj.level = kwargs.pop("level", self.level)
        new_obj.experience = kwargs.pop("experience", None) or kwargs.pop("exp", 0)
        new_obj.upgrades = kwargs.pop("upgrades", 0)

        new_obj.skills = kwargs.pop("skills", self.skills.copy())
        new_obj.equipment = kwargs.pop("equipment", None)

        new_obj.graphics = self.graphics._copy()

        new_obj.position = kwargs.pop("position", None)
        new_obj.statuses = kwargs.pop("statuses", None) or []
        new_obj.action_delay = 1.0

        return new_obj

################################################################################
    def get_status(self, name: str) -> Optional[DMStatus]:

        for status in self.statuses:
            if status.name == name:
                return status

################################################################################
    def heal(self, amount: Union[int, float]) -> None:

        self.stats.damage(-int(amount))

################################################################################
    def damage(self, amount: Union[int, float]) -> None:

        self.stats.damage(int(amount))

################################################################################
    def immobilize(self, time: float) -> None:

        self._move_penalty += time

################################################################################
