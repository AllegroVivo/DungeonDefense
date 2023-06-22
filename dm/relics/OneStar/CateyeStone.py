from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("CateyeStone",)

################################################################################
class CateyeStone(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-107",
            name="Cateye Stone",
            description=(
                "Inflicts damage to enemies as much as recovery canceled by Burn."
            ),
            rank=1
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("recovery_canceled_by_burn")

################################################################################
    def notify(self, amount: int) -> None:
        """A general event response function."""

        for hero in self.game.all_heroes:
            hero.damage(amount)

################################################################################
