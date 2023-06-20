from __future__ import annotations


from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import UnlockPack

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
            unlock=UnlockPack.Original
        )

################################################################################
    def effect_value(self) -> float:
        """The value(s) of this room's effect.

        Breakdown:
        ----------
        **effect = b + (a * LV)**

        In this function:

        - b is the base effectiveness.
        - a is the additional effectiveness per level.
        - LV is the level of this room.
        """

        return (200 + (50 * self.level)) / 100  # Convert to percentage.

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        if ctx.room == self:
            # Appears to apply to all units.
            burn = ctx.defender.get_status("Burn")
            if burn is not None:
                for hero in self.heroes:
                    hero.damage(self.effect_value() * burn.stacks)
                burn.reduce_stacks_flat(burn.stacks)

################################################################################
