from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts import StatusExecutionContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Furball",)

################################################################################
class Furball(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-174",
            name="Furball",
            description=(
                "Give 1 Merciless to all monsters when 'Boss Skill : "
                "Fury Explosion' is used."
            ),
            rank=2,
            unlock=UnlockPack.Original
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("boss_skill_fury_explosion")

################################################################################
    def notify(self, ctx: StatusExecutionContext) -> None:
        """A general event response function."""

        for monster in self.game.deployed_monsters:
            monster.add_status("Merciless", 1, self)

################################################################################
