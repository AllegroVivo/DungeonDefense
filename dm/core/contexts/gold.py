from __future__ import annotations

from typing     import TYPE_CHECKING

from .context  import Context
from utilities  import *

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("GoldSoulContext",)

################################################################################
class GoldSoulContext(Context):

    __slots__ = (
        "_type",
        "_base",
        "_scalar"
    )

################################################################################
    def __init__(self, state: DMGame, _type: str, amount: int):

        super().__init__(state)

        self._type: str = _type
        self._base: int = amount
        self._scalar: float = 1.0

################################################################################
    def scale(self, amount: float) -> None:

        if not isinstance(amount, float):
            raise ArgumentTypeError("Context.scale_exp()", type(amount), type(float))

        self._scalar += amount

################################################################################
    def execute(self) -> None:

        if self._scalar < 0:
            self._scalar = 0

        if self._type == "gold":
            self._state.inventory.add_gold(self.calculate())
        elif self._type == "soul":
            self._state.inventory.add_soul(self.calculate())

################################################################################
    def calculate(self) -> int:

        return int(self._base * self._scalar)

################################################################################
