from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("SmallDemonStatue",)

################################################################################
class SmallDemonStatue(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-276",
            name="Small Demon Statue",
            description=(
                "Apply 1 Frostbite to each enemy that enters the Dark Lord's room."
            ),
            rank=4,
            unlock=UnlockPack.Advanced
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("boss_room_entered")

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        if isinstance(unit, DMHero):
            unit.add_status("Frostbite", 1, self)

################################################################################
