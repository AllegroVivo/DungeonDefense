from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import SoulAcquiredContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("SoulGrant",)

################################################################################
class SoulGrant(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-283",
            name="Soul Grant",
            description=(
                "Every time a Soul is acquired from altar's effect, apply 1 "
                "Hatred to all traps in the dungeon."
            ),
            rank=6,
            cooldown=CooldownType.Passive
        )

        # Shit, I haven't planned for traps being able to have statuses.
        # Will come back to this.

################################################################################
    def on_acquire(self) -> None:

        self.listen("soul_acquired")

################################################################################
    def notify(self, ctx: SoulAcquiredContext) -> None:

        # Add hatred
        pass

################################################################################
