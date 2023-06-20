from __future__ import annotations

import random

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from ..traproom   import DMTrapRoom
from ...core.objects.hero import DMHero

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Template",)

################################################################################
class Template(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-000",
            name="UrMom",
            description=(
                "UrMom"
            ),
            level=level,
            rank=4
        )

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        pass

################################################################################
    def effect_value(self) -> int:
        """The value(s) of this room's effect.

        Breakdown:
        ----------
        **effect = b + (a * LV)**

        In this function:

        - b is the base effectiveness.
        - a is the additional effectiveness per level.
        - LV is the level of this room.
        """

        pass

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when this room is added to the map."""

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
