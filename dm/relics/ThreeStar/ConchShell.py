from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import BossSkillContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("ConchShell",)

################################################################################
class ConchShell(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-226",
            name="Conch Shell",
            description="'Boss Skill : Frost Arrow' gives 1 additional Frostbite.",
            rank=3,
            unlock=UnlockPack.Advanced
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("boss_skill_frost_arrow")

################################################################################
    def notify(self, ctx: BossSkillContext) -> None:
        """A general event response function."""

        # Need to implement boss skills first.
        pass

################################################################################
