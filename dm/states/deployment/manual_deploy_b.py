from __future__ import annotations

from pygame         import Rect, Surface
from pygame.font    import Font
from typing         import TYPE_CHECKING, List, Optional

from ...core.infocards  import DMInfoCard
from ...core.states     import DMState
from utilities          import *

if TYPE_CHECKING:
    from pygame.event   import Event

    from dm.core    import DMGame, DMRoom
################################################################################

__all__ = ("ManualDeployStateB",)

################################################################################
class ManualDeployStateB(DMState):

    __slots__ = (
        "_room",
        "_infocard",
        "_info_surface",
        "_grid_surface",
        "_title",
        "_title_text",
        "_selection",
        "_options"
    )

################################################################################
    def __init__(self, game: DMGame):

        super().__init__(game)

        self.game.dungeon.map.reset_cursor_location()
        self._room: DMRoom = game.dungeon.get_highlighted_room()
        self._infocard: DMInfoCard = DMInfoCard(
            game,
            self.game.spawn(obj_id="BTL-101", init_obj=True),
            description=True,
            rank=True,
            stats=False,
            level=True
        )

        self._info_surface: Optional[Surface] = None
        # self._grid_surface: Optional[Surface] = None
        self._title: Optional[Surface] = None
        self._title_text: str = "Selected Room"

        self._options: List[str] = ["Deploy Monsters", "Withdraw Monsters", "Go Back"]
        self._selection: int = 0

################################################################################
    def handle_event(self, event: Event) -> None:

        super().handle_event(event)

        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                self._selection = min(self._selection + 1, len(self._options) - 1)
            elif event.key == K_UP:
                self._selection = max(self._selection - 1, 0)
            elif event.key == K_RETURN:
                if self._selection == 0:
                    pass
                elif self._selection == 1:
                    pass
                elif self._selection == 2:
                    self.quit = True

################################################################################
    def update(self, dt: float) -> None:

        pass

################################################################################
    def draw(self, screen: Surface) -> None:

        screen.fill(BLACK)

        info_rect = self.draw_info_surface()

        # grid_surface = Surface((SCREEN_WIDTH * 0.70, SCREEN_HEIGHT))
        # grid_rect = grid_surface.get_rect(topleft=(SCREEN_WIDTH * 0.30, 0))
        # grid_surface.fill(BLACK)

        screen.blit(self._info_surface, info_rect)
        # screen.blit(grid_surface, grid_rect)

################################################################################
    def draw_info_surface(self) -> Rect:

        self._info_surface = Surface((SCREEN_WIDTH * 0.30, SCREEN_HEIGHT))
        info_rect = self._info_surface.get_rect(topleft=(0, 0))
        self._info_surface.fill(BLACK)

        card_rect = self._infocard._surface.get_rect()
        card_rect.center = info_rect.center
        card_rect.y -= 100

        self.draw_title()
        self.draw_options()

        self._infocard.draw(self._info_surface, card_rect.x, card_rect.y)

        return info_rect

################################################################################
    # def draw_grid_surface(self) -> Rect:
    #
    #     self._grid_surface = Surface((SCREEN_WIDTH * 0.70, SCREEN_HEIGHT))
    #     grid_rect = self._grid_surface.get_rect(topleft=(0, 0))
    #     self._grid_surface.fill(BLACK)
    #
    #     upper_surf = Surface((self._grid_surface.get_width(), self._grid_surface.get_height() // 2))
    #     lower_surf = Surface((self._grid_surface.get_width(), self._grid_surface.get_height() // 2))
    #
    #     self.handle_upper_grid_surface()
    #     self.handle_lower_grid_surface()
    #
    #     self._grid_surface.blit(upper_surf, (0, 0))
    #     self._grid_surface.blit(lower_surf, (0, self._grid_surface.get_height() // 2))
    #
    #     return grid_rect

################################################################################
    def draw_title(self) -> None:

        self._title = Font(None, 48).render(self._title_text, True, WHITE)

        title_rect = self._title.get_rect()
        title_rect.center = self._info_surface.get_rect().center
        title_rect.y -= self._info_surface.get_height() * 0.40

        self._info_surface.blit(self._title, title_rect)

################################################################################
    def draw_options(self) -> None:

        font = Font(None, 32)

        rendered = []
        for i, option in enumerate(self._options):
            color = RED if i == self._selection else WHITE
            rendered.append(font.render(option, True, color))

        options_surf = Surface((self._info_surface.get_width(), self._info_surface.get_height() * 0.2))
        options_surf.fill(BLACK)

        for i, option in enumerate(rendered):
            # Calculate the position for each option
            x = (options_surf.get_width() - option.get_width()) // 2
            y = i * (options_surf.get_height() // len(rendered)) + (
                        (options_surf.get_height() // len(rendered) - option.get_height()) // 2)

            # Draw the text on the surface
            options_surf.blit(option, (x, y))

            # Then blit options_surf onto thr main surface
        x = (self._info_surface.get_width() - options_surf.get_width()) // 2

        self._info_surface.blit(options_surf, (x, 450))

################################################################################
    def set_title(self, text: str) -> None:

        self._title_text = text

################################################################################
    def handle_upper_grid_surface(self) -> None:

        pass

################################################################################
    def handle_lower_grid_surface(self) -> None:

        pass

################################################################################
