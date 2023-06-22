from __future__ import annotations

from abc        import abstractmethod
from typing     import TYPE_CHECKING, Optional

from .adjustable import AdjustableContext

if TYPE_CHECKING:
    from dm.core.game.game    import DMGame
    from dm.core.objects.object import DMObject
################################################################################

__all__ = ("CorruptionContext",)

################################################################################
class CorruptionContext(AdjustableContext):

    __slots__ = (

    )

################################################################################
    def __init__(self, state: DMGame, base_amt: int = 0, _obj: Optional[DMObject] = None):

        super().__init__(state, base_amt, _obj)

################################################################################
    @abstractmethod
    def execute(self) -> None:

        raise NotImplementedError

################################################################################
