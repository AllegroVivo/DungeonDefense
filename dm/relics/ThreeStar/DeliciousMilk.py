from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import BossSkillContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("DeliciousMilk",)

################################################################################
class DeliciousMilk(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-216",
            name="Delicious Milk",
            description=(
                "Using 'Boss Skill : Rallying Cry' recovers all monsters' "
                "LIFE by 1 %."
            ),
            rank=3,
            unlock=UnlockPack.Original
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("boss_skill_rallying_cry")

################################################################################
    def notify(self, ctx: BossSkillContext) -> None:
        """A general event response function."""

        # Heal all monsters by 1% of their max life.
        for monster in self.game.deployed_monsters:
            monster.heal(monster.max_life * 0.01)

################################################################################
