from __future__ import annotations

from typing     import TYPE_CHECKING, Type, TypeVar, Union

from .object    import DMObject
from utilities  import *

if TYPE_CHECKING:
    # from .context       import AttackContext
    from dm.core.objects.fighter import DMFighter
    from dm.core.game import DMGame
################################################################################

__all__ = ("DMStatus",)

S = TypeVar("S", bound="DMStatus")

################################################################################
class DMStatus(DMObject):

    __slots__ = (
        "stacks",
        "type",
        "parent",
        "_flat_adjustment",
        "_scalar"
    )

################################################################################
    def __init__(
        self,
        state: DMGame,
        parent: DMFighter,
        *,
        _id: str,
        name: str,
        description: str,
        stacks: int,
        status_type: DMStatusType
    ):

        super().__init__(state, _id, name, description)

        self.stacks: int = stacks
        self.type: DMStatusType = status_type
        self.parent: DMFighter = parent

        self._flat_adjustment: int = 0
        self._scalar: float = 1.0

################################################################################
    def __iadd__(self, other: Union[DMStatus, int]) -> DMStatus:

        if type(other) == type(self):
            self.stacks += other.stacks
        elif isinstance(other, int):
            self.stacks += other

        return self

################################################################################
    def __isub__(self, other: int) -> DMStatus:

        if isinstance(other, int):
            self.stacks += other

        return self

################################################################################
    # @abstractmethod
    # def activate(self, attack: AttackContext) -> None:
    #
    #     raise NotImplementedError

################################################################################
    def calculate(self) -> int:

        return int(self.stacks + self._flat_adjustment * self._scalar)

################################################################################
    def _copy(self, **kwargs) -> DMStatus:

        new_obj: Type[S] = super()._copy()  # type: ignore

        new_obj.parent = kwargs.pop("parent")

        new_obj.type = self.type
        new_obj.stacks = kwargs.pop("stacks")

        return new_obj

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
    def reduce_stacks(self, amount: Union[int, float]) -> None:

        if not isinstance(amount, (int, float)):
            raise ArgumentTypeError(
                "DMStatus.reduce_stacks()",
                type(amount),
                type(int), type(float)
            )

        self.stacks -= int(amount)

################################################################################
