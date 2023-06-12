from __future__ import annotations

from typing     import TYPE_CHECKING

from .components    import InfoCardDescription
from .ranked        import RankedInfoCard
from utilities      import *

if TYPE_CHECKING:
    from dm.core    import DMGame, DMObject
################################################################################

__all__ = ("DescriptionInfoCard",)

################################################################################
class DescriptionInfoCard(RankedInfoCard):

    __slots__ = (
        "_description",
    )

################################################################################
    def __init__(self, game: DMGame, obj: DMObject, show_rank: bool = False):

        super().__init__(game, obj, show_rank)

        self._description: InfoCardDescription = InfoCardDescription(self)

################################################################################
