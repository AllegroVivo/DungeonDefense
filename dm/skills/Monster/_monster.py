from __future__ import annotations

from typing     import TYPE_CHECKING, Optional
from dm.core.objects.skill import DMSkill
from utilities import *

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("MonsterSkill",)

################################################################################
class MonsterSkill(DMSkill):

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
        cooldown: CooldownType = CooldownType.Passive,
        effect: Optional[SkillEffect] = None
    ):

        super().__init__(
            state, parent, cooldown, effect, _id, name, description, rank, unlock
        )

################################################################################
    @property
    def category(self) -> SkillCategory:

        return SkillCategory.Monster

################################################################################
