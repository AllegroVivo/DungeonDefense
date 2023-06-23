from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Betrayal",)

################################################################################
class Betrayal(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-133",
            name="Betrayal",
            description=(
                "Gives {value} Pleasure to monsters in the room whenever "
                "a hero enters."
            ),
            level=level,
            rank=2,
            unlock=UnlockPack.Original,
            effects=[
                Effect(name="Pleasure", base=6, per_lv=6),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        for monster in self.monsters:
            monster.add_status("Pleasure", self.effects["Pleasure"], self)

################################################################################
