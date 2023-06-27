from __future__ import annotations

from typing     import TYPE_CHECKING

from .adjustable  import AdjustableContext

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.room import DMRoom
################################################################################

__all__ = ("SoulAcquiredContext",)

################################################################################
class SoulAcquiredContext(AdjustableContext):

    def __init__(self, state: DMGame, base_amt: int):

        super().__init__(state, base_amt)

################################################################################
    @property
    def room(self) -> DMRoom:

        # Maybe?
        return self.game.dungeon.map.boss_tile

################################################################################
    def execute(self) -> None:

        self._state.inventory.add_soul(self.calculate())

################################################################################
