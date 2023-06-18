from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("ElixirOfImmortality",)

################################################################################
class ElixirOfImmortality(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-218",
            name="Elixir of Immortality",
            description=(
                "Gives 3 Immortality to all monsters at the beginning of battle."
            ),
            rank=3,
            unlock=UnlockPack.Original
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("battle_start", self.notify)

################################################################################
    def notify(self) -> None:
        """A general event response function."""

        for monster in self.game.deployed_monsters:
            monster.add_status("Immortality", 3)

################################################################################
