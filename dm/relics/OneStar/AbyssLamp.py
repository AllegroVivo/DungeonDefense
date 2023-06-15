from __future__ import annotations

from typing     import TYPE_CHECKING
from ..core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("AbyssLamp",)

################################################################################
class AbyssLamp(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-101",
            name="Abyss Lamp",
            description=(
                "Has a 10 % chance to attack an enemy, even in Blind status."
            ),
            rank=1
        )

        # I'm fairly sure this is supposed to be "ally" not "enemy". Otherwise
        # I have no idea what it could mean.

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        pass

################################################################################
    def activate(self) -> None:
        """A preset function for autocomplete convenience that doesn't require
        any arguments to execute."""

        pass

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        pass

################################################################################
    def effect_value(self) -> float:
        """The value of the effect corresponding to this relic."""

        pass

################################################################################
