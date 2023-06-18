from __future__ import annotations

from typing     import TYPE_CHECKING

from .adjustable  import AdjustableContext

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("SoulContext",)

################################################################################
class SoulContext(AdjustableContext):

    def __init__(self, state: DMGame, base_amt: int):

        super().__init__(state, base_amt)

################################################################################
    def execute(self) -> None:

        self._state.inventory.add_soul(self.calculate())

################################################################################
