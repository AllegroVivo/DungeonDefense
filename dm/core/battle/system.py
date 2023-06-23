from __future__ import annotations

from pygame     import Surface
from typing     import TYPE_CHECKING, List

from .encounter import DMEncounter
from ..contexts import AttackContext
from utilities  import FateType, ArgumentTypeError

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.hero import DMHero
    from dm.core.objects.unit import DMUnit
    from ...rooms.traproom import DMTrapRoom
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
        "_hero_amt_base",
        "_hero_amt_additional",
        "_hero_amt_scalar",
        "_dragon_slayer_flag",
        "counter"
    )

################################################################################
    def __init__(self, state: DMGame):

        self._state: DMGame = state

        self._type: FateType = None  # type: ignore
        self._encounters: List[DMEncounter] = []

        self._spawn_interval: float = 2.0
        self._spawn_elapsed: float = 0

        self._hero_amt_base: int = 1
        self._hero_amt_additional: int = 1
        self._hero_amt_scalar: float = 1.0

        self._dragon_slayer_flag: bool = False

        self.counter = 20

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

        # self.counter += 1
        # if self.counter % 20 != 0:
        #     return
        # else:
        #     self.counter = 0

        # Before battle event fires
        self.game.dispatch_event("before_battle")

        # Check for battle over

        # Update dungeon components
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
            encounter.run_turn(dt)

        # After battle event fires
        self.game.dispatch_event("after_battle")
        self.game.dispatch_event("reset_stats")

################################################################################
    def draw(self, screen: Surface) -> None:

        # Draw dungeon (including monsters)
        self.game.dungeon.draw(screen)

        # Draw heroes
        for hero in self.heroes:
            hero.draw(screen)

################################################################################
    def start_normal_battle(self) -> None:

        self._type = FateType.Battle

################################################################################
    def start_elite_battle(self) -> None:

        self._type = FateType.Elite

################################################################################
    def start_invade_battle(self) -> None:

        self._type = FateType.Invade

################################################################################
    def start_boss_battle(self) -> None:

        self._type = FateType.Boss

################################################################################
    def hero_spawn_check(self, dt: float) -> None:

        # Update elapsed_spawn_time with the time passed since the last frame
        self._spawn_elapsed += dt

        # Check if it's time to spawn a new hero
        if self._spawn_elapsed > self._spawn_interval:
            print("Spawning hero")
            # self.game.dungeon.spawn_hero()
            # self._spawn_elapsed = 0

################################################################################
    def engage(self, attacker: DMUnit, defender: DMUnit) -> None:

        self._encounters.append(DMEncounter(self.game, attacker, defender))

################################################################################
    def trap_attack(self, trap: DMTrapRoom, defender: DMUnit) -> None:

        # Traps don't need a full engagement, just a single turn.
        ctx = AttackContext(self.game, trap, defender)
        ctx.execute()

################################################################################
    def increase_hero_count_pct(self, amount: float) -> None:

        if not isinstance(amount, float):
            raise ArgumentTypeError(
                "BattleManager.increase_spawn_total_pct()",
                type(amount),
                type(float)
            )

        self._hero_amt_scalar += amount

################################################################################
    def increase_hero_count_flat(self, amount: int) -> None:

        if not isinstance(amount, int):
            raise ArgumentTypeError(
                "BattleManager.increase_spawn_total_pct()",
                type(amount),
                type(int)
            )

        self._hero_amt_additional += amount

################################################################################
    def set_dragon_slayer(self, value: bool) -> None:

        self._dragon_slayer_flag = value

################################################################################
