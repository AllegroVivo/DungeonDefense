from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.contexts.adjustable import AdjustableContext

if TYPE_CHECKING:
    from dm.core.game.game    import DMGame
    from dm.core.objects.status import DMStatus
################################################################################

__all__ = ("StackContext",)

################################################################################
class StackContext(AdjustableContext):
    """Mediates the loss of stacks from a status effect."""

    def __init__(self, state: DMGame, _obj: DMStatus, base_amt: int):

        super().__init__(state)

        self._obj: DMStatus = _obj

        self._base: int = base_amt
        self._scalar: float = 1.0
        self._flat_adjustment: int = 0

################################################################################
    @property
    def object(self) -> DMStatus:

        return self._obj

################################################################################
    def execute(self) -> None:

        raise NotImplementedError

################################################################################
