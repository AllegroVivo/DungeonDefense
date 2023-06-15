from __future__ import annotations

from typing     import TYPE_CHECKING, List, Optional, Union

from ..objects.object    import DMObject
from utilities  import *

if TYPE_CHECKING:
    from ..contexts.attack import AttackContext
    from .game import DMGame
    from ..objects.relic import DMRelic
################################################################################

__all__ = ("DMRelicManager",)

################################################################################
class DMRelicManager:

    __slots__ = (
        "_state",
        "_obtained"
    )

################################################################################
    def __init__(self, game: DMGame):

        self._state: DMGame = game
        self._obtained: List[DMRelic] = []

################################################################################
    def __contains__(self, item: DMRelic) -> bool:

        return item in self._obtained

################################################################################
    def __iter__(self):

        return iter(self._obtained)

################################################################################
    @property
    def game(self) -> DMGame:

        return self._state

################################################################################
    @property
    def obtained(self) -> List[DMRelic]:

        return self._obtained

################################################################################
    def get_relic(self, relic: Union[str, DMRelic]) -> Optional[DMRelic]:

        if not isinstance(relic, (str, DMRelic)):
            raise ArgumentTypeError(
                "RelicManager.get_relic().",
                type(relic),
                type(str), type(DMRelic)
            )

        if isinstance(relic, str):
            result = [r for r in self.obtained if r.name == relic]
        else:
            result = [r for r in self.obtained if r == relic]

        try:
            return result[0]
        except IndexError:
            return

################################################################################
    def add_relic(self, relic: DMRelic) -> None:

        if not isinstance(relic, DMRelic):
            raise ArgumentTypeError(
                "RelicManager.add_relic().",
                type(relic),
                type(DMRelic)
            )

        # Make sure there isn't already an instance in the relic list.
        found = False
        for r in self._obtained:
            if type(relic) == type(r):
                r += 1
                relic = r
                found = True

        # Append to relic list if not present.
        if not found:
            self._obtained.append(relic)

        # Run acquisition callback
        relic.on_acquire()

################################################################################
