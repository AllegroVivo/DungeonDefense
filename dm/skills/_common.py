from __future__ import annotations

from typing     import TYPE_CHECKING, Literal, Optional
from dm.core.objects.skill import DMSkill
from utilities import DMSkillType, UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("CommonSkill",)

################################################################################
class CommonSkill(DMSkill):

    def __init__(
        self,
        state: DMGame,
        parent: Optional[DMUnit],
        *,
        _id: str,
        name: str,
        description: Optional[str],
        rank: int = 0,
        unlock: Optional[UnlockPack] = None,
        cooldown: Literal[0, 1, 2, 4, 6, 8] = 0,
    ):

        super().__init__(state, parent, cooldown, _id, name, description, rank, unlock)

################################################################################
    @property
    def skill_type(self) -> DMSkillType:

        return DMSkillType.Common

################################################################################
