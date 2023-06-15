from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Defense",)

################################################################################
class Defense(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-105",
            name="Defense",
            description=(
                "Damage received is decreased by 50%, and effect increases "
                "depending on the Defense possessed. Stat is halved when "
                "receiving damage."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

        self.damage: int = 0

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """For use in an AttackContext-based situation. Is always called in
        every battle loop."""

        if ctx.defender == self.owner:
            self.damage = ctx.damage
            print(f"effect value: {self.effect_value()}")
            ctx.mitigate_pct(self.effect_value())
            self.reduce_stacks_by_half()

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect.

        Breakdown:
        ----------
        **% = (n * a) + x**

        In this function:

        - x is the base effectiveness
        - n is the number of Defense stacks.
        - a is the additional effectiveness per stack.
        """

        ret = (self.stacks * 0.001) + 0.50
        self.damage = None

        return ret

################################################################################
