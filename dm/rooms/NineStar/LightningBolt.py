from __future__ import annotations

import random

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("LightningBolt",)

################################################################################
class LightningBolt(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-230",
            name="Lightning Bolt",
            description=(
                "Once recharged, inflict {damage} damage to 4 random enemies "
                "and give them {status} Shock."
            ),
            level=level,
            rank=9,
            unlock=UnlockPack.Myth,
            base_dmg=81,
            effects=[
                Effect(name="Shock", base=40, per_lv=30),
            ]
        )

################################################################################
    def on_charge(self) -> None:

        heroes = []
        for room in self.adjacent_rooms:
            heroes.extend(room.heroes)

        targets = random.sample(heroes, 4)

        for target in targets:
            target.damage(self.damage)
            target.add_status("Shock", self.effects["Shock"], self)

################################################################################
