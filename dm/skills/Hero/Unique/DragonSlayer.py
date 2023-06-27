from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("DragonSlayer",)

################################################################################
class DragonSlayer(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-351",
            name="Dragon Slayer",
            description=(
                "Apply 5 Hatred and 20(+5.0ATK) Fury to all allies in the "
                "dungeon. Also, remove target's Armor upon inflicting 100 % "
                "penetrating damage to an enemy."
            ),
            rank=6,
            cooldown=CooldownType.DungeonWide,
            effect=SkillEffect(base=20, scalar=5.0)
        )

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're attacking
        if self.owner == ctx.source:
            # If penetrating damage if being dealt
            if ctx._damage._damage_override != 0:
                # If the target has Armor
                armor = ctx.target.get_status("Armor")
                if armor is not None:
                    # Remove it
                    armor.deplete_all_stacks()

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        for unit in self.game.units_of_type(self.owner):
            unit.add_status("Hatred", 5, self)
            unit.add_status("Fury", self.effect, self)

################################################################################
