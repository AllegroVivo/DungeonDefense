from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.hero import DMHero
from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Spore",)

################################################################################
class Spore(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="DBF-126",
            name="Spore",
            description=(
                "At the time of death, applies 10% of Poison stacks per Spore "
                "stack as damage to nearby enemies."
            ),
            stacks=stacks,
            status_type=DMStatusType.Debuff
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically upon the status's acquisition by the unit."""

        self.game.subscribe_event("on_death", self.notify)

################################################################################
    def notify(self, ctx: AttackContext) -> None:
        """A general event response function."""

        if self.owner == ctx.target:
            if isinstance(self.owner, DMHero):
                units = self.owner.room.heroes
            else:
                units = self.owner.room.monsters

            for unit in units:
                unit.damage(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect.

        Breakdown:
        ----------
        **effect = (p * b) + s**

        In this function:

        - s is the number of Spore stacks.
        - b is the base effectiveness per Spore stack
        - p is the number of Poison stacks.
        """

        poison = self.owner.get_status("Poison")
        if poison is None:
            return 0

        return (poison.stacks * 0.10) * self.stacks

################################################################################
