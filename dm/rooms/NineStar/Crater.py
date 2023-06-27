from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Crater",)

################################################################################
class Crater(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-229",
            name="Crater",
            description=(
                "Once recharged, inflict {damage} damage to all enemies "
                "in adjacent area and give them {status} Burn."
            ),
            level=level,
            rank=9,
            unlock=UnlockPack.Myth,
            base_dmg=121,
            effects=[
                Effect(name="Burn", base=144, per_lv=108),
            ]
        )

################################################################################
    def on_charge(self) -> None:

        for room in self.adjacent_rooms + [self]:
            for hero in room.heroes:
                hero.damage(self.dmg)
                hero.add_status("Burn", self.effects["Burn"], self)

##############################################################################
