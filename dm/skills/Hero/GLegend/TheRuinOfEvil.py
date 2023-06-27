from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("TheRuinOfEvil",)

################################################################################
class TheRuinOfEvil(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-389",
            name="The Ruin of Evil",
            description=(
                "Inflict 350 (+3.5*ATK) damage to all enemies in the room and "
                "immediately kill them at a low chance (10%). This attack "
                "cannot be missed or absorbed."
            ),
            rank=8,
            cooldown=CooldownType.RoomWide,
            effect=SkillEffect(base=350, scalar=3.5)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # Target all enemies in the room
        for unit in self.room.units_of_type(self.owner, inverse=True):
            # Determine whether the effect will instantly kill the unit
            damage = self.effect if not self.random.chance(10) else unit.life
            unit._damage(damage)  # Damage the unit directly, bypassing immunities.

################################################################################
