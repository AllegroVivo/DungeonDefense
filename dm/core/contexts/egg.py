from __future__ import annotations

import random

from typing     import TYPE_CHECKING, List

from .context  import Context
from utilities import DMSpawnType

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.monster import DMMonster
################################################################################

__all__ = ("EggHatchContext",)

################################################################################
class EggHatchContext(Context):

    __slots__ = (
        "_options",
    )

################################################################################
    def __init__(self, state: DMGame, num_monsters: int = 3):

        super().__init__(state)

        self._options: List[DMMonster] = []
        self._init_options(num_monsters)

################################################################################
    def _init_options(self, num_monsters: int) -> None:

        self._options = [
            self._state.spawn(spawn_type=DMSpawnType.Monster)
        ] * num_monsters

################################################################################
    def _calculate_experience(self) -> int:

        day = self._state.day
        base_exp = (5 * day.normal_battles) + (10 * day.elite_battles)

        return total_exp

################################################################################
    @property
    def options(self) -> List[DMMonster]:

        return self._options

################################################################################
    def set_options(self, *options: DMMonster) -> None:

        self._options = [m for m in options]

################################################################################
    def execute(self) -> None:

        for m in self._options:
            self._state.inventory.add_monster(m)

################################################################################
