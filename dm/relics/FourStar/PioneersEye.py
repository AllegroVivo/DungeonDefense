from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("PioneersEye",)

################################################################################
class PioneersEye(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-280",
            name="Pioneer's Eye",
            description=(
                "At the start of the battle, Focus of 1 per book read is "
                "given to allies."
            ),
            rank=4,
            unlock=UnlockPack.Corruption
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("battle_start")

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
        """The value of this relic's effect.

        Breakdown:
        ----------
        **effect = e * b**

        In this function:

        - e is the effectiveness per bool.
        - b is the number of books read.
        """

        # num_books = len(self.game.books.obtained)
        num_books = 0
        return 1 * num_books

################################################################################
    def notify(self, *args) -> None:
        """A general event response function."""

        for monster in self.game.deployed_monsters:
            monster.add_status("Focus", self.effect_value())

################################################################################
