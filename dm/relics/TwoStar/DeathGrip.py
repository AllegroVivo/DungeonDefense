from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.core.objects.monster import DMMonster
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("DeathGrip",)

################################################################################
class DeathGrip(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-139",
            name="Death Grip",
            description="Recover 1 Empty Mana Crystal every time a monster dies.",
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("on_death", self.notify)

################################################################################
    def notify(self, ctx: AttackContext) -> None:
        """A general event response function."""

        # If a monster was the defender
        if isinstance(ctx.defender, DMMonster):
            # Restore mana
            self.game.dark_lord.restore_mana(1)

################################################################################
