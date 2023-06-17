from __future__ import annotations

from pygame         import Surface
from pygame.font    import Font
from typing         import TYPE_CHECKING, List

from ...core.states import DMState
from utilities      import *

if TYPE_CHECKING:
    from dm.core        import DMFateCard, DMGame
    from pygame.event   import Event
################################################################################

__all__ = ("FateCardSelectState",)

################################################################################
class FateCardSelectState(DMState):

    def __init__(self, game: DMGame):

        super().__init__(game)

        self.options = self.game.fateboard.get_next_three_cards()
        self.selection: int = 0

################################################################################
    def handle_event(self, event: Event) -> None:

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                self.selection = max(self.selection - 1, 0)
            elif event.key == K_RIGHT:
                self.selection = min(self.selection + 1, 2)
            elif event.key == K_END:
                self.next_state = "fate_board_view"
            elif event.key == K_RETURN:
                card = self.options[self.selection]
                if card.name == "Rest":
                    self.game.state_machine.switch_state(card.next_state)

################################################################################
    def draw(self, screen: Surface) -> None:

        screen.fill(BLACK)

        upper_surface = Surface((SCREEN_WIDTH * 0.70, SCREEN_HEIGHT * 0.60))
        lower_surface = Surface((SCREEN_WIDTH * 0.70, SCREEN_HEIGHT * 0.40))

        upper_surface.fill(BLACK)
        lower_surface.fill(BLACK)

        font = Font(None, 60)
        text = font.render("Select Your Fate...", True, WHITE)
        text_rect = text.get_rect(centerx=lower_surface.get_rect().centerx, y=0)
        lower_surface.blit(text, text_rect)

        for i, card in enumerate(self.options):
            card.draw_large(upper_surface, i == self.selection)

        screen.blit(upper_surface, (0, 0))
        screen.blit(lower_surface, (0, SCREEN_HEIGHT * 0.60))

################################################################################
    def update(self, dt: float) -> None:

        pass

################################################################################
    def get_next_three_cards(self) -> List[DMFateCard]:

        return self.game.fateboard.get_next_three_cards()

################################################################################
