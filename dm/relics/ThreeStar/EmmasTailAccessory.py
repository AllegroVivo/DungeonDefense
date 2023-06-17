from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("EmmasTailAccessory",)

################################################################################
class EmmasTailAccessory(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-219",
            name="Emma's Tail Accessory",
            description=(
                "Inflicting damage to the enemy in Vulnerable state with "
                "'Boss Skill : Split' will increase generation of Fury to 200 %."
            ),
            rank=3,
            unlock=UnlockPack.Original
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("boss_skill_split", self.notify)

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        pass

################################################################################
    def notify(self, *args) -> None:
        """A general event response function."""

        # Need to implement skills first. :(
        pass

################################################################################
