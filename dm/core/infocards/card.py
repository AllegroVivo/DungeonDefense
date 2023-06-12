from __future__ import annotations

from pygame         import Surface
from typing         import TYPE_CHECKING, List

from .components    import (
    InfoCardBorder,
    InfoCardComponent,
    InfoCardDescription,
    InfoCardLevel,
    InfoCardMainSprite,
    InfoCardRank,
    InfoCardStats,
    InfoCardSubtitle,
    InfoCardTitle
)
from utilities      import *

if TYPE_CHECKING:
    from dm.core    import DMGame, DMObject
################################################################################

__all__ = ("DMInfoCard",)

################################################################################
class DMInfoCard:

    __slots__ = (
        "_state",
        "_obj",
        "_surface",
        "_title",
        "_display_title",
        "_subtitle",
        "_display_subtitle",
        "_border",
        "_display_border",
        "_main_sprite",
        "_display_main_sprite",
        "_children",
        "_description",
        "_display_description",
        "_rank",
        "_display_rank",
        "_stats",
        "_display_stats",
        "_level",
        "_display_level"
    )

    WIDTH = 200
    HEIGHT = 300

################################################################################
    def __init__(
        self,
        game: DMGame,
        obj: DMObject,
        *,
        title: bool = True,
        subtitle: bool = True,
        border: bool = True,
        main_sprite: bool = True,
        description: bool = True,
        rank: bool = False,
        stats: bool = False,
        level: bool = False
    ):

        self._state: DMGame = game
        self._obj: DMObject = obj
        self._children: List[InfoCardComponent] = []

        # This is ultimately the render order, starting at the top.
        self._title: InfoCardTitle = InfoCardTitle(self)
        self._display_title: bool = title

        self._main_sprite: InfoCardMainSprite = InfoCardMainSprite(self)
        self._display_main_sprite: bool = main_sprite

        self._subtitle: InfoCardSubtitle = InfoCardSubtitle(self)
        self._display_subtitle: bool = subtitle

        self._border: InfoCardBorder = InfoCardBorder(self)
        self._display_border: bool = border

        self._description: InfoCardDescription = InfoCardDescription(self)
        self._display_description: bool = description

        self._rank: InfoCardRank = InfoCardRank(self)
        self._display_rank: bool = rank

        self._stats: InfoCardStats = InfoCardStats(self)
        self._display_stats: bool = stats

        self._level: InfoCardLevel = InfoCardLevel(self)
        self._display_level: bool = level

        self._surface: Surface = None  # type: ignore
        self._prepare_surface()

################################################################################
    def _prepare_surface(self) -> None:

        self._surface: Surface = Surface((self.WIDTH, self.HEIGHT))

################################################################################
    def draw(self, screen, x: int, y: int) -> None:

        self._surface.fill(BLACK)

        for child in self._children:
            cls = child.__class__.__name__
            # Check for visibility of the various attached components.
            if cls == "InfoCardTitle":
                if not self._display_title:
                    continue
            elif cls == "InfoCardBorder":
                if not self._display_border:
                    continue
            elif cls == "InfoCardMainSprite":
                if not self._display_main_sprite:
                    continue
            elif cls == "InfoCardSubtitle":
                if not self._display_subtitle:
                    continue
            elif cls == "InfoCardDescription":
                if not self._display_description:
                    continue
            elif cls == "InfoCardRank":
                if not self._display_rank:
                    continue
            elif cls == "InfoCardStats":
                if not self._display_stats:
                    continue
            elif cls == "InfoCardLevel":
                if not self._display_level:
                    continue
            child.render(self._surface)

        screen.blit(self._surface, (x, y))

################################################################################
