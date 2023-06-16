from __future__ import annotations

from pygame         import Surface
from pygame.font    import Font
from typing         import TYPE_CHECKING

from ..core.states      import DMState
from utilities          import *

if TYPE_CHECKING:
    from pygame.event   import Event

    from ..core.game.game import DMGame
################################################################################

__all__ = ("_DebugState",)

################################################################################
class _DebugState(DMState):

    def __init__(self, game: DMGame):

        super().__init__(game)

        monster1 = self.game.inventory.get_random_inventory_monster()
        monster2 = self.game.inventory.get_random_inventory_monster()
        while monster1 == monster2:
            monster2 = self.game.inventory.get_random_inventory_monster()

        self.game.battle_mgr.engage(monster1, monster2)
        self.count = 0

################################################################################
    def handle_event(self, event: Event) -> None:

        if event.type == KEYDOWN:
            # if event.key == K_SPACE:
            #     # Pause
            #     pass
            if event.key == K_RETURN:
                self.count += 1
                self._add_status_debug()
            elif event.key == K_SPACE:
                self.game.battle_mgr.update(1)
            # elif event.key == K_BACKSPACE:
            #     self.count = max(self.count - 1, 0)
            #     self._add_status_debug()

################################################################################
    def _add_status_debug(self) -> None:

        monster = self.game.battle_mgr._encounters[0]._attacker
        hero = self.game.battle_mgr._encounters[0]._defender

        # if self.count == 1:
        monster.add_status("Chained", stacks=3)

################################################################################
    def draw(self, screen: Surface) -> None:

        screen.fill(BLACK)

        atk_statuses = [
            f"{s.name}: {s.stacks}" for s in self.game.battle_mgr._encounters[0]._attacker.statuses
        ]
        total_height = len(atk_statuses) * 40
        start_y = (SCREEN_HEIGHT - total_height) / 2
        font = Font("assets/fonts/raleway.ttf", 40)

        atk_title = font.render("Attacker:", True, WHITE)
        x = ((SCREEN_WIDTH // 2) - atk_title.get_width()) / 2
        screen.blit(atk_title, (x, 50))
        for i, string in enumerate(atk_statuses):
            text_surface = font.render(string, True, WHITE)
            # Center horizontally in the screen
            x = ((SCREEN_WIDTH // 2) - text_surface.get_width()) / 2
            # Stack vertically
            y = start_y + i * 40
            screen.blit(text_surface, (x, y))

        def_statuses = [
            f"{s.name}: {s.stacks}" for s in self.game.battle_mgr._encounters[0]._defender.statuses
        ]

        total_height = len(def_statuses) * 40
        start_y = ((SCREEN_HEIGHT - total_height) / 2)
        font = Font("assets/fonts/raleway.ttf", 40)

        def_title = font.render("Defender:", True, WHITE)
        x = (((SCREEN_WIDTH // 2) - def_title.get_width()) / 2) + (SCREEN_WIDTH // 2)
        screen.blit(def_title, (x, 50))
        for i, string in enumerate(def_statuses):
            text_surface = font.render(string, True, WHITE)
            # Center horizontally in the screen
            x = (((SCREEN_WIDTH // 2) - text_surface.get_width()) / 2) + (SCREEN_WIDTH // 2)
            # Stack vertically
            y = start_y + i * 40
            screen.blit(text_surface, (x, y))

        # self.game.battle_mgr.draw(screen)

################################################################################
    def update(self, dt: float) -> None:

        pass
        # self.game.battle_mgr.update(dt)

################################################################################
