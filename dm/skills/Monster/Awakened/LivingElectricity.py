from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from dm.core.objects.hero import DMHero
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext, StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("LivingElectricity",)

################################################################################
class LivingElectricity(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-322",
            name="Living Electricity",
            description=(
                "Shock applied to enemies in Recharge state increase by 2 % per "
                "Recharge possessed. Damage received by enemy in Electrical "
                "Short state increase by 10 % per Electrical Short possessed."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")
        self.listen("status_applied", self.status_applied)

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if isinstance(ctx.target, DMHero):
            short = ctx.target.get_status("Electrical Short")
            if short is not None:
                ctx.amplify_pct(short.stacks * 0.10)

################################################################################
    @staticmethod
    def status_applied( ctx: StatusApplicationContext) -> None:

        if isinstance(ctx.target, DMHero):
            if ctx.status.name == "Shock":
                recharge = ctx.target.get_status("Recharge")
                if recharge is not None:
                    ctx.increase_stacks_pct(recharge.stacks * 0.02)

################################################################################
