from __future__ import annotations

from typing     import TYPE_CHECKING, Optional, Type, TypeVar
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

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        pass

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        pass

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

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
