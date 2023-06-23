from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.monster import DMMonster
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("TeardrinkerSword",)

################################################################################
class TeardrinkerSword(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-298",
            name="Teardrinker Sword",
            description=(
                "Whenever a monster dies, 5 Hatred is given to the Dark Lord."
            ),
            rank=5
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("on_death")

################################################################################
    def notify(self, ctx: AttackContext) -> None:
        """A general event response function."""

        if isinstance(ctx.target, DMMonster):
            self.game.dark_lord.add_status("Hatred", 5, self)

################################################################################
