from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from .adjustable import AdjustableContext

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.object import DMObject
################################################################################

__all__ = ("PurchaseContext",)

################################################################################
class PurchaseContext(AdjustableContext):

    def __init__(self, state: DMGame, base_price: int, obj: Optional[DMObject] = None):

        super().__init__(state, base_price, obj)

################################################################################
    def execute(self) -> None:

        self._state.inventory.add_item(self._obj)

################################################################################
