from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Flash",)

################################################################################
class Flash(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-265",
            name="Flash",
            description=(
                "Apply 60 (+1.5*Lv) Shock and 3 Recharge to all enemies in "
                "the dungeon."
            ),
            rank=5,
            cooldown=CooldownType.DungeonWide,
            effect=SkillEffect(base=60, scalar=1.5)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # Easy way to check whether the owner is a monster or a hero without
        # having to import the respective classes.
        targets = self.game.all_heroes if self.owner in self.room.monsters else self.game.all_monsters
        for unit in targets:
            unit.add_status("Shock", self.effect, self)
            unit.add_status("Recharge", 3, self)

################################################################################
