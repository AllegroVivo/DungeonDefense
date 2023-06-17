from __future__ import annotations

from typing     import TYPE_CHECKING

from .context  import Context
from utilities  import *

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.levelable import DMLevelable
################################################################################

__all__ = ("ExperienceContext",)

################################################################################
class ExperienceContext(Context):

    __slots__ = (
        "_obj",
        "_exp",
        "_scalar",
        "_flat_adjustment"
    )

################################################################################
    def __init__(self, state: DMGame, obj: DMLevelable, base_exp: int):

        super().__init__(state)

        self._obj: DMLevelable = obj
        self._exp: int = base_exp
        self._scalar: float = 1.0
        self._flat_adjustment: int = 0

################################################################################
    @property
    def target(self) -> DMLevelable:

        return self._obj

################################################################################
    def scale(self, amount: float) -> None:

        if not isinstance(amount, float):
            raise ArgumentTypeError("ExperienceContext.scale_exp()", type(amount), type(float))

        self._scalar += amount

################################################################################
    def execute(self) -> None:

        if self._scalar < 0:
            self._scalar = 0

        self._obj.grant_exp((self._exp * self._scalar) + self._flat_adjustment)

################################################################################
    def mitigate_flat(self, value: int) -> None:
        """Applies reduction to this attack's experience calculation.

        Arguments of class :class:`float` will **NOT** be interpreted as a
        percentage and will be converted to a flat amount of reduction.

        Example:
        --------
        `ctx.mitigate_flat(25000)` == -25,000 removed from experience total

        Note:
        -----
            Just for clarification, positive values will **reduce** experience and
            negative values will **increase** experience.

        Parameters:
        -----------
        value: :class:`int`
            The amount to remove from this attack's experience.
        """

        self._flat_adjustment -= value

################################################################################
    def mitigate_pct(self, value: float) -> None:
        """Applies reduction to this attack's experience calculation.

        Arguments of class :class:`int` will **NOT** be interpreted as flat
        experience reduction and will be converted to a float and calculated as such.
        Values should be how much additional you want the experience reduced.

        Example:
        --------
        `ctx.mitigate_pct(0.25)` == -25% less experience overall

        Note:
        -----
            Just for clarification, positive values will **reduce** experience and
            negative values will **increase** experience.

        Parameters:
        -----------
        value: :class:`float`
            The percent to remove from this attack's experience.
        """

        self._scalar -= value

################################################################################
    def amplify_flat(self, value: int) -> None:
        """Applies an increase to this attack's experience calculation.

        Arguments of class :class:`float` will **NOT** be interpreted as a
        percentage and will be converted to a flat amount of bonus experience.

        Example:
        --------
        `ctx.amplify_flat(25000)` == +25,000 additional experience added to total

        Note:
        -----
            Just for clarification, positive values will **increase** experience and
            negative values will **reduce** experience.

        Parameters:
        -----------
        value: :class:`int`
            The amount to add to this attack's experience.
        """

        self._flat_adjustment += value

################################################################################
    def amplify_pct(self, value: float) -> None:
        """Applies an increase to this attack's experience calculation.

        Arguments of class :class:`int` will **NOT** be interpreted as flat
        experience bonus and will be converted to a float and calculated as such.
        Values should be how much additional you want the experience increased.

        Example:
        --------
        `ctx.amplify_pct(0.25)` == +25% additional experience overall

        Note:
        -----
            Just for clarification, positive values will **increase** experience and
            negative values will **reduce** experience.

        Parameters:
        -----------
        value: :class:`float`
            The percent to remove from this attack's experience.
        """

        self._scalar += value
        
################################################################################
