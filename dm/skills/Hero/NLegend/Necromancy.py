from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Necromancy",)

################################################################################
class Necromancy(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-369",
            name="Necromancy",
            description=(
                "Inflict 120 (+1.5*ATK) damage to enemies in the room and "
                "turn their Immortality into Vulnerable."
            ),
            rank=6,
            cooldown=CooldownType.RoomWide,
            effect=SkillEffect(base=120, scalar=1.5)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # If we're the attacker
        if self.owner == ctx.source:
            # Deal damage to all enemies in the room
            for unit in ctx.room.units_of_type(self.owner, inverse=True):
                unit.damage(self.effect)
                # Check for Immortality
                immortality = unit.get_status("Immortality")
                if immortality is not None:
                    # And, if present, convert it into Vulnerable
                    unit.add_status("Vulnerable", immortality.stacks, self)
                    immortality.deplete_all_stacks()

################################################################################
