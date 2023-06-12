from __future__ import annotations

from pygame     import Surface
from typing     import TYPE_CHECKING, List

from utilities  import DMFateType

if TYPE_CHECKING:
    from dm.core    import DMGame, DMHero
################################################################################

__all__ = ("DMBattleManager", )

################################################################################
class DMBattleManager:

    __slots__ = (
        "_state",
        "_status",
        "_type",
        "_encounters"
    )

################################################################################
    def __init__(self, state: DMGame):

        self._state: DMGame = state

        self._type: DMFateType = None  # type: ignore
        self._encounters: List[DMEncounter] = []

################################################################################
    @property
    def game(self) -> DMGame:

        return self._state

################################################################################
    @property
    def heroes(self) -> List[DMHero]:

        return self.game.dungeon.heroes

################################################################################
    def update(self, dt: float) -> None:

        pass

################################################################################
    def draw(self, screen: Surface) -> None:

        pass

################################################################################
    def start_normal_battle(self) -> None:

        self._type = DMFateType.Battle

################################################################################
    def start_elite_battle(self) -> None:

        self._type = DMFateType.Elite

################################################################################
    def start_invade_battle(self) -> None:

        self._type = DMFateType.Invade

################################################################################
    def start_boss_battle(self) -> None:

        self._type = DMFateType.Boss

################################################################################
    def battle_loop(self) -> None:

        # Before battle event fires

        while any(hero.is_alive for hero in self.game.dungeon.heroes):


################################################################################
