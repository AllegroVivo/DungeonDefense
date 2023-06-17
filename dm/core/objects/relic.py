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

################################################################################~
    def __iadd__(self, other: Union[int, DMRelic]) -> DMRelic:

        if not isinstance(other, (int, DMRelic)):
            raise ArgumentTypeError(
                "DMRelic.__iadd__().",
                type(other),
                type(int), type(DMRelic)
            )

        if isinstance(other, int):
            self._count += other
        else:
            self._count += other._count

################################################################################
    @property
    def type(self) -> DMType:

        return DMType.Relic

################################################################################
    @property
    def number_owned(self) -> int:

        return self._count

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
