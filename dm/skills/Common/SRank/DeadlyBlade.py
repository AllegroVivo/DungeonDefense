from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import SkillEffect, UnlockPack, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("DeadlyBlade",)

################################################################################
class DeadlyBlade(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-190",
            name="Deadly Blade",
            description=(
                "Apply 28 (+1*ATK) Poison to target upon inflicting damage."
            ),
            rank=4,
            cooldown=CooldownType.Passive,
            effect=SkillEffect(base=28, scalar=1),
            unlock=UnlockPack.Awakening
        )

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're attacking, wait for damage to be dealt
        if self.owner == ctx.source:
            ctx.register_post_execute(self.post_execute)

################################################################################
    def post_execute(self, ctx: AttackContext) -> None:

        # If damage is being applied
        if not ctx.will_fail:
            # Apply Poison as well
            ctx.target.add_status("Poison", self.effect, self)

################################################################################
