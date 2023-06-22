from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import BossSkillContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("StaffOfAuthority",)

################################################################################
class StaffOfAuthority(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-166",
            name="Staff of Authority",
            description="Reduces the cost of 'Boss Skill : Charm' by 1.",
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("boss_skill_charm")

################################################################################
    def notify(self, ctx: BossSkillContext) -> None:
        """A general event response function."""

        ctx.reduce_mana_cost(1)

################################################################################
