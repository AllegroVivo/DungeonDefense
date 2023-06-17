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

__all__ = ("LivingBomb",)

################################################################################
class LivingBomb(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="DBF-116",
            name="Living Bomb",
            description=(
                "Upon receiving the next damage, cause explosion and inflict "
                "damage to allies in nearby area as much as current Burn stat."
            ),
            stacks=stacks,
            status_type=DMStatusType.Debuff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every battle loop iteration."""

        ctx.register_after_execute(self.notify)

################################################################################
    def notify(self, ctx: AttackContext) -> None:
        """A general event response function."""

        # If we're defending
        if self.owner == ctx.defender:
            # And receiving damage
            if ctx.damage > 0:
                # Check for Burn status
                burn = self.owner.get_status("Burn")
                if burn is None:
                    return

                # Get appropriate unit group for owner's type.
                if isinstance(self.owner, DMHero):
                    units = self.owner.room.heroes
                else:
                    units = self.owner.room.monsters

                # Apply damage
                for unit in units:
                    unit.damage(burn.stacks)

                # Reduce stacks upon execution
                self.reduce_stacks_by_one()

################################################################################
