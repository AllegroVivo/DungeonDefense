from __future__ import annotations

from pygame         import Surface, Vector2
from typing         import TYPE_CHECKING, List, Optional, Type, Union

from utilities      import *

if TYPE_CHECKING:
    from dm.core    import DMDungeon, DMGame, DMMonster, DMRoom
    from dm.rooms   import BossRoom
################################################################################

__all__ = ("DMDungeonMap",)

################################################################################
class DMDungeonMap:

    __slots__ = (
        "parent",
        "grid",
        "highlighting",
        "hero_spawn_base",
        "hero_spawn_flat_additional",
        "hero_spawn_pct",
    )

################################################################################
    def __init__(self, parent: DMDungeon):

        self.parent: DMDungeon = parent

        self.grid: List[List[DMRoom]] = []
        self.highlighting = False

        self.hero_spawn_base: int = 15
        self.hero_spawn_flat_additional: int = 0
        self.hero_spawn_pct: float = 1.00
        
        self._init_map()

################################################################################
    def _init_map(self):

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

        # Create starter rows
        self.grid = [
            create_row(self.game, 0),
            create_row(self.game, 1),
            create_row(self.game, 2)
        ]

        # Fill in Boss, Entry, and starter Battle rooms.
        self.grid[1][0] = self.game.spawn(obj_id="BOSS-000")(self.game, col=0, row=1)
        self.grid[1][3] = self.game.spawn(obj_id="BTL-101")(self.game, col=3, row=1)
        self.grid[1][5] = self.game.spawn(obj_id="ENTR-000")(self.game, col=5, row=1)

        self.boss_tile._init_dark_lord()

################################################################################
    def __len__(self) -> int:

        return len(self.grid)

################################################################################
    def __getitem__(self, index) -> List[Optional[DMRoom]]:

        return self.grid[index]

################################################################################
    @property
    def boss_tile(self) -> BossRoom:

        return self.grid[len(self.grid) // 2][0]  # type: ignore

################################################################################
    @property
    def game(self) -> DMGame:
        
        return self.parent.game
    
################################################################################
    @property
    def hero_spawn_count(self) -> int:

        return int((self.hero_spawn_base * self.hero_spawn_pct) + self.hero_spawn_flat_additional)

###############################################################################
    @property
    def height(self) -> int:

        return len(self.grid)

###############################################################################
    @property
    def width(self) -> int:

        return len(self.grid[0])

###############################################################################
    def get_room_at(self, pos: Vector2) -> Optional[DMRoom]:

        try:
            return self.grid[int(pos.x)][int(pos.y)]
        except IndexError:
            return

################################################################################
    def modify_hero_spawn_rate(self, amount: Union[int, float]) -> None:

        if not isinstance(amount, (int, float)):
            raise ArgumentTypeError(
                "Invalid type passed to DungeonDetails.modify_hero_spawn_rate()",
                type(amount),
                type(int), type(float)
            )

        if isinstance(amount, int):
            self.hero_spawn_flat_additional += amount
        elif isinstance(amount, float):
            self.hero_spawn_pct += amount

################################################################################
    def draw(self, screen: Surface) -> None:

        for row in self.grid:
            for room in row:
                if room is not None:
                    room.draw(screen)

################################################################################
    def update(self, dt: float) -> None:

        for row in self.grid:
            for room in row:
                if room is not None:
                    room.update(dt)

################################################################################
    def auto_deploy(self) -> None:
        """Automatically deploys monsters from the inventory, from strongest -
        based on total stat score - to weakest. Starts at the top-right of the
        dng_options and moves to the bottom left.
        ~SP 6/2/23
        """

        # Start from the top-right corner and move down, then to the left
        while True:
            monsters_placed = 0

            for col in reversed(range(len(self.grid))):
                for row in range(len(self.grid[0])):
                    room = self.grid[col][row]

                    if room is not None:
                        # Try to deploy a monster here if it's a battle room.
                        if room.room_type is DMRoomType.Battle:
                            if not room.is_full:  # type: ignore
                                # Try to get a monster from the inventory
                                monster = self.game.inventory.get_random_inventory_monster()

                                # If there is a monster, deploy it
                                if monster is not None:
                                    room.deploy_monster(monster)  # type: ignore
                                    monsters_placed += 1

            # If no monsters were placed during this sweep, or there are no more monsters in the inventory, stop deploying
            if monsters_placed == 0 or len(self.game.inventory.monsters) == 0:
                return

################################################################################
    def all_rooms(self, entry: bool, boss: bool, empty: bool) -> List[DMRoom]:

        ret = []

        for row in self.grid:
            ret.extend([room for room in row if room is not None])

        for i, room in enumerate(ret):
            if not entry:
                if room.room_type is DMRoomType.Entrance:
                    ret.pop(i)
            if not boss:
                if room.room_type is DMRoomType.Boss:
                    ret.pop(i)
            if not empty:
                if room.room_type is DMRoomType.Empty:
                    ret.pop(i)

        return ret

################################################################################
    def reset_monster_deployment(self) -> None:

        for room in self.all_rooms(False, False, False):
            if room.room_type is DMRoomType.Battle and room.monsters:  # type: ignore
                room.reset_monster_deployment()  # type: ignore

################################################################################
    def toggle_highlighting(self, value: bool) -> None:

        self.highlighting = value
        if self.highlighting:
            self.reset_cursor_location()

################################################################################
    def reset_highlighting(self) -> None:

        for row in self.grid:
            for room in row:
                if room is not None:
                    room.toggle_highlighting(False)

################################################################################
    def reset_cursor_location(self) -> None:

        self.reset_highlighting()
        self.grid[0][1].toggle_highlighting(True)

################################################################################
    def get_highlighted_room(self) -> Optional[DMRoom]:

        for row in self.grid:
            for room in row:
                if room is not None:
                    if room.highlighted:
                        return room

################################################################################
    def get_all_adjacent_rooms(
        self,
        pos: Vector2,
        show_west: bool,
        show_east: bool,
        show_north: bool,
        show_south: bool,
        all_rooms: bool,
        include_current: bool
    ) -> List[DMRoom]:

        if all((show_west, show_east, show_north, show_south, all_rooms)):
            raise ValueError("Received conflicting arguments while completing adjacent rooms query.")
        if any((show_west, show_east, show_north, show_south)) and all_rooms:
            raise ValueError("Received conflicting arguments while completing adjacent rooms query.")
        if not any((show_west, show_east, show_north, show_south, all_rooms)):
            raise ValueError("Received literally no True arguments while completing adjacent rooms query.")

        ret = []

        # Left
        x = Vector2(pos.x - 1, pos.y)
        west = self.get_room_at(x)
        if west is not None:
            if show_west or all_rooms:
                ret.append(west)
        # Right
        x = Vector2(pos.x + 1, pos.y)
        east = self.get_room_at(x)
        if east is not None:
            if show_east or all_rooms:
                ret.append(east)
        # Up
        x = Vector2(pos.x, pos.y - 1)
        north = self.get_room_at(x)
        if north is not None:
            if show_north or all_rooms:
                ret.append(north)
        # Down
        x = Vector2(pos.x, pos.y + 1)
        south = self.get_room_at(x)
        if south is not None:
            if show_south or all_rooms:
                ret.append(south)

        final = [r for r in ret if r.__class__.__name__ != "EntranceRoom"]
        if include_current:
            final.append(self.get_room_at(pos))

        return final

################################################################################
    @property
    def deployed_monsters(self) -> List[DMMonster]:

        ret = []

        for row in self.grid:
            for room in row:
                try:
                    ret.extend(room.monsters)  # type: ignore
                except AttributeError:
                    pass

        return ret

################################################################################
