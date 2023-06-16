from __future__ import annotations

import random

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("AbyssLamp",)

################################################################################
class AbyssLamp(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-101",
            name="Abyss Lamp",
            # description=(  # Original
            #     "Has a 10 % chance to attack an enemy, even in Blind status."
            # ),

            # I reworded this because the original version was unclear.
            # I'm fairly sure it was supposed to be "ally" not "enemy".
            description=(
                "Enemies have a 10 % chance to attack another enemy, even if "
                "under the effect of Blind."
            ),
            rank=1
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        # If a hero is attacking
        if isinstance(ctx.attacker, DMHero):
            # 10% chance to activate
            chance = random.random()
            if chance <= 0.10:
                # Reassign the target to another hero in the same room.
                ctx._defender = random.choice(
                    self.game.dungeon.get_heroes_by_room(ctx.attacker.room.position)
                )

################################################################################
