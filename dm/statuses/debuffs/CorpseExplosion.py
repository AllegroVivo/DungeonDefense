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

__all__ = ("CorpseExplosion",)

################################################################################
class CorpseExplosion(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="DBF-107",
            name="Corpse Explosion",
            description=(
                "If killed while in Corpse Explosion state, inflicts damage equal "
                "to number of Corpse Explosion stacks possessed to nearby allies."
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

        # If the status owner was the one killed
        if self.owner == ctx.target:
            # Get units based on owner type
            if isinstance(self.owner, DMHero):
                units = self.game.dungeon.get_heroes_by_room(self.owner.room.position)
            else:
                units = self.game.dungeon.get_monsters_by_room(self.owner.room.position)

            # Then damage each unit in the group.
            for unit in units:
                unit.damage(self.stacks)

################################################################################
