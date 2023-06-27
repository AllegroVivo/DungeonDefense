from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from dm.core.objects.monster import DMMonster
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("LethalSeduction",)

################################################################################
class LethalSeduction(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-307",
            name="Lethal Seduction",
            description=(
                "A monster that inflicts damage to an enemy under Charm "
                "effect gets Pleasure as much as 100% of its ATK."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if isinstance(ctx.target, DMMonster):
            ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        if ctx.damage > 0:
            charm = ctx.target.get_status("Charm")
            if charm is not None:
                ctx.source.add_status("Pleasure", ctx.source.attack, self)

################################################################################
