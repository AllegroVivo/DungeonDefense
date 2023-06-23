from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("BigBang",)

################################################################################
class BigBang(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-235",
            name="Big Bang",
            description=(
                "Once recharged, inflict {damage} damage to all enemies in the "
                "dungeon, and apply them {status} Burn and {status} Shock."
            ),
            level=level,
            rank=10,
            unlock=UnlockPack.Myth,
            base_dmg=121,
            effects=[
                Effect(name="Burn", base=80, per_lv=40),
                Effect(name="Shock", base=80, per_lv=40),
            ]
        )
        self.setup_charging(6.6, 6.6)

################################################################################
    def on_charge(self) -> None:

        for hero in self.game.all_heroes:
            hero.damage(self.damage)
            hero.add_status("Burn", self.effects["Burn"], self)
            hero.add_status("Shock", self.effects["Shock"], self)

################################################################################
