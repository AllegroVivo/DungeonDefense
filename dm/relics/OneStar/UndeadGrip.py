from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.monster import DMMonster
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("UndeadGrip",)

################################################################################
class UndeadGrip(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-124",
            name="Undead Grip",
            description="Get 2 Immortality when a monster kills an enemy.",
            rank=1
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("on_death", self.notify)

################################################################################
    def notify(self, ctx: AttackContext) -> None:
        """A general event response function."""

        # If a hero was killed
        if isinstance(ctx.defender, DMHero):
            # By a monster
            if isinstance(ctx.attacker, DMMonster):
                # Then assign all monsters the buff.
                for monster in self.game.deployed_monsters:
                    monster.add_status("Immortality", stacks=2)

################################################################################
