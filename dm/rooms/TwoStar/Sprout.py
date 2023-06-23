from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Sprout",)

################################################################################
class Sprout(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-118",
            name="Sprout",
            description=(
                "Gives {value} Regeneration to the deployed monsters whenever "
                "a hero enters the room."
            ),
            level=level,
            rank=2,
            effects=[
                Effect(name="Regeneration", base=32, per_lv=16),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        for monster in self.monsters:
            monster.add_status("Regeneration", self.effects["Regeneration"], self)

################################################################################
