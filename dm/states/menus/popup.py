from __future__ import annotations

from pygame         import Surface
from pygame.font    import Font
from typing         import TYPE_CHECKING, Optional

from dm.core.states.state      import DMState
from utilities          import *

if TYPE_CHECKING:
    from pygame.event   import Event

    from dm.core.game.game import DMGame
################################################################################

__all__ = ("PopupDialogState",)

################################################################################
class PopupDialogState(DMState):

    __slots__ = (
        "_title",
        "_text",
        "_surface"
    )

################################################################################
    def __init__(
        self,
        game: DMGame,
        title: Optional[str] = None,
        text: Optional[str] = None
    ):

        super().__init__(game)

        self._title: Optional[str] = title
        self._text: Optional[str] = text

        self._surface: Surface = Surface((600, 450))

################################################################################
    @property
    def title(self) -> Optional[Surface]:

        if self._title is None:
            return

        return Font("assets/fonts/raleway.ttf", 40).render(self._title, True, BLACK)

################################################################################
    @property
    def text(self) -> Optional[Surface]:

        if self._text is None:
            return

        font = Font("assets/fonts/raleway.ttf", 30)

        text_surf = Surface((400, 300))
        text_surf.fill(BROWN)
        text_dict = text_to_multiline_rect(
            self._text,
            text_surf.get_rect(),
            30,
            font.render(self._text, True, BLACK).get_height()
        )

        for text, text_rect in text_dict.items():
            text_surface = font.render(text, True, BLACK)

            # Center the text within its rectangle by adjusting its x position
            text_pos = text_surface.get_rect(center=text_rect.center)

            text_surf.blit(text_surface, text_pos)

        return text_surf

################################################################################
    @property
    def confirm_text(self) -> Surface:

        return Font(None, 42).render("Confirm", True, WHITE)

################################################################################
    def handle_event(self, event: Event) -> None:

        super().handle_event(event)

        # Check for user input here
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                self.quit = True

################################################################################
    def update(self, dt: float) -> None:

        pass

################################################################################
    def draw(self, screen: Surface) -> None:

        screen.fill(TINTED)
        self._surface.fill(BROWN)

        surf_center_x = self._surface.get_width() // 2

        title_offset = 0
        if self.title is not None:
            title_rect = self.title.get_rect(center=(surf_center_x, self._surface.get_height() * 0.20))
            title_offset = title_rect.height
            self._surface.blit(self.title, title_rect)

        if self.text is not None:
            text_rect = self.text.get_rect(centerx=surf_center_x,
                                           y=(self._surface.get_height() * 0.20) + title_offset + 8)
            self._surface.blit(self.text, text_rect)

        confirm_surf = Surface((self._surface.get_width() * 0.35, 70))
        confirm_surf.fill(CONFIRM_BG)
        center_text(confirm_surf, self.confirm_text)

        confirm_pos = (self._surface.get_width() * 0.15, self._surface.get_height() * 0.70)

        size = confirm_surf.get_size()
        highlight_surf = Surface((size[0] + 6, size[1] + 6))
        highlight_surf.fill(RED)
        highlight_rect = highlight_surf.get_rect(center=confirm_pos)
        highlight_rect.x += confirm_surf.get_width() // 2
        highlight_rect.y += confirm_surf.get_height() // 2

        self._surface.blit(highlight_surf, highlight_rect)
        self._surface.blit(confirm_surf, confirm_pos)

        self_rect = self._surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(self._surface, self_rect)

################################################################################
    def set_title(self, text: str) -> None:

        self._title = text

################################################################################
    def set_text(self, text: str) -> None:

        self._text = text

################################################################################
