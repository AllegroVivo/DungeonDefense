from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("VampireRune",)

################################################################################
class VampireRune(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-212",
            name="Vampire Rune",
            description="'Boss Skill : Vampiric Impulse' grants 1 extra Focus.",
            rank=3
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("boss_skill_vampiric_impulse", self.notify)

################################################################################
    def notify(self, *args) -> None:
        """A general event response function."""

        # Need to implement boss skills first I think.
        pass

################################################################################
