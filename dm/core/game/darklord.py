from __future__ import annotations

from pygame     import Surface
from typing     import TYPE_CHECKING, Union

from dm.core.objects.unit import DMUnit
from ..graphics.darklord    import DarkLordGraphical

if TYPE_CHECKING:
    from .game  import DMGame
    from ..objects.room import DMRoom
################################################################################

__all__ = ("DMDarkLord",)

################################################################################
class DMDarkLord(DMUnit):

    __slots__ = (
        "_state",
        "_max_mana",
        "_deployed",
        "_current_mana"
    )

################################################################################
    def __init__(self, game: DMGame):

        super().__init__(
            game,
            "DRK-LRD",
            "Elizabeth",
            None,
            225,
            28,
            12,
            1.0,
            1,
            rank=10,
            graphics=DarkLordGraphical(self)
        )

        self._max_mana = 10
        self._current_mana = 10
        self._deployed = True  # Always true here

        self._mover = None

################################################################################
    def draw(self, screen: Surface) -> None:

        self.graphics.draw(screen)

################################################################################
    def increase_max_mana(self, amount: int) -> None:

        self._max_mana += amount
        self.restore_mana(amount)

################################################################################
    @property
    def current_mana(self) -> int:

        return self._current_mana

################################################################################
    def consume_mana(self, amount: int) -> None:

        self._current_mana = max(self._current_mana - amount, 0)

################################################################################
    def reset_mana(self) -> None:

        self._current_mana = 0

################################################################################
    def restore_mana(self, amount: int) -> None:

        self._current_mana = min(self._current_mana + amount, self._max_mana)

################################################################################
    def heal(self, amount: Union[int, float]) -> None:

        relic = self.game.get_relic("Healing Necklace")
        if relic is not None:
            amount *= 1.25  # Adds 25% additional healing

        super().heal(amount)

################################################################################
    def deploy(self, room: DMRoom) -> None:

        self.room = room

################################################################################
