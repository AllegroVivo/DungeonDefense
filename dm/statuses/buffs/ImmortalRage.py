from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("ImmortalRage",)

################################################################################
class ImmortalRage(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-115",
            name="Immortal Rage",
            description=(
                "The next attack deals 5% extra damage per Immortality stat "
                "possessed, with increasing effect depending on the Immortal Rage "
                "stat possessed. Stat is halved with each attack."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every iteration of the battle loop."""

        if self.owner == ctx.attacker:
            immortality = self.owner.get_status("Immortality")
            if immortality is not None:
                ctx.amplify_pct(self.effect_value())
                self.reduce_stacks_by_half()

################################################################################
    @property
    def base_effect(self) -> Optional[float]:

        return (self._base_effect * self._scalar) * (0.005 * self.stacks)  # 0.5% additional effectiveness

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect.

        Breakdown:
        ----------
        **effect = b * s**

        In this function:

        - b is the base adjustment.
        - s is the number of Immortality stacks.
        """

        immortality = self.owner.get_status("Immortality")
        if immortality is None:
            return 0

        return self.base_effect * immortality.stacks

################################################################################
