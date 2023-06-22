from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("GuardianJellyfish",)

################################################################################
class GuardianJellyfish(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-267",
            name="Guardian Jellyfish",
            description="Damage received by Dark Lord is reduced by 15 %.",
            rank=4,
            unlock=UnlockPack.Original
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        if self.game.dark_lord == ctx.target:
            ctx.mitigate_pct(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.15

################################################################################
