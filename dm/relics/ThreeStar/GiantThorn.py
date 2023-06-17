from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.status import DMStatus
################################################################################

__all__ = ("GiantThorn",)

################################################################################
class GiantThorn(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-195",
            name="Giant Thorn",
            description="The damage from Thorn targets all the enemies in the room.",
            rank=3
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("status_execute", self.notify)

################################################################################
    def notify(self, status: DMStatus) -> None:
        """A general event response function."""

        # If we have a valid Thorn status
        if status.name == "Thorn":
            # If the owner is a hero
            if isinstance(status.owner, DMHero):
                if status.stacks > 0:
                    # Get all the heroes in the room
                    targets = self.game.dungeon.get_heroes_by_room(status.owner.room.position)
                    # Remove the status owner because they're going to be damaged already.
                    targets.remove(status.owner)  # type: ignore
                    # Apply the damage to all the targets
                    for hero in targets:
                        hero.damage(status.stacks)

################################################################################
