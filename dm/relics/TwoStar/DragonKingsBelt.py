from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import RoomType, UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts import RoomChangeContext
    from dm.core.game.game import DMGame
    from dm.core.objects.hero import DMHero
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("DragonKingsBelt",)

################################################################################
class DragonKingsBelt(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-172",
            name="Dragon King's Belt",
            description=(
                "If a hero leaves a Battle Room without Dull, hero gets 1 Dull."
            ),
            rank=2,
            unlock=UnlockPack.Original
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("room_change")

################################################################################
    def notify(self, ctx: RoomChangeContext) -> None:

        # If the unit is a hero.
        if isinstance(ctx.unit, DMHero):
            # Since the unit is switching rooms, that means they just left
            # a room. So check if the room they just left was a Battle Room.
            if ctx.previous.room_type == RoomType.Battle:
                # If so, check for dull
                dull = ctx.unit.get_status("Dull")
                if dull is None:
                    # And add if not present.
                    ctx.unit.add_status("Dull", 1, self)

################################################################################
