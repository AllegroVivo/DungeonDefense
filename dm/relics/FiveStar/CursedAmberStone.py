from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import EXPSource

if TYPE_CHECKING:
    from dm.core.contexts   import ExperienceContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("CursedAmberStone",)

################################################################################
class CursedAmberStone(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-287",
            name="Cursed Amber Stone",
            description=(
                "Increases EXP acquired from battle by 10 %. However, more "
                "heroes will come to the dungeon."
            ),
            rank=5
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("exp_awarded")
        self.game.battle_mgr.increase_hero_count_pct(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.10

################################################################################
    def notify(self, ctx: ExperienceContext) -> None:
        """A general event response function."""

        if ctx.source == EXPSource.Battle:
            ctx.amplify_pct(self.effect_value())

################################################################################
