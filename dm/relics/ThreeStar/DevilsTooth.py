from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import BossSkillContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("DevilsTooth",)

################################################################################
class DevilsTooth(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-191",
            name="Devil's Tooth",
            description=(
                "Increases the Dark Lord's ATK by 1(+0.1 per Dark Lord Lv.) "
                "if enemy is defeated using 'Boss Skill : Bite'."
            ),
            rank=3
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("boss_skill_bite", self.notify)

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect.

        Breakdown:
        ----------
        **effect = b + (e * l)**

        In this function:

        - b is the base adjustment.
        - e is the additional effectiveness per stack.
        - l is the Dark Lord's level.
        """

        return 1 + (0.1 * self.game.dark_lord.level)

################################################################################
    def notify(self, ctx: BossSkillContext) -> None:
        """A general event response function."""

        # If the defender is a hero
        if isinstance(ctx.defender, DMHero):
            # And the attack would kill the hero
            if ctx.would_kill():
                # Increase the Dark Lord's ATK
                self.game.dark_lord.increase_stat_flat("attack", int(self.effect_value()))

################################################################################
