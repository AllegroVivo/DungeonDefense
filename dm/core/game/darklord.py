from __future__ import annotations

from pygame     import Surface
from typing     import TYPE_CHECKING

from dm.core.objects.fighter import DMFighter
from ..graphics.darklord    import DarkLordGraphical

if TYPE_CHECKING:
    from .game  import DMGame
################################################################################

__all__ = ("DMDarkLord",)

################################################################################
class DMDarkLord(DMFighter):

    __slots__ = (
        "_state",
        "_max_mana",
        "current_mana"
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
        self.current_mana = 10

################################################################################
    def draw(self, screen: Surface) -> None:

        self.graphics.draw(screen)

################################################################################
    def increase_max_mana(self, amount: int) -> None:

        self._max_mana += amount
        self.restore_mana(amount)

################################################################################
    def consume_mana(self, amount: int) -> None:

        self.current_mana = max(self.current_mana - amount, 0)

################################################################################
    def restore_mana(self, amount: int) -> None:

        self.current_mana = min(self.current_mana + amount, self._max_mana)

################################################################################
