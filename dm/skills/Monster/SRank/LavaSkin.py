from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("LavaSkin",)

################################################################################
class LavaSkin(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-259",
            name="Lava Skin",
            description=(
                "Damage received is reduced by 40 %. Also, apply 8 (+0.4*ATK) "
                "to the attacker."
            ),
            rank=5,
            cooldown=CooldownType.Passive,
            passive=True
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            ctx.amplify_pct(0.40)
            ctx.source.damage(8 + (0.4 * self.owner.attack))

################################################################################
