from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from ....core.objects.hero import DMHero
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Template",)

################################################################################
class Template(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-266",
            name="Lightning Reflux",
            description=(
                "Every time enemies inflicted with Shock receive damage, "
                "(this unit) receives 2 Quick. Increases DEX by 200 %."
            ),
            rank=5,
            cooldown=CooldownType.Passive,
            passive=True,
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        # Just going to perform a hard check here to see if the target is
        # a hero. It's pretty safe to assume we don't need to use generalized
        # logic for unit types here since this is a monster skill.
        if isinstance(ctx.target, DMHero):
            ctx.register_post_execute(self.post_execute)

################################################################################
    def post_execute(self, ctx: AttackContext) -> None:

        if not ctx.will_fail:
            shock = ctx.target.get_status("Shock")
            if shock is not None:
                self.owner.add_status("Quick", 2, self)

################################################################################
    def stat_adjust(self) -> None:

        self.owner.increase_stat_pct("DEX", 2.00)

################################################################################
