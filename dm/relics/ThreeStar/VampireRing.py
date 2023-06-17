from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import BossSkillContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("VampireRing",)

################################################################################
class VampireRing(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-211",
            name="Vampire Ring",
            description=(
                "The Dark Lord acquires 3(+0.3 added per Dark Lord Lv.) Vampire "
                "each time a Boss skill is used."
            ),
            rank=3
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

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

        return 3.0 + (0.3 * self.game.dark_lord.level)

################################################################################
    def notify(self, ctx: BossSkillContext) -> None:
        """A general event response function."""

        self.game.dark_lord.add_status("Vampire", self.effect_value())

################################################################################
