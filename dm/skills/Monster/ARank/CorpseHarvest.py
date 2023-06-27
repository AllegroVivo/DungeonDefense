from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("CorpseHarvest",)

################################################################################
class CorpseHarvest(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-238",
            name="Corpse Harvest",
            description=(
                "Gain 2 Immortality every time a unit dies in this room."
            ),
            rank=4,
            cooldown=CooldownType.Passive,
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_death")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if ctx.room == self.room:
            self.owner.add_status("Immortality", 2, self)

################################################################################
