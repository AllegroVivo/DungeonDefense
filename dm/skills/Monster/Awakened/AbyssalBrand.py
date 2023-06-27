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

__all__ = ("AbyssalBrand",)

################################################################################
class AbyssalBrand(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-305",
            name="Abyssal Brand",
            description=(
                "Dull applies to damage dealt by monsters that are not traps."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        pass

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_applied")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if isinstance(ctx.target, DMHero):
            dull = ctx.target.get_status("Dull")
            if dull is not None:
                # We'll just to the math here, since we don't want to trigger
                # a full `status_execute` event. Just buff the damage and
                # reduce stacks as usual.
                # For reference, the effect for `Dull` is as follows:
                # "Damage received from traps is increased by 100%. The stat
                # is reduced by 1 each time it is activated."
                ctx.amplify_pct(1.00)
                dull.reduce_stacks_by_one()


################################################################################
