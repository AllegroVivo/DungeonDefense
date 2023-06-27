from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from dm.core.objects.hero import DMHero
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("BindingCurse",)

################################################################################
class BindingCurse(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-312",
            name="Binding Curse",
            description=(
                "Rigidity, Stun, Chained stats applied to the enemy increases "
                "by 1. Also, damage to immobilized enemy increases by 100 %."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_applied")

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:

        if isinstance(ctx.target, DMHero):
            if ctx.status.name in ("Rigidity", "Stun", "Chained"):
                ctx.increase_stacks_flat(1)

################################################################################
