from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities  import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ChaosRain",)

################################################################################
class ChaosRain(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-198",
            name="Chaos Rain",
            description=(
                "Inflict {damage} damage to to all enemies that entered the "
                "room, and give {status} Poison, Burn, and Shock each"
            ),
            level=level,
            rank=6,
            unlock=UnlockPack.Awakening,
            base_dmg=73,
            effects=[
                Effect(name="Status", base=32, per_lv=24),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        if unit.room == self:
            # Ouch
            unit.damage(self.dmg)
            for status in ("Poison", "Burn", "Shock"):
                unit.add_status(status, self.effects["Status"], self)

################################################################################
