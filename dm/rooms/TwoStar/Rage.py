from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from ...core.contexts   import ExperienceContext
from ..battleroom       import DMBattleRoom

if TYPE_CHECKING:
    from dm.core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("Rage",)

################################################################################
class Rage(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-109",
            name="Rage",
            description=(
                "Gives 2 (+2 per Lv.) Acceleration to deployed monsters whenever a "
                "hero enters."
            ),
            level=level,
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("on_room_change", self.notify)

################################################################################
    def notify(self, **kwargs) -> None:

        ctx: RoomChangeContext = kwargs.get("ctx")
        if ctx.target_room == self:
            for monster in self.monsters:
                monster += self.game.spawn("Acceleration", stacks=self.effect_value())

################################################################################
    def effect_value(self) -> int:

        return 3 + (1 * self.level)

################################################################################
