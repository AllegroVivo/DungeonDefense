from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ImmortalBeing",)

################################################################################
class ImmortalBeing(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-258",
            name="Immortal Being",
            description=(
                "Gain 5 Immortality at the beginning of the battle. Also, "
                "damage received from enemies in Panic decreases by 75%."
            ),
            rank=5,
            cooldown=CooldownType.Passive,
            passive=True
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("before_battle", self.before_battle)
        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            panic = ctx.source.get_status("Panic")
            if panic is not None:
                ctx.amplify_pct(0.25)

################################################################################
    def before_battle(self) -> None:

        self.owner.add_status("Immortality", 5, self)

################################################################################
