from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities     import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("IronMaiden",)

################################################################################
class IronMaiden(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-114",
            name="Iron Maiden",
            description=(
                "Gives {value} Thorn to deployed monsters whenever a hero enters."
            ),
            level=level,
            rank=2,
            effects=[
                Effect(name="Thorn", base=18, per_lv=12),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        for monster in self.monsters:
            monster.add_status("Thorn", self.effects["Thorn"], self)

################################################################################
