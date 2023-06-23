from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities  import SpawnType

if TYPE_CHECKING:
    from dm.core.contexts   import EggHatchContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("AdvancedIncubator",)

################################################################################
class AdvancedIncubator(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-102",
            name="Advanced Incubator",
            description="A powerful monster appears from the next Monster Egg.",
            rank=1
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("egg_hatch", self.notify)

################################################################################
    def notify(self, ctx: EggHatchContext) -> None:

        # Brute force three high level monsters in as the new result.
        ctx.set_options(
            self.game.spawn(  # type: ignore
                spawn_type=SpawnType.Monster,
                start_rank=6,
                end_rank=7,
                weighted=False
            )(self.game, ctx._options[0].level),  # Just give them the same levels
            self.game.spawn(  # type: ignore
                spawn_type=SpawnType.Monster,
                start_rank=6,
                end_rank=7,
                weighted=False
            )(self.game, ctx._options[1].level),
            self.game.spawn(  # type: ignore
                spawn_type=SpawnType.Monster,
                start_rank=6,
                end_rank=7,
                weighted=False
            )(self.game, ctx._options[2].level)
        )

        # Only usable once, so unsubscribe to prevent future activations.
        self.game.unsubscribe_event("egg_hatch", self.notify)

################################################################################
