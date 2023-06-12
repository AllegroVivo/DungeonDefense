from __future__ import annotations

from pygame.font    import Font
from typing         import TYPE_CHECKING

from dm.states._hrz_menu import HorizontalMenuState
from utilities      import *

if TYPE_CHECKING:
    from pygame         import Surface
    from pygame.event   import Event

    from dm.core.game import DMGame
################################################################################

__all__ = ("AutoDeployState",)

################################################################################
class AutoDeployState(HorizontalMenuState):

    def __init__(self, game: DMGame):

        super().__init__(
            game,
            ["Auto Deploy", "Manual Deploy", "Reset Monsters", "Confirm"],
            option_font=Font(None, 28),
            x_offset=-140,
            y_offset=200
        )

        self.game.dungeon.toggle_highlighting(False)

################################################################################
    def handle_event(self, event: Event) -> None:

        super().handle_event(event)

        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                if self.selection == 0:  # Auto-Deploy
                    self.game.dungeon.map.auto_deploy()
                elif self.selection == 1:
                    # Manual Placement
                    self.next_state = "manual_deploy_a"
                elif self.selection == 2:  # Reset Monsters
                    self.game.dungeon.map.reset_monster_deployment()
                elif self.selection == 3:
                    self.next_state = "fate_select"

################################################################################
    def update(self, dt: float) -> None:

        self.game.dungeon.update(dt)

################################################################################
    def draw(self, screen: Surface) -> None:

        screen.fill(BLACK)

        self.game.draw_dungeon()

        # Draw menu texts after dungeon is drawn.
        super().draw(screen)

################################################################################
