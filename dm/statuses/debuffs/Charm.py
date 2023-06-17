from __future__ import annotations

import random

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.hero import DMHero
from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Charm",)

################################################################################
class Charm(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="DBF-105",
            name="Charm",
            description=(
                "The next attack will target an ally. Stat decreases by 1 and "
                "you gain 1 Charm Resist per action."
            ),
            stacks=stacks,
            status_type=DMStatusType.Debuff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every battle loop iteration."""

        # If we're attacking
        if self.owner == ctx.attacker:
            # Check resist before executing the effect
            resist = self.owner.get_status("Charm Resist")
            if resist is not None:
                if resist >= self:
                    return

            # Reassign to a random ally in the same room.
            if isinstance(ctx.attacker, DMHero):
                options = self.game.dungeon.get_heroes_by_room(self.owner.room.position)
            else:
                options = self.game.dungeon.get_monsters_by_room(self.owner.room.position)
            ctx.reassign_defender(random.choice(options))

            # Reduce stacks and apply resist.
            self.reduce_stacks_by_one()
            self.owner.add_status("Charm Resist")

################################################################################
