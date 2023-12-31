from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("CurseOfTheSkull",)

################################################################################
class CurseOfTheSkull(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-108",
            name="Curse of the Skull",
            description=(
                "Grants 1 Curse to all heroes in the dungeon when a hero invades "
                "the Dark Lord's Room."
            ),
            rank=1
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("boss_room_entered")

################################################################################
    def notify(self, unit: DMUnit) -> None:

        for hero in self.game.all_heroes:
            hero.add_status("Curse", 1, self)

################################################################################
