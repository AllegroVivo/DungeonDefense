from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..facilityroom import DMFacilityRoom
from utilities      import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Blacksmith",)

################################################################################
class Blacksmith(DMFacilityRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-191",
            name="Blacksmith",
            description=(
                "Increases ATK of monsters in adjacent rooms by {value}%."
            ),
            level=level,
            rank=5,
            unlock=UnlockPack.Advanced,
            effects=[
                Effect(name="atk", base=30, per_lv=2),
            ]
        )

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        targets = []
        for room in self.adjacent_rooms + [self]:
            targets.extend(room.monsters)

        for monster in targets:
            monster.increase_stat_pct("atk", self.effects["atk"] / 100)  # Convert to percentage

################################################################################
