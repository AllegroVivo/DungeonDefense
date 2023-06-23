from __future__ import annotations

from abc        import abstractmethod
from typing     import TYPE_CHECKING, Optional

from .adjustable import AdjustableContext

if TYPE_CHECKING:
    from dm.core.game.game    import DMGame
    from dm.core.objects.unit import DMUnit
    from dm.core.objects.room import DMRoom
################################################################################

__all__ = ("TortureContext",)

################################################################################
class TortureContext(AdjustableContext):

    __slots__ = (

    )

################################################################################
    def __init__(self, state: DMGame, base_amt: int = 0, _obj: Optional[DMUnit] = None):

        super().__init__(state, base_amt, _obj)

################################################################################
    @property
    def room(self) -> DMRoom:

        return self._obj.room

################################################################################
    def execute(self) -> None:

        raise NotImplementedError

################################################################################
