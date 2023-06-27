from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ThornBush",)

################################################################################
class ThornBush(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-195",
            name="Thorn Bush",
            description=(
                "Gives {value} Armor, Thorn to all monsters in adjacent rooms "
                "whenever a hero enters."
            ),
            level=level,
            rank=6,
            unlock=UnlockPack.Advanced,
            effects=[
                Effect(name="Status", base=36, per_lv=24),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        for room in self.adjacent_rooms + [self]:
            for monster in room.monsters:
                for status in ("Armor", "Thorn"):
                    monster.add_status(status, self.effects["Status"], self)

################################################################################
