from __future__ import annotations

from typing     import TYPE_CHECKING, List, Optional, TypeVar

from dm.core.objects.room import DMRoom
from utilities      import *

if TYPE_CHECKING:
    from pygame     import Surface

    from dm.core    import DMGame, DMMonster
################################################################################

__all__ = ("DMBattleRoom",)

R = TypeVar("R")

################################################################################
class DMBattleRoom(DMRoom):

    __slots__ = (
        "monsters",
        "monster_cap"
    )

################################################################################
    def __init__(
        self,
        state: DMGame,
        row: int,
        col: int,
        _id: str,
        name: str,
        description: str,
        rank: int,
        level: int = 1,
        unlock: Optional[UnlockPack] = None,
        monster_cap: int = 3
    ):

        super().__init__(state, row, col, _id, name, description, rank, level, unlock)

        self.monsters: List[DMMonster] = []
        self.monster_cap: int = monster_cap

################################################################################
    @property
    def is_full(self) -> bool:

        return len(self.monsters) >= self.monster_cap

################################################################################
    def deploy_monster(self, monster: DMMonster) -> None:

        monster.room = self.position
        self.monsters.append(monster)

################################################################################
    def withdraw_monster(self, monster: DMMonster) -> None:

        if monster in self.monsters:
            self.monsters.remove(monster)

################################################################################
    @property
    def room_type(self) -> DMRoomType:

        return DMRoomType.Battle

################################################################################
    def set_monster_cap(self, value: int) -> None:

        self.monster_cap = value

################################################################################
    def reset_monster_deployment(self) -> None:

        self.game.inventory.monsters.extend(self.monsters)
        self.monsters.clear()

################################################################################
    def draw(self, screen: Surface) -> None:

        super().draw(screen)

        for monster in self.monsters:
            monster.graphics.draw(screen)

################################################################################
    def _copy(self, **kwargs) -> DMBattleRoom:

        new_obj: DMBattleRoom = super()._copy(**kwargs)  # type: ignore

        new_obj.monsters = []
        new_obj.monster_cap = kwargs.pop("monster_cap", 3)

        return new_obj  # type: ignore

################################################################################
