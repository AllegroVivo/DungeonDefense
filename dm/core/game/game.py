from __future__ import annotations

import pygame
import sys

from pygame     import Vector2
from typing     import TYPE_CHECKING, Callable, List, Optional, Type, Union

from ..battle.system        import DMBattleManager
from .darklord              import DMDarkLord
from .dungeon               import DMDungeon
from .event_mgr             import DMEventManager
from ..fates.fateboard      import DMFateBoard
from .inventory             import DMInventory
from .objpool               import DMObjectPool
from .relic_mgr             import DMRelicManager
from ..states.state_manager import DMStateMachine
from utilities              import *

if TYPE_CHECKING:
    from dm.core.game.map import DMDungeonMap
    from dm.core.objects.hero import DMHero
    from dm.core.objects.monster import DMMonster
    from dm.core.objects.object import DMObject
    from dm.core.objects.relic import DMRelic
    from dm.core.objects.room import DMRoom
    from dm.core.states.state import DMState
################################################################################

__all__ = ("DMGame",)

################################################################################
class DMGame:

    __slots__ = (
        "screen",
        "clock",
        "running",
        "dungeon",
        "state_machine",
        "inventory",
        "fateboard",
        "battle_mgr",
        "objpool",
        "relics",
        "day",
        "events",
        "dark_lord",
    )

################################################################################
    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running: bool = True

        self.day: int = 1

        # Order is important here.
        self.events: DMEventManager = DMEventManager(self)
        self.objpool: DMObjectPool = DMObjectPool(self)
        self.fateboard: DMFateBoard = DMFateBoard(self)
        self.dark_lord: DMDarkLord = DMDarkLord(self)
        self.dungeon: DMDungeon = DMDungeon(self)
        self.inventory: DMInventory = DMInventory(self)
        self.state_machine: DMStateMachine = DMStateMachine(self)
        self.relics: DMRelicManager = DMRelicManager(self)
        self.battle_mgr: DMBattleManager = DMBattleManager(self)

################################################################################
    def run(self) -> None:

        self.state_machine.push_state("main_menu")

        while self.running:
            dt = self.clock.tick(FPS) / 1000

            self.handle_events()

            self.state_machine.update(dt)
            self.state_machine.draw(self.screen)

            pygame.display.flip()

        self.quit()

################################################################################
    def handle_events(self) -> None:

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                self.running = False

            self.state_machine.handle_event(event)

################################################################################
    def draw_dungeon(self) -> None:

        self.dungeon.draw(self.screen)

################################################################################
    @property
    def state(self) -> DMState:

        return self.state_machine._states[-1]

################################################################################
    @property
    def map(self) -> DMDungeonMap:

        return self.dungeon.map

################################################################################
    @staticmethod
    def quit() -> None:

        pygame.quit()
        sys.exit()

################################################################################
    @property
    def deployed_monsters(self) -> List[DMMonster]:

        return self.dungeon.deployed_monsters

################################################################################
    @property
    def all_monsters(self) -> List[DMMonster]:

        return self.dungeon.deployed_monsters + self.inventory.monsters

################################################################################
    @property
    def all_heroes(self) -> List[DMHero]:

        return self.dungeon.heroes

################################################################################
    def spawn(
        self,
        _n: Optional[str] = None,
        *,
        obj_id: Optional[str] = None,
        spawn_type: Optional[DMSpawnType] = None,
        start_rank: int = 1,
        end_rank: int = 5,
        weighted: bool = True,
        init_obj: bool = False,
        **kwargs
    ) -> Union[DMObject, Type[DMObject]]:
        """Attempts to spawn a DMObject per the given arguments.

        All arguments are optional, but at least one of `_n`, `obj_id`, or
        `spawn_type` must be present.

        By default this will return a newly instantiated copy of the object utilizing
        any provided `**kwargs` that would be compatible with the spawned type's
        internal `_copy()` method.

        Parameters:
        -----------
        _n: :class:`str`
            The object's in-game name. This is the one that might have spaces and
            definitely has capital letters.

        obj_id: :class:`str`
            The unique string identifier of the object. In the general format `ABC-123`.

        spawn_type: :class:`SpawnType`
            The type of object to spawn if a random spawn is being invoked.

        start_rank: :class:`int`
            If spawning a random entity, the lowest rank group to include in the
            options. Defaults to `1`.

        end_rank: :class:`int`
            If spawning a random entity, the highest rank group to include in the
            options. Defaults to `5`.

        weighted: :class:`bool`
            If spawning a random entity, whether or not to weight the selection based
            on ranking, where lower ranks will appear more frequently then higher ranks.
            Defaults to `True`.

        init_obj: :class:`bool`
            Whether to return only the class type or an instantiated copy of the
            class with the given `**kwargs`. Defaults to False.

        Returns:
        --------
        Union[:class:`DMObject`, Type[:class:`DMObject`]]
            Either the type of the returned spawn or a cleanly instantiated copy
            utilizing the provided `**kwargs` if `init_obj` was set to True.
        """

        return self.objpool.spawn(
            _n=_n,
            obj_id=obj_id,
            spawn_type=spawn_type,
            start_rank=start_rank,
            end_rank=end_rank,
            weighted=weighted,
            init_obj=init_obj,
            **kwargs
        )

###############################################################################
    def get_room_at(self, pos: Vector2) -> Optional[DMRoom]:

        return self.dungeon.get_room_at(pos)

################################################################################
    def display_popup(self, title: Optional[str], text: Optional[str]) -> None:

        self.state_machine.push_state("popup_box")

        self.state_machine.current_state.set_title(title)  # type: ignore
        self.state_machine.current_state.set_text(text)  # type: ignore

################################################################################
    def advance_day(self) -> None:

        self.day += 1
        self.state_machine.switch_state("fate_select")

################################################################################
    def dispatch_event(self, event_type: str, **payload) -> None:

        self.events.dispatch(event_type, **payload)

################################################################################
    def subscribe_event(self, event_type: str, callback: Callable) -> None:

        self.events.subscribe(event_type, callback)

################################################################################
    def unsubscribe_event(self, event_type: str, callback: Callable) -> None:

        self.events.unsubscribe(event_type, callback)

################################################################################
    def generate_type(self, raw_type: str) -> Type[DMObject]:

        return self.objpool.generate_type(raw_type)

################################################################################
    def get_relic(self, relic: Union[str, DMRelic]) -> Optional[DMRelic]:

        return self.relics.get_relic(relic)

################################################################################
    def push_state(self, state: Union[str, DMState]) -> None:
        """Pushes a state on top of the current state, but doesn't replace it."""

        self.state_machine.push_state(state)

################################################################################
    def pop_state(self) -> None:
        """Removes the top state from the stack."""

        self.state_machine.pop_state()

################################################################################
    def switch_state(self, state: Union[str, DMState]) -> None:
        """Completely replaces the current state with the given state."""

        self.state_machine.switch_state(state)

################################################################################
