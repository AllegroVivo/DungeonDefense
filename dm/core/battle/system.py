from __future__ import annotations

from pygame     import Surface
from typing     import TYPE_CHECKING, List

from .encounter import DMEncounter
from utilities  import DMFateType

if TYPE_CHECKING:
    from dm.core    import DMFighter, DMGame, DMHero
################################################################################

__all__ = ("DMBattleManager", )

################################################################################
class DMBattleManager:

    __slots__ = (
        "_state",
        "_status",
        "_type",
        "_encounters",
        "_spawn_interval",
        "_spawn_elapsed",
    )

################################################################################
    def __init__(self, state: DMGame):

        self._state: DMGame = state

        self._type: DMFateType = None  # type: ignore
        self._encounters: List[DMEncounter] = []

        self._spawn_interval: float = 2.0
        self._spawn_elapsed: float = 0

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

        # Before battle event fires
        self.game.dispatch_event("stat_calculation")
        self.game.dispatch_event("before_battle")

        # Check for battle over

        self.game.dungeon.update(dt)

        # Auto spawns a hero at the entrance tile after the appropriate
        # amount of time has passed.
        self.hero_spawn_check(dt)

        # Update Heroes (movement)
        for hero in self.heroes:
            hero.update(dt)

        # Update Monsters (No reason yet)
        for monster in self.game.dungeon.deployed_monsters:
            monster.update(dt)

        # Run encounters
        for encounter in self._encounters:
            encounter.run_turn()

        # After battle event fires
        self.game.dispatch_event("after_battle")
        self.game.dispatch_event("stats_reset")

################################################################################
    def draw(self, screen: Surface) -> None:

        # Draw dungeon (including monsters)
        self.game.dungeon.draw(screen)

        # Draw heroes
        for hero in self.heroes:
            hero.draw(screen)

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
    def hero_spawn_check(self, dt: float) -> None:

        # Update elapsed_spawn_time with the time passed since the last frame
        self._spawn_elapsed += dt

        # Check if it's time to spawn a new hero
        if self._spawn_elapsed > self._spawn_interval:
            self.game.dungeon.spawn_hero()
            self._spawn_elapsed = 0

################################################################################
    def engage(self, attacker: DMFighter, defender: DMFighter) -> None:

        self._encounters.append(DMEncounter(self.game, attacker, defender))

################################################################################
