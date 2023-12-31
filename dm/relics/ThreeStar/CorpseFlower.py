from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("CorpseFlower",)

################################################################################
class CorpseFlower(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-227",
            name="Corpse Flower",
            description=(
                "If an enemy under the effect of Corpse Explosion dies while also "
                "under the effect of Burn, deal damage to nearby enemies equal to "
                "50 % of remaining Burn stat."
            ),
            rank=3,
            unlock=UnlockPack.Advanced
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("on_death")

################################################################################
    def notify(self, ctx: AttackContext) -> None:
        """A general event response function."""

        # If a hero has been killed
        if isinstance(ctx.target, DMHero):
            # Check both required statuses
            c_expl = ctx.target.get_status("Corpse Explosion")
            burn = ctx.target.get_status("Burn")
            if c_expl is None or burn is None:
                return

            # If the check passes, deal damage to nearby enemies
            for hero in ctx.room.heroes:
                hero.damage(burn.stacks * 0.50)

################################################################################
