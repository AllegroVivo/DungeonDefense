from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from dm.core.objects.hero import DMHero
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("AbyssalWeapon",)

################################################################################
class AbyssalWeapon(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-320",
            name="Abyssal Weapon",
            description=(
                "Gain 1 Overweight each time enemies in the dungeon "
                "receive damage."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

        # I'm making the assumption that the above description means that the
        # status effect will be applied to the unit(s) receiving damage, not
        # this skill's owner.

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if isinstance(ctx.source, DMHero):
            ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        if ctx.damage > 0:
            ctx.source.add_status("Overweight", 1, self)

################################################################################
