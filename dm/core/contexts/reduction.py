from __future__ import annotations

from typing     import TYPE_CHECKING

from .stacks import StackContext

if TYPE_CHECKING:
    from dm.core.game.game    import DMGame
    from dm.core.objects.status import DMStatus
################################################################################

__all__ = ("StackReductionContext",)

################################################################################
class StackReductionContext(StackContext):
    """Mediates the loss of stacks from a status effect."""

    def __init__(self, state: DMGame, _obj: DMStatus, base_amt: int):

        super().__init__(state, _obj, base_amt)

################################################################################
    def execute(self) -> None:

        self._obj._stacks -= self.calculate()

################################################################################
