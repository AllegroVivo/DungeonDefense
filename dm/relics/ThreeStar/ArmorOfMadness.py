from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.monster import DMMonster
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("ArmorOfMadness",)

################################################################################
class ArmorOfMadness(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-184",
            name="Armor of Madness",
            description="Damage received decreases by 20 % when in Rampage status.",
            rank=3
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:

        # If a monster is defending
        if isinstance(ctx.target, DMMonster):
            # And has the Rampage status
            rampage = ctx.target.get_status("Rampage")
            if rampage is not None:
                # Reduce the damage received by 20%
                ctx.mitigate_pct(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.20

################################################################################
