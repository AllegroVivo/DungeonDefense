from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from ...rooms.traproom import DMTrapRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("JewelOfTheDeepSea",)

################################################################################
class JewelOfTheDeepSea(DMRelic):

    SLOW_TRAPS = (
        "Ice", "Rockslide", "Icebolt", "Ice Pit", "Frost Storm", "Swamp Monster"
    )

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-222",
            name="Jewel of the Deep Sea",
            description=(
                "Traps that give Slow have their damage increased by 100 %."
            ),
            rank=3,
            unlock=UnlockPack.Original
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        if isinstance(ctx.source, DMTrapRoom):
            if ctx.source.name in self.SLOW_TRAPS:
                ctx.amplify_pct(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 1.00

################################################################################
