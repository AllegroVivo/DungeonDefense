from __future__ import annotations

from typing     import TYPE_CHECKING

from .components    import InfoCardLevel
from .ranked        import RankedInfoCard

if TYPE_CHECKING:
    from dm.core    import DMGame, DMObject
################################################################################

__all__ = ("LevelableInfoCard",)

################################################################################
class LevelableInfoCard(RankedInfoCard):

    __slots__ = (
        "_level",
        "_display_level"
    )

################################################################################
    def __init__(
        self,
        game: DMGame,
        obj: DMObject,
        display_level: bool,
        display_rank: bool = True
    ):

        super().__init__(game, obj, display_rank)

        self._level: InfoCardLevel = InfoCardLevel(self)
        self._display_level: bool = display_level

################################################################################
