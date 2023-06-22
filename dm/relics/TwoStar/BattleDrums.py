from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import RoomType

if TYPE_CHECKING:
    from dm.core.contexts   import RoomChangeContext
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

        self.listen("room_change")

################################################################################
    def notify(self, ctx: RoomChangeContext) -> None:

        if ctx.room.room_type == RoomType.Battle:
            # Add Fury to all monsters in the same room.
            for monster in ctx.room.monsters:
                monster.add_status("Fury", monster.attack * self.effect_value(), self)

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.10

################################################################################
