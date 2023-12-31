from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("AncientDictionaryPage",)

################################################################################
class AncientDictionaryPage(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-130",
            name="Ancient Dictionary Page",
            description=(
                "Unleash special powers by unlocking potential keyword of monsters."
            ),
            rank=1,
            unlock=UnlockPack.AncientDict
        )

        # Definitely too early to implement this.

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        pass

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        pass

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        pass

################################################################################
    def effect_value(self) -> float:
        """The value of the effect corresponding to this relic."""

        pass

################################################################################
    def notify(self, *args) -> None:
        """A general event response function."""

        pass

################################################################################
