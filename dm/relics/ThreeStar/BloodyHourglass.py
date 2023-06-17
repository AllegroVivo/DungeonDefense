from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("BloodyHourglass",)

################################################################################
class BloodyHourglass(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-225",
            name="Bloody Hourglass",
            description=(
                "Gives 2 Bloodlust to all monsters when 'Boss Skill : "
                "Hemokinesis' is used."
            ),
            rank=3,
            unlock=UnlockPack.Advanced
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("boss_skill_hemokinesis", self.notify)

################################################################################
    def notify(self, *args) -> None:
        """A general event response function."""

        for monster in self.game.deployed_monsters:
            monster.add_status("Bloodlust", 2)

################################################################################
