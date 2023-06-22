from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic
from ...rooms.traproom import DMTrapRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("CrudeCube",)

################################################################################
class CrudeCube(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-302",
            name="Crude Cube",
            description="Enemies will receive 30 % more damage from traps.",
            rank=5,
            unlock=UnlockPack.Adventure
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        if isinstance(ctx.source, DMTrapRoom):
            if isinstance(ctx.target, DMHero):
                ctx.amplify_pct(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.30

################################################################################
