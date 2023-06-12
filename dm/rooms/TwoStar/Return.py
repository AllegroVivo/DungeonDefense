from __future__ import annotations

from typing     import TYPE_CHECKING

from ..traproom import DMTrapRoom

if TYPE_CHECKING:
    from ...core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("Return",)

################################################################################
class Return(DMTrapRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="TRP-113",
            name="Return",
            description=(
                "The 3rd enemy is returned to the dungeon entrance. The number "
                "of entries required for operation increases with each activation. "
                "It works up to 3 (+1 per Lv) times."
            ),
            level=level,
            rank=2
        )

        self._enemy_counter = 0
        self._use_counter = 0

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("on_room_enter", self.notify)
        self.game.subscribe_event("after_battle", self.after_battle)

################################################################################
    def notify(self, **kwargs) -> None:

        ctx: RoomChangeContext = kwargs.get("ctx")
        if ctx.target_room == self:
            if self._use_counter < self.effect_value():
                self._enemy_counter += 1
                if self._enemy_counter >= 3:
                    # Reset unit position to entrance and increment uses.
                    self._use_counter += 1

################################################################################
    def effect_value(self) -> int:

        return 3 + (1 * self.level)

################################################################################
    def after_battle(self) -> None:

        self._enemy_counter = 0
        self._use_counter = 0

################################################################################
