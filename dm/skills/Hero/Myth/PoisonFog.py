from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("PoisonFog",)

################################################################################
class PoisonFog(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-391",
            name="Poison Fog",
            description=(
                "Applies 60 (+3.0*ATK) Poison and 1 Spore to all enemies in "
                "the dungeon with each attack. Attacking an enemy in Poison "
                "state will deal extra damage equal to Poison possessed by "
                "the target."
            ),
            rank=9,
            cooldown=CooldownType.Passive,
            effect=SkillEffect(base=60, scalar=3.0)
        )

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're attacking
        if self.owner == ctx.source:
            # First let's make the attack so the unit doesn't necessarily have
            # Poison applied to it yet.
            poison = ctx.target.get_status("Poison")
            if poison is not None:
                ctx.amplify_flat(poison.stacks)

            # Then we can apply the status to all units.
            for unit in self.game.units_of_type(self.owner, inverse=True):
                unit.add_status("Poison", self.effect, self)
                unit.add_status("Spore", 1, self)

################################################################################
