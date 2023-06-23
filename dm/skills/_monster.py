from __future__ import annotations

from typing     import TYPE_CHECKING, List, Literal, Optional
from dm.core.objects.skill import DMSkill
from utilities import SkillCategory, UnlockPack, SkillType, SkillEffect

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
        cooldown: Literal[0, 1, 2, 4, 6, 8] = 0,
        passive: bool = False,
        effect: Optional[SkillEffect] = None
    ):

        _type = SkillType.Passive if passive else SkillType.Active

        super().__init__(
            state, parent, cooldown, _type, effect,
            _id, name, description, rank, unlock
        )

################################################################################
    @property
    def category(self) -> SkillCategory:

        return SkillCategory.Monster

################################################################################
