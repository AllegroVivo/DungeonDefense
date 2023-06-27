from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from dm.core.objects.monster import DMMonster
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext, StatusExecutionContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("HealingFairy",)

################################################################################
class HealingFairy(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-309",
            name="Healing Fairy",
            description=(
                "Gain 2(+2.0*ATK) Regeneration each time any monster takes an "
                "action. Also, healing amount of Regeneration increases by 100 %."
            ),
            rank=10,
            cooldown=CooldownType.Passive,
            effect=SkillEffect(base=2, scalar=2.0)
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")
        self.listen("status_execute", self.status_execute)

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if isinstance(ctx.source, DMMonster):
            self.owner.add_status("Regeneration", self.effect, self)

################################################################################
    def status_execute(self, ctx: StatusExecutionContext) -> None:

        if self.owner == ctx.target:
            if ctx.status.name == "Regeneration":
                ctx.status.increase_base_effect(1.00)

################################################################################
