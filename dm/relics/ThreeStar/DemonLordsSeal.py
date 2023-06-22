from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("DemonLordsSeal",)

################################################################################
class DemonLordsSeal(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-230",
            name="Demon Lord's Seal",
            description=(
                "Damage inflicted by enemies under the effect of obey Obey to "
                "other enemies under the effect of Obey is increased by 50 %."
            ),
            rank=3,
            unlock=UnlockPack.Advanced
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        if isinstance(ctx.source, DMHero) and isinstance(ctx.target, DMHero):
            atk_obey = ctx.source.get_status("Obey")
            def_obey = ctx.target.get_status("Obey")
            if atk_obey is None or def_obey is None:
                return

            ctx.amplify_pct(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.50

################################################################################
