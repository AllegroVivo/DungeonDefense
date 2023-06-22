from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import BossSkillContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("DemonGlove",)

################################################################################
class DemonGlove(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-190",
            name="Demon Glove",
            description=(
                "The Dark Lord gets 1 Hatred for inflicting damage to enemies "
                "under the effect of Obey by using 'Boss Skill : Whip'."
            ),
            rank=3
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("boss_skill_whip")

################################################################################
    def notify(self, ctx: BossSkillContext) -> None:
        """A general event response function."""

        # If the defender is a hero
        if isinstance(ctx.target, DMHero):
            # Check if the defender has the Obey status
            obey = ctx.target.get_status("Obey")
            if obey is not None:
                # If so, add 1 Hatred to the Dark Lord
                self.game.dark_lord.add_status("Hatred", 1, self)

################################################################################
