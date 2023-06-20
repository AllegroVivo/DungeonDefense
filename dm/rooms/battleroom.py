from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, List, Optional, TypeVar

from dm.core.objects.room import DMRoom
from utilities      import *

if TYPE_CHECKING:
    from pygame     import Surface

    from dm.core    import DMUnit, DMGame, DMMonster
################################################################################

__all__ = ("DMBattleRoom",)

R = TypeVar("R")

################################################################################
class DMBattleRoom(DMRoom):

    __slots__ = (
        "monster_cap",
    )

################################################################################
    def __init__(
        self,
        state: DMGame,
        position: Optional[Vector2],
        _id: str,
        name: str,
        description: str,
        rank: int,
        level: int = 1,
        unlock: Optional[UnlockPack] = None,
        monster_cap: int = 3
    ):

        super().__init__(state, position, _id, name, description, rank, level, unlock)

        self.monster_cap: int = monster_cap

################################################################################
    @property
    def is_full(self) -> bool:

        return len(self.monsters) >= self.monster_cap

################################################################################
    def deploy_monster(self, monster: DMMonster) -> None:

        monster.deploy(self)

################################################################################
    def withdraw_monster(self, monster: DMMonster) -> None:

        if monster in self.monsters:
            monster.withdraw()

################################################################################
    @property
    def room_type(self) -> DMRoomType:

        return DMRoomType.Battle

################################################################################
    def set_monster_cap(self, value: int) -> None:

        self.monster_cap = value

################################################################################
    def reset_monster_deployment(self) -> None:

        for monster in self.monsters:
            monster.withdraw()

################################################################################
    def draw(self, screen: Surface) -> None:

        super().draw(screen)

        for monster in self.monsters:
            monster.graphics.draw(screen)

################################################################################
    def try_engage_monster(self, unit: DMUnit) -> bool:

        for monster in self.monsters:
            if not monster.engaged:
                monster.engage(unit)
                return True

        return False

################################################################################
    def _copy(self, **kwargs) -> DMBattleRoom:

        new_obj: DMBattleRoom = super()._copy(**kwargs)  # type: ignore

        new_obj.monster_cap = kwargs.pop("monster_cap", 3)

        return new_obj  # type: ignore

################################################################################
