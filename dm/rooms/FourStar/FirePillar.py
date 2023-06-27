from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("FirePillar",)

################################################################################
class FirePillar(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-166",
            name="FirePillar",
            description=(
                "Inflicts {damage} damage and gives {status} Burn to all "
                "enemies in the room when a hero enters the room."
            ),
            level=level,
            rank=4,
            unlock=UnlockPack.Awakening,
            base_dmg=73,
            effects=[
                Effect(name="Burn", base=240, per_lv=192),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        for hero in self.heroes:
            hero.damage(self.dmg)
            hero.add_status("Burn", self.effects["Burn"], self)

################################################################################
