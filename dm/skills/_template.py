from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Template",)

################################################################################
class Template(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-000",
            name="UrMom",
            description=(
                "UrMom"
            ),
            rank=2,
            cooldown=0
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
    def stat_adjust(self) -> None:

        pass

################################################################################
