from __future__ import annotations

from typing     import TYPE_CHECKING, Type, TypeVar, Union

from .object    import DMObject
from utilities  import *

if TYPE_CHECKING:
    from .unit import DMUnit
    from ..game.game import DMGame
    from ..contexts.attack import AttackContext
################################################################################

__all__ = ("DMStatus",)

S = TypeVar("S", bound="DMStatus")

################################################################################
class DMStatus(DMObject):

    __slots__ = (
        "_parent",
        "_stacks",
        "_type",
        "_flat_adjustment",
        "_scalar"
    )

################################################################################
    def __init__(
        self,
        state: DMGame,
        parent: DMUnit,
        *,
        _id: str,
        name: str,
        description: str,
        stacks: int,
        status_type: DMStatusType
    ):

        super().__init__(state, _id, name, description)

        self._stacks: int = int(stacks)
        self._type: DMStatusType = status_type
        self._parent: DMUnit = parent

        self._flat_adjustment: int = 0
        self._scalar: float = 1.0

################################################################################
    def __iadd__(self, other: Union[DMStatus, int]) -> DMStatus:

        if type(other) == type(self):
            self.increase_stacks_flat(other.stacks)
        elif isinstance(other, int):
            self.increase_stacks_flat(other)
        else:
            raise ArgumentTypeError(
                "DMStatus.__iadd__()",
                type(other),
                type(DMStatus), type(int)
            )

        return self

################################################################################
    def __isub__(self, other: Union[DMStatus, int]) -> DMStatus:

        if type(other) == type(self):
            self.reduce_stacks_flat(other.stacks)
        elif isinstance(other, int):
            self.reduce_stacks_flat(other)
        else:
            raise ArgumentTypeError(
                "DMStatus.__iadd__()",
                type(other),
                type(DMStatus), type(int)
            )

        return self

################################################################################
    def __lt__(self, other: DMStatus) -> bool:

        return self.stacks < other.stacks

################################################################################
    def __gt__(self, other: DMStatus) -> bool:

        return self.stacks > other.stacks

################################################################################
    def __le__(self, other: DMStatus) -> bool:

        return self.stacks <= other.stacks

################################################################################
    def __ge__(self, other: DMStatus) -> bool:

        return self.stacks >= other.stacks

################################################################################
    def __repr__(self) -> str:

        return (
            "<DMStatus: "
            f"name={self.name}, type={self.type}, stacks={self.stacks} "
            f"flat_adj={self._flat_adjustment}, scalar: {self._scalar}>"
        )

################################################################################
    @property
    def game(self) -> DMGame:

        return self._parent.game

################################################################################
    @property
    def owner(self) -> DMUnit:

        return self._parent

################################################################################
    @property
    def type(self) -> DMStatusType:

        return self._type

################################################################################
    @property
    def stacks(self) -> int:

        return self._stacks

################################################################################
    def calculate(self) -> int:

        return int((self._stacks * self._scalar) + self._flat_adjustment)

################################################################################
    def reduce_stacks_flat(self, amount: int) -> None:

        if not isinstance(amount, int):
            raise ArgumentTypeError(
                "DMStatus.reduce_stacks().",
                type(amount),
                type(int)
            )

        self._stacks -= amount

################################################################################
    def reduce_stacks_pct(self, amount: float) -> None:

        if not isinstance(amount, float):
            raise ArgumentTypeError(
                "DMStatus.reduce_stacks().",
                type(amount),
                type(float)
            )

        self._stacks = int(self._stacks * amount)

################################################################################
    def increase_stacks_flat(self, amount: int) -> None:

        if not isinstance(amount, int):
            raise ArgumentTypeError(
                "DMStatus.increase_stacks().",
                type(amount),
                type(int)
            )

        self._stacks += amount

################################################################################
    def increase_stacks_pct(self, amount: float) -> None:

        if not isinstance(amount, float):
            raise ArgumentTypeError(
                "DMStatus.reduce_stacks().",
                type(amount),
                type(float)
            )

        self._stacks = int(self._stacks * (amount + 1))

################################################################################
    def reduce_stacks_by_one(self) -> None:

        self.reduce_stacks_flat(1)

################################################################################
    def reduce_stacks_by_half(self) -> None:

        self.reduce_stacks_pct(0.50)

################################################################################
    def _copy(self, **kwargs) -> DMStatus:

        new_obj: Type[S] = super()._copy()  # type: ignore

        new_obj._parent = kwargs.pop("parent")

        new_obj._type = self._type
        new_obj._stacks = int(kwargs.pop("stacks", 1))

        new_obj._flat_adjustment = 0
        new_obj._scalar = 1.0

        return new_obj

################################################################################
    def on_acquire(self) -> None:
        """Called automatically upon the status's initial acquisition by the unit.
        (When it's added to their status list, but not when stacks are added to
        the instance.)"""

        pass

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """For use in an AttackContext-based situation. Is always called in
        every battle loop."""

        pass

################################################################################
    def activate(self) -> None:
        """For use in a no-arguments-required situation. This is not automatically
        called."""

        pass

################################################################################
    def stat_adjust(self) -> None:
        """This function is called automatically when a stat refresh is initiated.
        A refresh can be initiated manually or by the global listener."""

        pass

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect. For example:

        Breakdown:
        ----------
        D = (D0 * 0.5 * (1 + a * n)) / 2

        In this function:

        - D0 is the original dexterity.
        - n is the number of Acceleration stacks.
        - a is the additional effectiveness per stack.
        """

        pass

################################################################################
    def amplify_flat(self, amount: int) -> None:
        """Increases the damage of this status by a flat `amount`.

        If a :class:`float` value is passed, it will be converted to a :class:`int`
        and calculated in accordingly.
        """

        if not isinstance(amount, int):
            raise ArgumentTypeError("DMStatus.amplify_flat().", type(amount), type(int))

        self._flat_adjustment += amount

################################################################################
    def amplify_pct(self, amount: Union[int, float]) -> None:
        """Increases the damage of this status by `amount` percent.

        If amount is of type :class:`int` it will be divided by 100 and applied
        into the scalar as normal.

        Note:
        -----
        Percentages are added directly to the scalar as passed, so you should
        take care to pass the amount of additional damage you want, and not
        the now total scalar value.

        Example:
        --------
        `status.amplify_pct(1.0)` == 100% **additional** damage.

        (Equivalent to 200% total.)
        """

        if not isinstance(amount, (int, float)):
            raise ArgumentTypeError("DMStatus.amplify_pct().", type(amount), type(int))

        if isinstance(amount, int):
            amount /= 100

        self._scalar += amount

################################################################################
    def mitigate_flat(self, amount: Union[int, float]) -> None:
        """Decreases the damage of this status by a flat `amount`.

        If a :class:`float` value is passed, it will be converted to a :class:`int`
        and calculated in accordingly.
        """

        if not isinstance(amount, int):
            raise ArgumentTypeError("DMStatus.mitigate_flat().", type(amount), type(int))

        self._flat_adjustment -= amount

################################################################################
    def mitigate_pct(self, amount: Union[int, float]) -> None:
        """Reduces the damage of this status by `amount` percent.

        If amount is of type :class:`int` it will be divided by 100 and applied
        into the scalar as normal.

        Note:
        -----
        Percentages are added directly to the scalar as passed, so you should
        take care to pass the amount of additional damage you want, and not
        the now total scalar value.

        Example:
        --------
        `status.mitigate_pct(0.5)` == 50% **less** damage.

        (Equivalent to 50% total.)
        """

        if not isinstance(amount, (int, float)):
            raise ArgumentTypeError("DMStatus.mitigate_pct().", type(amount), type(int))

        if isinstance(amount, int):
            amount /= 100

        self._scalar -= amount

################################################################################
