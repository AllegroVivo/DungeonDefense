from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import BossSkillContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("ObsidianFang",)

################################################################################
class ObsidianFang(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-157",
            name="Obsidian Fang",
            description=(
                "The cost of 'Boss Skill : Petrifying Gaze' is reduced by (2)."
            ),
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("boss_skill_petrifying_gaze")

################################################################################
    def notify(self, ctx: BossSkillContext) -> None:
        """A general event response function."""

        ctx.reduce_mana_cost(2)

################################################################################
