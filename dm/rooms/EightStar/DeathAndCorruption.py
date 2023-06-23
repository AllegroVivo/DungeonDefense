from __future__ import annotations

import random

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional, Tuple

from ..traproom   import DMTrapRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("DeathAndCorruption",)

################################################################################
class DeathAndCorruption(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-221",
            name="Death and Corruption",
            description=(
                "Once recharged, inflict {damage} damage to all enemies in "
                "adjacent area and give them {status} Corpse Explosion."
            ),
            level=level,
            rank=8,
            unlock=UnlockPack.Myth,
            base_dmg=121,
            effects=[
                Effect(name="Corpse Explosion", base=48, per_lv=36)
            ]
        )
        self.setup_charging(3.3, 3.3)

################################################################################
    def on_charge(self) -> None:

        targets = []
        for room in self.adjacent_rooms:
            targets.extend(room.heroes)

        for target in targets:
            target.damage(self.damage)
            target.add_status("Corpse Explosion", self.effects["Corpse Explosion"], self)

################################################################################
