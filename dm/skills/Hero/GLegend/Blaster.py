from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from dm.core.objects.hero import DMHero
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Blaster",)

################################################################################
class Blaster(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-384",
            name="Blaster",
            description=(
                "Attack all monsters in (the dungeon) and the Dark Lord's "
                "Room. (Hero)'s attack will never miss."
            ),
            rank=8,
            cooldown=CooldownType.DungeonWide
        )

        # I assume the portion indicating that an attack will never miss is
        # referring to this attack that is currently being executed.

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        if self.owner == ctx.source:
            for unit in self.game.units_of_type(self.owner, inverse=True):
                unit.direct_damage(ctx.damage)

################################################################################
