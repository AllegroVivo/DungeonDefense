from __future__ import annotations

import random

from pygame         import Surface, Vector2
from typing         import TYPE_CHECKING, List, Optional, Tuple, Union

from .map           import DMDungeonMap
from utilities      import *

if TYPE_CHECKING:
    from .game import DMGame
    from ..objects.hero import DMHero
    from ..objects.monster import DMMonster
    from ..objects.room import DMRoom
    from ...rooms.special.Entrance   import EntranceRoom
    from ..objects.unit import DMUnit
################################################################################

__all__ = ("DMDungeon",)

################################################################################
class DMDungeon:

    __slots__ = (
        "game",
        "heroes",
        "map",
        "spawned"
    )

################################################################################
    def __init__(self, game: DMGame):

        self.game: DMGame = game
        self.heroes: List[DMHero] = []
        self.map = DMDungeonMap(self)

        self.spawned = False

################################################################################
    def __getitem__(self, index: int) -> List[Optional[DMRoom]]:

        return self.map[index]

################################################################################
    def draw(self, screen: Surface) -> None:

        self.map.draw(screen)

################################################################################
    def update(self, dt: float) -> None:

        self.map.update(dt)
        self.game.dark_lord.update(dt)

###############################################################################
    def get_room_at(self, pos: Union[Vector2, Tuple[int, int]]) -> Optional[DMRoom]:

        return self.map.get_room_at(Vector2(pos))

################################################################################
    def all_rooms(self, entry: bool = False, boss: bool = False, empty: bool = False) -> List[DMRoom]:

        return self.map.all_rooms(entry, boss, empty)

################################################################################
    def modify_hero_spawn_rate(self, amount: Union[int, float]) -> None:

        if not isinstance(amount, (int, float)):
            raise ArgumentTypeError(
                "Invalid type passed to DMDungeon.modify_hero_spawn_rate()",
                type(amount),
                type(int), type(float)
            )

        self.map.modify_hero_spawn_rate(amount)

################################################################################
    @property
    def highlighting(self) -> bool:

        return self.map.highlighting

################################################################################
    def reset_highlighting(self) -> None:

        self.map.reset_highlighting()

################################################################################
    def toggle_highlighting(self, value: bool) -> None:

        self.map.toggle_highlighting(value)

################################################################################
    def get_highlighted_room(self) -> Optional[DMRoom]:

        return self.map.get_highlighted_room()

################################################################################
    def get_adjacent_rooms(
        self,
        pos: Vector2,
        *,
        show_west: bool = False,
        show_east: bool = False,
        show_north: bool = False,
        show_south: bool = False,
        all_rooms: bool = True,
        include_current: bool = False
    ) -> List[DMRoom]:

        return self.map.get_all_adjacent_rooms(
            pos, show_west, show_east, show_north,
            show_south, all_rooms, include_current
        )

################################################################################
    def get_adjacent_monsters(
        self,
        pos: Vector2,
        *,
        include_west: bool = False,
        include_east: bool = False,
        include_north: bool = False,
        include_south: bool = False,
        all_rooms: bool = True,
        include_current: bool = False
    ) -> List[DMMonster]:
        
        rooms = self.get_adjacent_rooms(
            pos, show_west=include_west, show_east=include_east, show_north=include_north,
            show_south=include_south, all_rooms=all_rooms, include_current=include_current
        )
        
        monsters = []
        for room in rooms:
            try:
                monsters.extend(room.monsters)  # type: ignore
            except AttributeError:
                pass
            
        return monsters
        
################################################################################
    @property
    def deployed_monsters(self) -> List[DMMonster]:

        return self.map.deployed_monsters

################################################################################
    def upgrade_random_monster(self, include_inventory: bool = False) -> DMMonster:

        monsters = self.deployed_monsters
        if include_inventory:
            monsters.extend(self.game.inventory.monsters)

        choice = random.choice(monsters)
        choice.upgrade()

        return choice

################################################################################
    def spawn_hero(self) -> DMHero:

        if not self.spawned:
            hero = self.game.spawn(
                spawn_type=DMSpawnType.Hero,
                end_rank=1
            )(self.game, self.game.dungeon.entrance)
            self.heroes.append(hero)  # type: ignore
            self.spawned = True

            return hero  # type: ignore

################################################################################
    @property
    def entrance(self) -> EntranceRoom:

        return self.map[len(self.map) // 2][len(self.map[0]) - 1]  # type: ignore

################################################################################
    def get_heroes_by_room(self, pos: Vector2) -> List[DMHero]:

        return self.get_room_at(pos).heroes

################################################################################
    def get_monsters_by_room(self, pos: Vector2) -> List[DMHero]:

        room = self.get_room_at(pos)
        if room.room_type is not DMRoomType.Battle:
            return []

        return room.monsters  # type: ignore

################################################################################
