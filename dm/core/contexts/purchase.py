from __future__ import annotations

import math

from typing     import TYPE_CHECKING, Optional, Union

from .context  import Context
from utilities  import *

if TYPE_CHECKING:
    from dm.core    import DMGame, DMObject
################################################################################

__all__ = ("PurchaseContext",)

################################################################################
class PurchaseContext(Context):

    __slots__ = (
        "_base_cost",
        "_scalar",
        "_type",
        "_obj"
    )

################################################################################
    def __init__(
        self,
        state: DMGame,
        base_price: int,
        purchase_type: DMPurchaseType,
        object: Optional[DMObject] = None
    ):

        super().__init__(state)

        self._base_cost: int = base_price
        self._type: DMPurchaseType = purchase_type
        self._scalar: float = 1.0
        self._obj: Optional[DMObject] = object

################################################################################
    def calculate(self) -> int:

        return math.ceil(self._base_cost * self._scalar)

################################################################################
    def execute(self) -> None:

        self._state.inventory.add_item(self._obj)

################################################################################
    def scale(self, amount: Union[int, float]) -> None:

        if not isinstance(amount, (int, float)):
            raise ArgumentTypeError(
                "PurchaseContext.scale()",
                type(amount),
                type(int), type(float)
            )

        if isinstance(amount, int):
            amount /= 100

        self._scalar += amount

################################################################################
