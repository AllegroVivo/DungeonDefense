from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.states      import DMState
from utilities          import *

if TYPE_CHECKING:
    from pygame         import Surface
    from pygame.event   import Event

    from ...core.game.game    import DMGame
################################################################################

__all__ = ("Template",)

################################################################################
class Template(DMState):
    __slots__ = (

    )

################################################################################
    def __init__(self, game: DMGame):

        super().__init__(game)

################################################################################
    def handle_event(self, event: Event) -> None:

        pass

################################################################################
    def update(self, dt: float) -> None:

        pass

################################################################################
    def draw(self, screen: Surface) -> None:

        pass

################################################################################
