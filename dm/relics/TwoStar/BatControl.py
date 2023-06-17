from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import BossSkillContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("BatControl",)

################################################################################
class BatControl(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-136",
            name="Bat Control",
            description=(
                "Reduces the cost of 'Boss Skill : Vampiric Impulse' by 1."
            ),
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("boss_skill_vampiric_impulse", self.notify)

################################################################################
    def notify(self, ctx: BossSkillContext) -> None:
        """A general event response function."""

        ctx.reduce_mana_cost(1)

################################################################################
