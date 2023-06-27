from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Engineer",)

################################################################################
class Engineer(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-359",
            name="Engineer",
            description=(
                "Apply (10 (+3.0*ATK) damage and) additional damage as much "
                "as Armor applied to target, and remove all Armor, Shield, "
                "and Defense."
            ),
            rank=5,
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=10, scalar=3.0)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # If we're attacking
        if self.owner == ctx.source:
            # Handle buff offsets first
            damage = self.effect
            # If the target has Armor, apply additional damage
            armor = ctx.target.get_status("Armor")
            if armor is not None:
                damage += armor.stacks
                # and remove all Armor
                armor.deplete_all_stacks()

            # If the target has Shield, remove all Shield
            shield = ctx.target.get_status("Shield")
            if shield is not None:
                shield.deplete_all_stacks()

            # If the target has Defense, remove all Defense
            defense = ctx.target.get_status("Defense")
            if defense is not None:
                defense.deplete_all_stacks()

            # Then damage
            ctx.target.damage(damage)

################################################################################
