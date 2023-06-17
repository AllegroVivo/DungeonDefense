from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("BattleDrums",)

################################################################################
class BattleDrums(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-137",
            name="Battle Drums",
            description=(
                "All the monsters in the Battle Room gain Fury equal to 10 % "
                "of their ATK when a hero enters the Battle Room."
            ),
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("room_change", self.notify)

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        for monster in unit.room.monsters:
            monster.add_status("Fury", stacks=monster.attack * 0.10)

################################################################################
