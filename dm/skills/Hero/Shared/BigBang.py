from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("BigBangSkill",)

################################################################################
class BigBangSkill(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-337",
            name="Big Bang",
            description=(
                "Inflict 20 (+1.0*ATK) damage to all enemies in adjacent rooms."
            ),
            rank=5,
            cooldown=CooldownType.AdjacentWide,
            effect=SkillEffect(base=20, scalar=1.0)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # Get targets from the room and adjacent rooms
        targets = self.room.units_of_type(self.owner, inverse=True)
        for room in self.room.adjacent_rooms:
            targets.extend(room.units_of_type(self.owner, inverse=True))

        # Deal damage to all targets
        for target in targets:
            target.damage(self.effect)

################################################################################
