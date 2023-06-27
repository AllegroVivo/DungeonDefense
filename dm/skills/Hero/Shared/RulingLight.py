from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("RulingLight",)

################################################################################
class RulingLight(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-336",
            name="Ruling Light",
            description=(
                "Inflict 24 (+1.0*ATK) damage and apply 3 Blind to all "
                "enemies in the room."
            ),
            rank=4,
            cooldown=CooldownType.RoomWide,
            effect=SkillEffect(base=24, scalar=1.0)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # For each enemy in the room
        for target in ctx.room.units_of_type(self.owner, inverse=True):
            # Inflict damage and apply Blind.
            target.damage(self.effect)
            target.add_status("Blind", 3, self)

################################################################################
