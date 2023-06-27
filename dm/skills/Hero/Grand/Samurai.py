from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from dm.core.objects.monster import DMMonster
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Samurai",)

################################################################################
class Samurai(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-358",
            name="Samurai",
            description=(
                "When attacking enemy, apply additional damage as much as "
                "50 % of target's current LIFE at 20 % chance."
            ),
            rank=5,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're attacking
        if self.owner == ctx.source:
            # If we're attacking a monster
            if isinstance(ctx.target, DMMonster):
                # Apply additional damage at 20 % chance
                if self.random.chance(20):
                    ctx.amplify_pct(0.50 * ctx.target.life)

################################################################################
