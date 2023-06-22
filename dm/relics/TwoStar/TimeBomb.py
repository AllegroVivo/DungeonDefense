from __future__ import annotations

import random

from typing     import TYPE_CHECKING

from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic
from ...rooms.traproom import DMTrapRoom

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("TimeBomb",)

################################################################################
class TimeBomb(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-168",
            name="Time Bomb",
            description=(
                "Has a small chance of increasing the damage area of a trap."
            ),
            rank=2
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        ctx.register_after_execute(self.after_attack)

################################################################################
    def after_attack(self, ctx: AttackContext) -> None:

        # If a Trap Room is attacking
        if isinstance(ctx.source, DMTrapRoom):
            # And a hero is defending
            if isinstance(ctx.target, DMHero):
                # There's a small chance (I'm going to say 10%)
                if self.random.chance(10):
                    # Get all the adjacent heroes:
                    rooms = self.game.dungeon.get_adjacent_rooms(ctx.target.room.position, include_current=True)
                    for room in rooms:
                        for hero in room.heroes:
                            hero.damage(ctx.damage)

################################################################################
