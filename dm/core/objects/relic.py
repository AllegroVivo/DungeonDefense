from __future__ import annotations

from typing     import TYPE_CHECKING, Optional, Type, TypeVar, Union
from .object    import DMObject
from utilities  import *

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("DMRelic",)

R = TypeVar("R", bound="DMRelic")

################################################################################
class DMRelic(DMObject):

    __slots__ = (
        "_count",
    )

################################################################################
    def __init__(
        self,
        state: DMGame,
        _id: str,
        name: str,
        description: Optional[str],
        rank: int = 0,
        unlock: Optional[UnlockPack] = None
    ):

        super().__init__(state, _id, name, description, rank, unlock)

        self._count: int = 1

        # Subscribe to the events we'll be listening for most.
        self.listen("relic_acquired", self.on_acquire)
        self.listen("stat_refresh", self.stat_adjust)
        self.listen("on_attack", self.handle)

################################################################################
    @property
    def type(self) -> DMType:

        return DMType.Relic

################################################################################
    @property
    def count(self) -> int:

        return self._count

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        pass

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called when the `on_attack` event is fired."""

        pass

################################################################################
    def stat_adjust(self) -> None:
        """Automatically called when the `stat_refresh` event is fired."""

        pass

################################################################################
    def effect_value(self) -> float:
        """The value of the effect corresponding to this relic."""

        pass

################################################################################
    def notify(self, *args) -> None:
        """A general event response function."""

        pass

################################################################################
    def _copy(self) -> DMRelic:
        """Returns a clean copy of the current relic type.

        Returns:
        --------
        :class:`DMRelic`
            A fresh copy of the current DMObject.

        """

        new_obj: Type[R] = super()._copy()  # type: ignore

        return new_obj  # type: ignore

################################################################################
