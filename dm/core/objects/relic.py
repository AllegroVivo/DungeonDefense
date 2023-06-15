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

    __slots__ = (
        "_uses",
        "_count",
        "_repeatable",
    )

################################################################################
    def __init__(
        self,
        state: DMGame,
        _id: str,
        name: str,
        description: Optional[str],
        rank: int = 0,
        unlock: Optional[UnlockPack] = None,
        uses: int = 1
    ):

        super().__init__(state, _id, name, description, rank, unlock)

        self._uses: int = uses
        self._repeatable: bool = self._uses > 1
        self._count = 1

################################################################################
    def __iadd__(self, other: int) -> DMRelic:

        if not isinstance(other, int):
            raise ArgumentTypeError(
                "RelicManager.add_relic().",
                type(other),
                type(int)
            )

        self._count += other

        return self

################################################################################
    def on_acquire(self) -> None:

        pass

################################################################################
    def activate(self) -> None:

        pass

################################################################################
    def handle(self, ctx: AttackContext) -> None:

        pass

################################################################################
    def effect_value(self) -> float:

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

        new_obj._uses = self._uses
        new_obj._repeatable = self._repeatable
        new_obj._count = 1

        return new_obj  # type: ignore

################################################################################
