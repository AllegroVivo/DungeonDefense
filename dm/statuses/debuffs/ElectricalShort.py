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
            status_type=DMStatusType.Debuff
        )

        self._shock: int = 0

################################################################################
    def on_acquire(self) -> None:
        """Called automatically upon the status's acquisition by the unit."""

        self.game.subscribe_event("on_death", self.notify)

################################################################################
    def notify(self, ctx: AttackContext) -> None:
        """A general event response function."""

        # If owner was the one killed
        if self.owner == ctx.defender:
            # Check for presence of Shock
            shock = self.owner.get_status("Shock")
            if shock is not None:
                # Set the attribute we need for the effect value.
                self._shock = shock.stacks

                # Get proper units depending on type.
                if isinstance(self.owner, DMHero):
                    units = self.owner.room.heroes
                else:
                    units = self.owner.room.monsters  # type: ignore

                # Damage each unit in the group.
                for unit in units:
                    unit.damage(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect.

        Breakdown:
        ----------
        **effect = a * n**

        In this function:

        - n is the number of Shock stacks possessed at death.
        - a is the effectiveness per stack.
        """

        return 0.10 * self._shock

################################################################################
