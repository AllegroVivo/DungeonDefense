from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import TortureContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("SkilledTorturer",)

################################################################################
class SkilledTorturer(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-140",
            name="Skilled Torturer",
            description=(
                "Time required for Torture is reduced by 1D."
            ),
            rank=2,
            cooldown=0,
            passive=True
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("torture_start")

################################################################################
    def notify(self, ctx: TortureContext) -> None:

        ctx.reduce_flat(1)

################################################################################
