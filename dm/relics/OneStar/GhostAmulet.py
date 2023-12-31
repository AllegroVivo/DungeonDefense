from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.monster import DMMonster
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("GhostAmulet",)

################################################################################
class GhostAmulet(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-111",
            name="Ghost Amulet",
            description="Grants 3 Panic to a hero who killed a monster.",
            rank=1
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("on_death")

################################################################################
    def notify(self, ctx: AttackContext) -> None:
        """A general event response function."""

        if isinstance(ctx.source, DMHero):
            if isinstance(ctx.target, DMMonster):
                ctx.source.add_status("Panic", 3, self)

################################################################################
