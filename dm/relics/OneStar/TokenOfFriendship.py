from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from ...core.objects.monster import DMMonster

if TYPE_CHECKING:
    from dm.core.contexts   import ExperienceContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("TokenOfFriendship",)

################################################################################
class TokenOfFriendship(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-123",
            name="Token Of Friendship",
            description="Increases EXP acquired from battle by 10 %.",
            rank=1
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("exp_awarded")

################################################################################
    def notify(self, ctx: ExperienceContext) -> None:
        """A general event response function."""

        # Since we can get experience from multiple sources, we need to check
        # that the source is a monster.
        if isinstance(ctx.object, DMMonster):
            # Increase experience
            ctx.amplify_pct(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.10

################################################################################
