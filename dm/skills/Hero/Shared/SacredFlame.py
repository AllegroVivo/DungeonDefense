from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("SacredFlame",)

################################################################################
class SacredFlame(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-332",
            name="Sacred Flame",
            description=(
                "Inflict 16 (+3.0*ATK) damage to target and remove Immortality "
                "applied to target."
            ),
            rank=3,
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=16, scalar=3.0)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # Remove Immortality from the target first to allow for death if
        # damage is sufficient.
        immortality = ctx.target.get_status("Immortality")
        if immortality is not None:
            immortality.deplete_all_stacks()

        # Then deal damage.
        ctx.target.damage(self.effect)

################################################################################
