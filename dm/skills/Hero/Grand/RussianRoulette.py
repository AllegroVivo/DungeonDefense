from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("RussianRoulette",)

################################################################################
class RussianRoulette(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-354",
            name="Russian Roulette",
            description=(
                "The 7th attack deals 1,000 % damage."
            ),
            rank=5,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're attacking
        if self.owner == ctx.source:
            # If this is the 7th attack
            if self.atk_count % 7 == 0:
                # Apply additional damage
                ctx.amplify_pct(10.00)

################################################################################
