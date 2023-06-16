from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import BossSkillContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("BloodyMeteorite",)

################################################################################
class BloodyMeteorite(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-105",
            name="Bloody Meteorite",
            description=(
                "The Dark Lord recovers LIFE equal to Vampire absorbed by "
                "'Boss Skill : Blood Lord'."
            ),
            rank=1
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("boss_skill_blood_lord", self.notify)

################################################################################
    def notify(self, ctx: BossSkillContext) -> None:
        """A general receptor function for any argument-emitting events."""

        # Need to implement specifics for the skill first I think.
        pass

################################################################################
