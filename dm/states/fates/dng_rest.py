from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.states      import DMState

if TYPE_CHECKING:
    from pygame         import Surface
    from pygame.event   import Event
################################################################################

__all__ = ("DungeonRestFate",)

################################################################################
class DungeonRestFate(DMState):

    def handle_event(self, event: Event) -> None:

        pass

################################################################################
    def update(self, dt: float) -> None:

        # Heals the Dark Lord for 30% of max health.
        self.game.dark_lord.heal(self.game.dark_lord.max_life * 0.30)

        # Then move on to the next day.
        self.game.advance_day()

################################################################################
    def draw(self, screen: Surface) -> None:

        pass

################################################################################
