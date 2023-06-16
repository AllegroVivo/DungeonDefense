from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import BossSkillContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("DeadlySting",)

################################################################################
class DeadlySting(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-109",
            name="Deadly Sting",
            description=(
                "Recovers 1 Mana at 25 % chance upon killing an enemy with "
                "'Boss Skill : Venom Fang'."
            ),
            rank=1
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("boss_skill_venom_fang", self.notify)

################################################################################
    def notify(self, ctx: BossSkillContext) -> None:
        """A general receptor function for any argument-emitting events."""

        # Need to implement skill before I can implement this.
        pass

################################################################################
