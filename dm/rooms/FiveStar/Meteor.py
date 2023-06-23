from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Meteor",)

################################################################################
class Meteor(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-180",
            name="Meteor",
            description=(
                "Inflicts {damage} damage and gives {status} Burn to all heroes "
                "in the room when a hero enters the room. Damage inflicted is "
                "doubled for enemies under the effect of Slow."
            ),
            level=level,
            rank=5,
            unlock=UnlockPack.Original,
            base_dmg=31,
            effects=[
                Effect(name="Burn", base=32, per_lv=24)
            ]
        ),

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        for hero in self.heroes:
            damage = self.damage
            if unit.get_status("Slow") is not None:
                damage *= 2

            hero.damage(damage)
            hero.add_status("Burn", self.effects["Burn"], self)

################################################################################
