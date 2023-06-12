from __future__ import annotations

from typing     import TYPE_CHECKING

from .components    import InfoCardStats
from .levelable     import LevelableInfoCard

if TYPE_CHECKING:
    from dm.core    import DMGame, DMObject
################################################################################

__all__ = ("FighterInfoCard",)

################################################################################
class FighterInfoCard(LevelableInfoCard):

    __slots__ = (
        "_life",
        "_attack",
        "_defense",
    )

################################################################################
    def __init__(self, game: DMGame, obj: DMObject, display_level: bool = True):

        super().__init__(game, obj, display_level)

        # Establish the attributes before running _prepare_surfaces in the parent classes
        self._life: InfoCardStats = InfoCardStats(self, "life")
        self._attack: InfoCardStats = InfoCardStats(self, "attack")
        self._defense: InfoCardStats = InfoCardStats(self, "defense")

################################################################################
