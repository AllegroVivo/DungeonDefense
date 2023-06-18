from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import BossSkillContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("FairyWings",)

################################################################################
class FairyWings(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-278",
            name="Fairy Wings",
            description=(
                "Reduce the cost of all Dark Lord abilities by 1 to a "
                "minimum of 1."
            ),
            rank=4,
            unlock=UnlockPack.Corruption
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("boss_skill_used", self.notify)

################################################################################
    def notify(self, ctx: BossSkillContext) -> None:
        """A general event response function."""

        ctx.reduce_mana_cost(1)

################################################################################
