from __future__ import annotations

import random

from pygame         import Surface, Vector2
from typing         import TYPE_CHECKING, List, Optional, Type, Union

from .map           import DMDungeonMap
from utilities      import *

if TYPE_CHECKING:
    from dm.core    import DMGame, DMHero, DMMonster, DMRoom
################################################################################

__all__ = ("DMDungeon",)

################################################################################
class DMDungeon:

    __slots__ = (
        "game",
        "heroes",
        "map"
    )

################################################################################
    def __init__(self, game: DMGame):

        self.game: DMGame = game
        self.heroes: List[DMHero] = []
        self.map = DMDungeonMap(self)

################################################################################
    def __getitem__(self, index: int) -> List[Optional[DMRoom]]:

        return self.map[index]

################################################################################
    def _init_map(self):
        """Initializes the dungeon grid map with a fresh 4x3 main grid
        (with boss/entry rooms on their respective sides).
        """

        def create_row(game, row):
            empty_room: Type[EmptyRoom] = game.spawn(obj_id="ROOM-000", init_obj=False)  # type: ignore
            row_rooms = []
            for col in range(6):
                if col in {0, 5}:
                    room = None
                else:
                    room = empty_room(game, row=row, col=col)
                row_rooms.append(room)
            return row_rooms

        self.map = [
            create_row(self.game, 0),
            create_row(self.game, 1),
            create_row(self.game, 2)
        ]

        self.map[1][0] = self.game.spawn(obj_id="BOSS-000")(self.game, col=0, row=1)
        self.map[1][3] = self.game.spawn(obj_id="BTL-101")(self.game, col=3, row=1)
        self.map[1][5] = self.game.spawn(obj_id="ENTR-000")(self.game, col=5, row=1)

################################################################################
    def draw(self, screen: Surface) -> None:

        self.map.draw(screen)

################################################################################
    def update(self, dt: float) -> None:

        self.map.update(dt)
        self.game.dark_lord.update(dt)

###############################################################################
    def get_room_at(self, pos: Vector2) -> Optional[DMRoom]:

        return self.map.get_room_at(pos)

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
