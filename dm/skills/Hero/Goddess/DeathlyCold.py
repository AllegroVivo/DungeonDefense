from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from dm.core.objects.monster import DMMonster
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("DeathlyCold",)

################################################################################
class DeathlyCold(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-402",
            name="Deathly Cold",
            description=(
                "All monsters gain 3 Overweight. Also after ending an action, "
                "LIFE decreases by 1 % of lost LIFE per Overweight possessed."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        # Start all opponents off with 3 stacks of Overweight
        for unit in self.game.units_of_type(self.owner, inverse=True):
            unit.add_status("Overweight", 3, self)

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're being attacked by a monster, register a callback
        if isinstance(ctx.source, DMMonster):
            ctx.register_post_execute(self.callback)

################################################################################
    @staticmethod
    def callback(ctx: AttackContext) -> None:

        # Decrease LIFE by 1% of lost LIFE per Overweight possessed
        overweight = ctx.source.get_status("Overweight")
        if overweight is not None:
            ctx.source._damage(overweight.stacks * (ctx.damage / 100))

################################################################################
