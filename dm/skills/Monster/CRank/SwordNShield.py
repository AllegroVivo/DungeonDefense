from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("SwordNShieldSkill",)

################################################################################
class SwordNShieldSkill(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-209",
            name="Sword 'n Shield",
            description=(
                "Gain 3 (+0.75*ATK) Armor for every attack."
            ),
            rank=2,
            cooldown=CooldownType.Passive,
            effect=SkillEffect(base=3, scalar=0.75),
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        # Doesn't say it needs to be successful.
        if self.owner == ctx.source:
            self.owner.add_status("Armor", self.effect, self)

################################################################################
