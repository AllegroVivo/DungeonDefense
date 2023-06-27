from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Template",)

################################################################################
class Template(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-000",
            name="UrMom",
            description=(
                "UrMom"
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        pass

################################################################################
    def on_acquire(self) -> None:

        pass

################################################################################
    def notify(self, *args) -> None:

        pass

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        pass

################################################################################
    def stat_adjust(self) -> None:

        pass

################################################################################
