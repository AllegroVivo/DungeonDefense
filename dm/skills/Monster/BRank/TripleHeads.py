from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("TripleHeads",)

################################################################################
class TripleHeads(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-233",
            name="Triple Heads",
            description=(
                "Attacks target 2 more enemies. ATK decreases by 33 %."
            ),
            rank=3,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        options = self.room.units_of_type(self.owner, inverse=True)
        targets = self.random.sample(options, 2)
        for target in targets:
            ctx.register_additional_target(target)

################################################################################
    def stat_adjust(self) -> None:

        self.owner.reduce_stat_pct("ATK", 0.33)

################################################################################
