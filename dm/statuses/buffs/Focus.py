from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Focus",)

################################################################################
class Focus(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-110",
            name="Focus",
            description=(
                "The next attack inflicts 50% extra damage, and effect increases "
                "depending on the Focus possessed. Stat is halved with each action."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff,
            base_effect=0.50
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every iteration of the battle loop."""

        # If we're attacking
        if self.owner == ctx.attacker:
            # Boost that damage
            ctx.amplify_pct(self.effect_value())
            # And reduce stacks
            self.reduce_stacks_by_half()

################################################################################
    @property
    def base_effect(self) -> float:

        # After much deliberation, I've decided that the scaled percentage should
        # be the base for the effectiveness increase below, so the scalar is
        # factored in here instead at at the time of return.
        base_effect = self._base_effect * self._scalar

        # Check for the associated relic
        relic = self.game.get_relic("Necklace of Focus")
        if relic is not None:
            base_effect *= 2  # Relic effect increases base effectiveness to 100%

        return base_effect

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect.

        Breakdown:
        ----------
        **effect = b + (e * s)**

        In this function:

        - b is the base adjustment.
        - e is the additional effectiveness per stack.
        - s is the number of Focus stacks.
        """

        return self.base_effect * (0.001 * self.stacks)  # 0.1% additional effectiveness

################################################################################
