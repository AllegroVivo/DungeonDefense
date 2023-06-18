from __future__ import annotations

from typing     import TYPE_CHECKING

from .adjustable import AdjustableContext

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("HealingContext",)

################################################################################
class HealingContext(AdjustableContext):

    def __init__(self, state: DMGame, target: DMUnit, amount: int):

        super().__init__(state, amount, target)

################################################################################
    def execute(self) -> None:

        self._obj.heal(self.calculate())  # type: ignore

################################################################################
