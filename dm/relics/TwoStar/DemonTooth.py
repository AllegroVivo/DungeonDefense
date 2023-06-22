from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import BossSkillContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("DemonTooth",)

################################################################################
class DemonTooth(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-142",
            name="Demon Tooth",
            description=(
                "Increases Vampire given to the Dark Lord from 'Boss Skill : Bite' "
                "by 1(+0.2 added per Dark Lord Lv.)"
            ),
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("boss_skill_bite")

################################################################################
    def effect_value(self) -> float:
        """The value of the effect corresponding to this relic."""

        return 1 + (0.20 * self.game.dark_lord.level)

################################################################################
    def notify(self, ctx: BossSkillContext) -> None:
        """A general event response function."""

        ctx.register_after_execute(self.after_skill)

################################################################################
    def after_skill(self, ctx: BossSkillContext) -> None:

        for status in ctx.statuses:
            if status.name == "Vampire":
                status.increase_stacks_flat(int(self.effect_value()))

################################################################################
