from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.states      import DMState
from utilities          import *

if TYPE_CHECKING:
    from pygame         import Surface
    from pygame.event   import Event

    from ...core.game.game    import DMGame
################################################################################

__all__ = ("BattleState",)

################################################################################
class BattleState(DMState):

    def __init__(self, game: DMGame):

        super().__init__(game)

        # self.game.battle_mgr.engage(
        #     self.game.inventory.get_random_inventory_monster(),
        #     self.game.inventory.get_random_inventory_monster()
        # )

################################################################################
    def handle_event(self, event: Event) -> None:

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                # Pause
                pass

################################################################################
    def draw(self, screen: Surface) -> None:

        screen.fill(BLACK)

        self.game.battle_mgr.draw(screen)

################################################################################
    def update(self, dt: float) -> None:

        self.game.battle_mgr.update(dt)

################################################################################
