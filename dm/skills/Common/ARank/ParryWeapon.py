from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

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
            rank=2,
            cooldown=0
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            self.owner.add_status("Defense", 1, self)

################################################################################
