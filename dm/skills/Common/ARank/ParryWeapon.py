from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ParryWeapon",)

################################################################################
class ParryWeapon(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-163",
            name="Parry Weapon",
            description=(
                "Gain 1 Defense when attacked."
            ),
            rank=4,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're being attacked
        if self.owner == ctx.target:
            # Add Defense.
            self.owner.add_status("Defense", 1, self)

################################################################################
