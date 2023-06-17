from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import BossSkillContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("VampireAxe",)

################################################################################
class VampireAxe(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-210",
            name="Vampire Axe",
            description=(
                "Grants 20(+1.0 added per Dark Lord Lv.) Vampire to all monsters "
                "when defeating an enemy with a Boss Skill."
            ),
            rank=3
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        # Might need to change this to `on_death` instead, but I don't have
        # a way to track Boss Skills in that event yet.
        self.game.subscribe_event("boss_skill_used", self.notify)

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect.

        Breakdown:
        ----------
        **effect = b + (e * l)**

        In this function:

        - b is the base adjustment.
        - e is the additional effectiveness per level.
        - l is the Dark Lord's level.
        """

        return 20.0 + (1.0 * self.game.dark_lord.level)

################################################################################
    def notify(self, ctx: BossSkillContext) -> None:
        """A general event response function."""

        ctx.register_after_execute(self.activate)

################################################################################
    def activate(self, ctx: BossSkillContext) -> None:

        # If we've killed the defender...
        if not ctx.defender.is_alive:
            # Add Vampire to all monsters.
            for monster in self.game.deployed_monsters:
                monster.add_status("Vampire", self.effect_value())

################################################################################
