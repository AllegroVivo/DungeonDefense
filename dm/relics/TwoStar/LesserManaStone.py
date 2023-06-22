from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("LesserManaStone",)

################################################################################
class LesserManaStone(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-150",
            name="Lesser Mana Stone",
            description="Recover 2 Empty Mana Crystal at the beginning of battle.",
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("battle_start")

################################################################################
    def notify(self) -> None:
        """A general event response function."""

        self.game.dark_lord.restore_mana(2)

################################################################################
