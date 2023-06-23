from __future__ import annotations

import random

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional, Tuple

from ..traproom   import DMTrapRoom
from utilities import *

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("MeteorShower",)

################################################################################
class MeteorShower(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-199",
            name="Meteor Shower",
            description=(
                "Inflicts {damage} damage and gives {status} Burn to all "
                "heroes in adjacent rooms when a hero enters the room. Damage "
                "inflicted is doubled for enemies under the effect of Slow."
            ),
            level=level,
            rank=6,
            unlock=UnlockPack.Awakening,
            base_dmg=49,
            effects=[
                Effect(name="Burn", base=128, per_lv=96),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        targets = []
        for room in self.adjacent_rooms:
            targets.extend(room.get_heroes_or_monsters(unit))

        for target in targets:
            damage = self.damage
            burn = target.get_status("Burn")
            if burn is not None:
                damage *= 2

            target.damage(damage)
            target.add_status("Burn", self.effects["Burn"], self)

################################################################################
