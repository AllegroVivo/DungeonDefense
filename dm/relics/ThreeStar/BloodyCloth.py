from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("BloodyCloth",)

################################################################################
class BloodyCloth(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-186",
            name="Bloody Cloth",
            description=(
                "The Dark Lord acquires Vampire equal to 50 % of missing LIFE "
                "at the start of the battle."
            ),
            rank=3
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("before_battle", self.notify)

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return (self.game.dark_lord.max_life - self.game.dark_lord.life) / 2

################################################################################
    def notify(self, *args) -> None:
        """A general event response function."""

        self.game.dark_lord.add_status("Vampire", self.effect_value())

################################################################################
