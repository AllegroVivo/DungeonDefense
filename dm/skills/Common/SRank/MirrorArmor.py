from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("MirrorArmor",)

################################################################################
class MirrorArmor(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-182",
            name="Mirror Armor",
            description=(
                "Gain 3 Mirror at the beginning of battle. Upon receiving "
                "8th damage, gain 1 Mirror."
            ),
            rank=4,
            cooldown=CooldownType.Passive
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            if self.atk_count % 8 == 0:
                self.owner.add_status("Mirror", 1, self)

################################################################################
    def on_acquire(self) -> None:

        self.listen("hero_spawn")

################################################################################
    def notify(self, unit: DMUnit) -> None:

        if self.owner == unit:
            self.owner.add_status("Mirror", 3, self)

################################################################################
