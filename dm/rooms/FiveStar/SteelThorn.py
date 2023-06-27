from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("SteelThorn",)

################################################################################
class SteelThorn(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-178",
            name="Steel Thorn",
            description=(
                "Gives {value} Armor and Thorn to deployed monsters in the "
                "dungeon when a hero enters."
            ),
            level=level,
            rank=5,
            unlock=UnlockPack.Advanced,
            effects=[
                Effect(name="Status", base=36, per_lv=24),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        for monster in self.monsters:
            for status in ("Armor", "Thorn"):
                monster.add_status(status, self.effects["Status"], self)

################################################################################
