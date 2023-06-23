from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from ...rooms.traproom import DMTrapRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("StatueOfLiberatedRage",)

################################################################################
class StatueOfLiberatedRage(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-338",
            name="Statue of Liberated Rage",
            description=(
                "All characters in the dungeon get Fury as much as 30 % of "
                "ATK when attacking. All characters have a very low chance to "
                "attack allies."
            ),
            rank=5,
            unlock=UnlockPack.Adventure
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        # Doesn't apply to traps.
        if isinstance(ctx.source, DMTrapRoom):
            return

        # Add Fury to the attacker.
        ctx.source.add_status("Fury", ctx.source.attack * self.effect_value(), self)

        # Low chance to attack allies. 5% seems reasonable like before.
        if self.random.chance(5):
            source = ctx.room.get_heroes_or_monsters(ctx.source)
            ctx.reassign_defender(self.random.choice(source))

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.30

################################################################################
