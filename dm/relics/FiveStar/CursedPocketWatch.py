from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.monster import DMMonster
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.contexts import StatusExecutionContext
################################################################################

__all__ = ("CursedPocketWatch",)

################################################################################
class CursedPocketWatch(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-312",
            name="Cursed Pocket Watch",
            description=(
                "The effect of Acceleration increases to 250 %. Acceleration "
                "that heroes get is reduced to 40 %."
            ),
            rank=5,
            unlock=UnlockPack.Adventure
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("status_applied")

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 2.00  # 200% *additional* effectiveness

################################################################################
    def notify(self, ctx: StatusExecutionContext) -> None:
        """A general event response function."""

        if ctx.status.name == "Acceleration":
            if isinstance(ctx.target, DMMonster):
                ctx.status.increase_base_effect(self.effect_value())
            else:
                ctx.status.reduce_base_effect(0.10)

################################################################################
