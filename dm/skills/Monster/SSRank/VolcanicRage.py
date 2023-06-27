from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("VolcanicRage",)

################################################################################
class VolcanicRage(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-280",
            name="Volcanic Rage",
            description=(
                "Apply 2 Focus, Acceleration, and Hatred to all allies in the "
                "dungeon. Also, apply 2 Stun and 1 (+1.0*ATK) Burn to the attacker."
            ),
            rank=6,
            cooldown=CooldownType.DungeonWide,
            effect=SkillEffect(base=1, scalar=1.0)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # Deal with the attacker first.
        if self.owner == ctx.target:
            ctx.source.add_status("Stun", 2, self)
            ctx.source.add_status("Burn", self.effect, self)

        # Then the rest of the dungeon:
        for monster in self.game.all_monsters:
            for status in ("Focus", "Acceleration", "Hatred"):
                monster.add_status(status, 2, self)

################################################################################
