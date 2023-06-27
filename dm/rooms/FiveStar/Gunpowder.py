from __future__ import annotations


from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Gunpowder",)

################################################################################
class Gunpowder(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-171",
            name="Gunpowder",
            description=(
                "If the attacked character in this room is under effect of "
                "Burn, it consumes all of Burn state and inflicts {value} %x "
                "damage to nearby enemies."
            ),
            level=level,
            rank=5,
            unlock=UnlockPack.Original,
            effects=[
                Effect(name="scalar", base=200, per_lv=50)
            ]
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:

        burn = ctx.target.get_status("Burn")
        if burn is not None:
            for hero in self.heroes:
                hero.damage(burn.stacks * (self.effects["scalar"] / 100))

            burn.deplete_all_stacks()

################################################################################
