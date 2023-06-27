from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import StatusType, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("DeadmanSword",)

################################################################################
class DeadmanSword(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-240",
            name="Deadman Sword",
            description=(
                "For each attack, inflict 15 % additional damage for each "
                "unique debuff on the target."
            ),
            rank=4,
            cooldown=CooldownType.Passive,
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        debuffs = [
            s for s in ctx.target.statuses
            if s._type in (StatusType.Debuff, StatusType.AntiBuff)
        ]
        ctx.target.damage(ctx.damage * (0.15 * len(debuffs)))

################################################################################
