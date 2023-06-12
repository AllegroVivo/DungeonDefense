from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom   import DMBattleRoom

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("Template",)

################################################################################
class Template(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-000",
            name="Template",
            description="",
            level=level,
            rank=0
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("", self.notify)

################################################################################
    def notify(self, **kwargs) -> None:

        pass

################################################################################
    def effect_value(self) -> int:

        pass

################################################################################
