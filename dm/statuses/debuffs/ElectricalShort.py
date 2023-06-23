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

__all__ = ("ElectricalShort",)

################################################################################
class ElectricalShort(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="DBF-112",
            name="Electrical Short",
            description=(
                "When killed, inflicts damage equal to 10% of Shock possessed "
                "per Electrical Short to nearby allies."  # Originally said "enemies".
            ),
            stacks=stacks,
            status_type=StatusType.Debuff,
            base_effect=0.10
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically upon the status's acquisition by the unit."""

        self.game.subscribe_event("on_death", self.notify)

################################################################################
    def notify(self, ctx: AttackContext) -> None:
        """A general event response function."""

        # If owner was the one killed
        if self.owner == ctx.target:
            # Get proper units depending on type.
            if isinstance(self.owner, DMHero):
                units = self.owner.room.heroes
            else:
                units = self.owner.room.monsters  # type: ignore

            # Damage each unit in the group.
            for unit in units:
                unit.damage(self.effect_value())

################################################################################
    @property
    def base_effect(self) -> float:

        # Check for presence of Shock
        shock = self.owner.get_status("Shock")
        if shock is None:
            return 0

        return (self._base_effect * self._base_scalar) * shock.stacks

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect.

        Breakdown:
        ----------
        **effect = b * s**

        In this function:

        - b is the base adjustment.
        - s is the number of Electrical Short stacks.
        """

        return self.base_effect * self.stacks

################################################################################
