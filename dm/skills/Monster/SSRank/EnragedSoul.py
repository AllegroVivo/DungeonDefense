from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import SoulAcquiredContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("EnragedSoul",)

################################################################################
class EnragedSoul(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-281",
            name="Enraged Soul",
            description=(
                "Every time a Soul is acquired from altar's effect, apply 1 "
                "Hatred to all monsters in the dungeon."
            ),
            rank=6,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("soul_acquired")

################################################################################
    def notify(self, ctx: SoulAcquiredContext) -> None:

        # if ctx.source == altar?
        for monster in self.game.all_monsters:
            monster.add_status("Hatred", 1, self)

################################################################################
