from __future__ import annotations

import random

from typing import TYPE_CHECKING

from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext, BossSkillContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("LastMarkOfAsceticism",)


################################################################################
class LastMarkOfAsceticism(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-322",
            name="Last Mark of Asceticism",
            description="Damage received by Dark Lord is reduced by 50 %.",
            rank=5,
            unlock=UnlockPack.Adventure
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        # If the Dark Lord is defending
        if ctx.target == self.game.dark_lord:
            # 50% damage reduction
            ctx.mitigate_pct(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.50

################################################################################
