from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.monster import DMMonster
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Scorpion",)

################################################################################
class Scorpion(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-206",
            name="Scorpion",
            description=(
                "When a monster kills an enemy under the effect of Poison, get "
                "Regeneration as much as their Poison stacks."
            ),
            rank=3
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("on_death", self.notify)

################################################################################
    def notify(self, ctx: AttackContext) -> None:
        """A general event response function."""

        # If we've killed a hero
        if isinstance(ctx.target, DMHero):
            # And if a monster is the one attacking
            if isinstance(ctx.source, DMMonster):
                # Check if for Poison status
                poison = ctx.target.get_status("Poison")
                if poison is None:
                    return

                # If present, add Regeneration to the attacker
                ctx.source.add_status("Regeneration", poison.stacks)

################################################################################
