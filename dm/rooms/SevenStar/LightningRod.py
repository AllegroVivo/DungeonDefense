from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("LightningRod",)

################################################################################
class LightningRod(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-212",
            name="Lightning Rod",
            description=(
                "Once recharged, inflict {damage} damage to a random hero in "
                "the dungeon and give them {status} Shock."
            ),
            level=level,
            rank=7,
            unlock=UnlockPack.Myth,
            base_dmg=121,
            effects=[
                Effect(name="Shock", base=48, per_lv=32)
            ]
        )
        self.setup_charging(3.3, 3.3)

################################################################################
    def on_charge(self) -> None:

        target = self.random.choice(self.game.all_heroes)
        target.damage(self.dmg)
        target.add_status("Shock", self.effects["Shock"], self)

################################################################################
