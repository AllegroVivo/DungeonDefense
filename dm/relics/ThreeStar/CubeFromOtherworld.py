from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("CubeFromOtherworld",)

################################################################################
class CubeFromOtherworld(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-228",
            name="Cube from Otherworld",
            description=(
                "Gives 5 Elasticity to all monsters at the beginning of the battle."
            ),
            rank=3,
            unlock=UnlockPack.Advanced
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("battle_start")

################################################################################
    def notify(self) -> None:
        """A general event response function."""

        for monster in self.game.deployed_monsters:
            monster.add_status("Elasticity", 5, self)

################################################################################
