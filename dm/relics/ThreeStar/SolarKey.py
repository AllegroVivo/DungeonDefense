from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("SolarKey",)

################################################################################
class SolarKey(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-236",
            name="Solar Key",
            description=(
                "Gives 2 Recharge when inflicting damage to an enemy under the "
                "effect of Blind."
            ),
            rank=3,
            unlock=UnlockPack.Corruption
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        if isinstance(ctx.target, DMHero):
            blind = ctx.target.get_status("Blind")
            if blind is not None:
                ctx.target.add_status("Recharge", 2)

################################################################################
