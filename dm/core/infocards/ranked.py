from __future__ import annotations

from typing     import TYPE_CHECKING

from .card         import DMInfoCard
from .components    import InfoCardRank

if TYPE_CHECKING:
    from dm.core    import DMGame, DMObject
################################################################################

__all__ = ("RankedInfoCard",)

################################################################################
class RankedInfoCard(DMInfoCard):

    __slots__ = (
        "_stars",
        "_display_rank"
    )

################################################################################
    def __init__(self, game: DMGame, obj: DMObject, show: bool):

        super().__init__(game, obj)

        self._stars: InfoCardRank = InfoCardRank(self)
        self._display_rank: bool = show

################################################################################
