from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Executioner",)

################################################################################
class Executioner(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-153",
            name="Executioner",
            description=(
                "Damage inflicted is doubled if target's LIFE is below 50%."
            ),
            rank=4,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        if self.owner == ctx.source:
            if ctx.target.life <= ctx.target.max_life / 2:
                ctx.amplify_pct(1.00)  # Additional 100% damage

################################################################################
