from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.contexts import BossSkillContext
################################################################################

__all__ = ("ArmorOfPower",)

################################################################################
class ArmorOfPower(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-135",
            name="Armor of Power",
            description="Gives extra 1 Hatred when 'Boss Skill : Climax' is given.",
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("boss_skill_climax")

################################################################################
    def notify(self, ctx: BossSkillContext) -> None:

        pass
        # # (Basically)
        # ctx.register_after_execute(self.add_hatred)

################################################################################
