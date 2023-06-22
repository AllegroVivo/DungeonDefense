from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import BossSkillContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("VampireRune",)

################################################################################
class VampireRune(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-212",
            name="Vampire Rune",
            description="'Boss Skill : Vampiric Impulse' grants 1 extra Focus.",
            rank=3
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("boss_skill_vampiric_impulse")

################################################################################
    def notify(self, ctx: BossSkillContext) -> None:
        """A general event response function."""

        # If Focus is attached to the context.
        focus = ctx.get_status("Focus")
        if focus is not None:  # Shouldn't be None since it's linked directly to the skill.
            focus.increase_stacks_flat(1)

################################################################################
