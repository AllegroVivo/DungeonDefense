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

__all__ = ("IceFog",)

################################################################################
class IceFog(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-310",
            name="Ice Fog",
            description=(
                "Gain 3 Slow and 1 Frostbite each time an enemy in the "
                "dungeon takes an action."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if isinstance(ctx.source, DMHero):
            ctx.source.add_status("Slow", 3, self)
            ctx.source.add_status("Frostbite", 1, self)

################################################################################
