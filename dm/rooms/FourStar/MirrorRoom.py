from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("MirrorRoom",)

################################################################################
class MirrorRoom(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-152",
            name="MirrorRoom",
            description=(
                "Gives {mirror} Mirror and {pleasure} Pleasure to deployed "
                "monsters whenever a hero enters."
            ),
            level=level,
            rank=4,
            unlock=UnlockPack.Advanced,
            effects=[
                Effect(name="Mirror", base=1, per_lv=1),
                Effect(name="Pleasure", base=20, per_lv=20),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        for monster in self.monsters:
            monster.add_status("Mirror", self.effects["Mirror"], self)
            monster.add_status("Pleasure", self.effects["Pleasure"], self)

################################################################################
