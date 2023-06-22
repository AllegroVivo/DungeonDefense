from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.contexts.adjustable import AdjustableContext

if TYPE_CHECKING:
    from dm.core.game.game    import DMGame
    from dm.core.objects.status import DMStatus
    from dm.core.objects.room    import DMRoom
    from dm.core.objects.unit    import DMUnit
################################################################################

__all__ = ("StackReductionContext",)

################################################################################
class StackReductionContext(AdjustableContext):
    """Mediates the loss of stacks from a status effect."""

    def __init__(self, state: DMGame, _obj: DMStatus, base_amt: int):

        super().__init__(state, base_amt, _obj)

################################################################################
    @property
    def room(self) -> DMRoom:

        return self._obj.owner.room  # type: ignore

################################################################################
    @property
    def owner(self) -> DMUnit:

        return self._obj.owner  # type: ignore

################################################################################
    def execute(self) -> int:

        return self.calculate()

################################################################################
