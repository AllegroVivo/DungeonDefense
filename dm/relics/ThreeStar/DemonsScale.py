from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import BossSkillContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("DemonsScale",)

################################################################################
class DemonsScale(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-231",
            name="Demon's Scale",
            description=(
                "'Boss Skill : Harvest' gives 3 Elasticity to all monsters."
            ),
            rank=3,
            unlock=UnlockPack.Advanced
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("boss_skill_harvest", self.notify)

################################################################################
    def notify(self, *args) -> None:
        """A general event response function."""

        for monster in self.game.deployed_monsters:
            monster.add_status("Elasticity", 3)

################################################################################
