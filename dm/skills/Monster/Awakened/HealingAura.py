from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from dm.core.objects.monster import DMMonster
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("HealingAura",)

################################################################################
class HealingAura(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-316",
            name="Healing Aura",
            description=(
                "All monsters recover 20 % of the lost LIFE when taking an "
                "action. If LIFE is less than half, gain 1 Absorption."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

        # I'm making the assumption that the check for life being less than
        # half occurs *after* the restoration of heath.

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if isinstance(ctx.source, DMMonster):
            ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        if ctx.damage > 0:
            ctx.source.heal(int(ctx.damage * 0.20))
            if ctx.source.life < ctx.source.max_life / 2:
                ctx.source.add_status("Absorption", 1, self)

################################################################################
