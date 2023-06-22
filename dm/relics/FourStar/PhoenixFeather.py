from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.monster import DMMonster
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("PhoenixFeather",)

################################################################################
class PhoenixFeather(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-269",
            name="Phoenix Feather",
            description=(
                "Allies under the effect of Acceleration will receive "
                "35 % less damage."
            ),
            rank=4,
            unlock=UnlockPack.Original
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        if isinstance(ctx.target, DMMonster):
            acceleration = ctx.target.get_status("Acceleration")
            if acceleration is not None:
                ctx.mitigate_pct(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.35

################################################################################
