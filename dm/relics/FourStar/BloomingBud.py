from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.monster import DMMonster
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("BloomingBud",)

################################################################################
class BloomingBud(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-265",
            name="Blooming Bud",
            description=(
                "Get Regeneration as much as 100 % of DEF when receiving damage."
            ),
            rank=4,
            unlock=UnlockPack.Original
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        if isinstance(ctx.target, DMMonster):
            ctx.register_after_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:
        """A general event response function."""

        if ctx.damage > 0:
            ctx.target.add_status("Regeneration", ctx.target.defense * 1.00)

################################################################################
