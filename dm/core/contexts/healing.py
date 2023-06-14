from __future__ import annotations

import math

from typing     import TYPE_CHECKING, Union

from .context  import Context
from utilities  import *

if TYPE_CHECKING:
    from dm.core    import DMUnit, DMGame
################################################################################

__all__ = ("HealingContext",)

################################################################################
class HealingContext(Context):

    __slots__ = (
        "_base",
        "_scalar",
        "target"
    )

################################################################################
    def __init__(self, state: DMGame, target: DMUnit, amount: int):

        super().__init__(state)

        self.target: DMUnit = target
        self._base: int = amount
        self._scalar: float = 1.0

################################################################################
    def calculate(self) -> int:

        return math.ceil(self._base * self._scalar)

################################################################################
    def execute(self) -> None:

        self.target.heal(self.calculate())

################################################################################
    def scale(self, amount: Union[int, float]) -> None:

        if not isinstance(amount, (int, float)):
            raise ArgumentTypeError(
                "HealingContext.scale()",
                type(amount),
                type(int), type(float)
            )

        if isinstance(amount, int):
            amount /= 100

        self._scalar += amount

################################################################################
