from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("GoddessBlessing",)

################################################################################
class GoddessBlessing(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-341",
            name="Goddess Blessing",
            description=(
                "Damage from the Dark Lord is reduced by 60 %."
            ),
            rank=5,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're being targeted
        if self.owner == ctx.target:
            # By the Dark Lord
            if ctx.source == self.game.dark_lord:
                # Mitigate damage
                ctx.mitigate_pct(0.60)

################################################################################
