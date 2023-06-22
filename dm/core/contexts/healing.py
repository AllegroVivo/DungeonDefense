from __future__ import annotations

from typing     import TYPE_CHECKING

from .adjustable import AdjustableContext

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
    from dm.core.objects.room import DMRoom
################################################################################

__all__ = ("HealingContext",)

################################################################################
class HealingContext(AdjustableContext):

    def __init__(self, state: DMGame, target: DMUnit, amount: int):

        super().__init__(state, amount, target)

################################################################################
    @property
    def room(self) -> DMRoom:

        return self.object.room

################################################################################
    @property
    def target(self) -> DMUnit:

        return self.object  # type: ignore

################################################################################
    def execute(self) -> None:

        self._obj._heal(self.calculate())  # type: ignore

################################################################################
