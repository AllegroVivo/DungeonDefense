from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType, SkillEffect, StatusType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("DivineBrilliance",)

################################################################################
class DivineBrilliance(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-339",
            name="Divine Brilliance",
            description=(
                "Recover 40 (+1.0*ATK) LIFE of all allies in the room and "
                "remove all unfavorable states."
            ),
            rank=5,
            cooldown=CooldownType.RoomWide,
            effect=SkillEffect(base=40, scalar=1.0)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # For every ally in the same room
        for unit in self.room.units_of_type(self.owner):
            # Heal the unit
            unit.heal(self.effect)
            # And remove all negative effects.
            for status in unit.statuses:
                if status._type in (StatusType.Debuff, StatusType.AntiBuff):
                    status.deplete_all_stacks()

################################################################################
