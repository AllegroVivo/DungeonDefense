from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import BossSkillContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("SnakeBracelet",)

################################################################################
class SnakeBracelet(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-164",
            name="Snake Bracelet",
            description="The cost of 'Boss Skill : Snake Trap' is reduced by (1).",
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("boss_skill_snake_trap", self.notify)

################################################################################
    def notify(self, ctx: BossSkillContext) -> None:
        """A general event response function."""

        ctx.reduce_mana_cost(1)

################################################################################
