from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("FireDance",)

################################################################################
class FireDance(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-257",
            name="Fire Dance",
            description=(
                "Inflict 7 (+1.5*ATK) damage and apply 6 (+0.35*ATK) Burn "
                "to the attacker."
            ),
            rank=5,
            cooldown=CooldownType.Passive,
            passive=True,
            effect=SkillEffect(base=7, scalar=1.5)
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            ctx.source.damage(self.effect)
            ctx.source.add_status("Burn", 6 + (0.35 * self.owner.attack), self)

################################################################################
