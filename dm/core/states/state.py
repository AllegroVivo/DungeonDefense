from __future__ import annotations

from abc        import ABC, abstractmethod
from typing     import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from dm.core.game import DMGame
    from pygame         import Surface
    from pygame.event   import Event
################################################################################

__all__ = ("DMState",)

################################################################################
class DMState:

    __slots__ = (
        "_game",
        "quit",
        "next_state",
    )

################################################################################
    def __init__(self, game: DMGame):

        self._game: DMGame = game
        self.quit: bool = False
        self.next_state: Optional[str] = None

################################################################################
    def __repr__(self) -> str:

        return f"<DMState: {self.__class__.__name__}>"

################################################################################
    @property
    def game(self) -> DMGame:

        return self._game

################################################################################
    @abstractmethod
    def handle_event(self, event: Event) -> None:

        # Make sure to override K_RETURN behavior in subclasses.
        pass

################################################################################
    @abstractmethod
    def update(self, dt: float) -> None:

        pass

################################################################################
    @abstractmethod
    def draw(self, screen: Surface) -> None:

        pass

################################################################################
