from __future__ import annotations

from abc        import abstractmethod
from typing     import TYPE_CHECKING, Optional

from .context import Context

if TYPE_CHECKING:
    from dm.core.game.game    import DMGame
    from dm.core.objects.object import DMObject
################################################################################

__all__ = ("AdjustableContext",)

################################################################################
class AdjustableContext(Context):

    __slots__ = (
        "_obj",
        "_base",
        "_scalar",
        "_flat_adjustment",
    )

################################################################################
    def __init__(self, state: DMGame, base_amt: int, _obj: Optional[DMObject] = None):

        super().__init__(state)

        self._obj: Optional[DMObject] = _obj

        self._base: int = base_amt
        self._scalar: float = 1.0
        self._flat_adjustment: int = 0

################################################################################
    @property
    def object(self) -> Optional[DMObject]:

        return self._obj

################################################################################
    @abstractmethod
    def execute(self) -> None:

        raise NotImplementedError

################################################################################
    def reduce_flat(self, value: int) -> None:
        """Applies a flat amount of reduction to this calculation.

        Arguments must be of class :class:`int` and amount to the total
        value you want removed from the calculation.

        Example:
        --------
        `ctx.mitigate_flat(25000)` == -25,000 removed from total amount

        Parameters:
        -----------
        value: :class:`int`
            The amount to remove from this calculation's value.
        """

        self._flat_adjustment -= value

################################################################################
    def reduce_pct(self, value: float) -> None:
        """Applies percentage-based reduction to this calculation.

        Arguments must be of class :class:`float` and must be the amount of
        effectiveness you want to remove.

        Example:
        --------
        `ctx.mitigate_pct(0.25)` == -25% less value overall

        Parameters:
        -----------
        value: :class:`float`
            The percent to remove to this calculation's value.
        """

        self._scalar -= value

################################################################################
    def amplify_flat(self, value: int) -> None:
        """Applies a flat increase to this calculation.

        Arguments must be of class :class:`int` and amount to the total
        value you want added to the calculation.

        Example:
        --------
        `ctx.amplify_flat(25000)` == 25,000 added to final calculation

        Parameters:
        -----------
        value: :class:`int`
            The amount to add to this calculation's value.
        """

        self._flat_adjustment += value

################################################################################
    def amplify_pct(self, value: float) -> None:
        """Applies percentage-based increase to this calculation.

        Arguments must be of class :class:`float` and must be the amount of
        effectiveness you want to add.

        Example:
        --------
        `ctx.amplify_pct(0.25)` == 25% more value overall

        Parameters:
        -----------
        value: :class:`float`
            The percent to add to this calculation's value.
        """

        self._scalar += value

################################################################################
    def calculate(self) -> int:

        if self._scalar < 0:
            self._scalar = 0

        return int((self._base * self._scalar) + self._flat_adjustment)

################################################################################
