from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Bloodthirst",)

################################################################################
class Bloodthirst(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-145",
            name="Bloodthirst",
            description=(
                "Gives {value} Vampire and Fury each to deployed monsters "
                "whenever a hero enters the room."
            ),
            level=level,
            rank=4,
            effects=[
                Effect(name="Vampire", base=20, per_lv=12),
                Effect(name="Fury", base=20, per_lv=12),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        for monster in self.monsters:
            monster.add_status("Vampire", self.effects["Vampire"], self)
            monster.add_status("Fury", self.effects["Fury"], self)

################################################################################
