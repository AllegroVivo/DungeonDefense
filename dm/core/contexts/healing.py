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
        "_flat_additional",
        "target"
    )

################################################################################
    def __init__(self, state: DMGame, target: DMUnit, amount: int):

        super().__init__(state)

        self.target: DMUnit = target
        self._base: int = amount
        self._scalar: float = 1.0
        self._flat_additional: int = 0

################################################################################
    def calculate(self) -> int:

        return math.ceil((self._base * self._scalar) + self._flat_additional)

################################################################################
    def execute(self) -> None:

        self.target.heal(self.calculate())

################################################################################
    def modify_flat(self, amount: int) -> None:

        if not isinstance(amount, int):
            raise ArgumentTypeError(
                "HealingContext.modify_flat()",
                type(amount),
                type(int)
            )

        self._flat_additional += amount

################################################################################
    def scale(self, amount: float) -> None:

        if not isinstance(amount, float):
            raise ArgumentTypeError(
                "HealingContext.scale()",
                type(amount),
                type(float)
            )

        self._scalar += amount

################################################################################
