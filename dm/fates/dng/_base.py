from __future__ import annotations

import pygame

from pygame     import Surface, Vector2
from typing     import TYPE_CHECKING

from ...core.fates  import DMFateCard
from ...core.graphics import DungeonFateGraphical
from utilities      import *

if TYPE_CHECKING:
    from ...core.game.game import DMGame
################################################################################

__all__ = ("DungeonFateCard",)

################################################################################
class DungeonFateCard(DMFateCard):

    FTYPE: FateType = FateType.Dungeon

    def __init__(
        self,
        game: DMGame,
        _id: str,
        name: str,
        description: str,
        next_state: str,
        position: Vector2
    ):

        super().__init__(game, _id, name, description, position, 0, next_state)

################################################################################
    def _load_sprites(self) -> None:

        self._large_sprite = DungeonFateGraphical(self)

################################################################################
    @property
    def screen_pos(self) -> Vector2:

        return Vector2(EDGE_PADDING // 2 + (self.position.x * (FATE_CARD_WIDTH + 125)), 100)

################################################################################
    def draw_large(self, surface: Surface, selected: bool) -> None:

        card_x, card_y = self.screen_pos

        if self.position.x > 2:  # If it's in the second set of cards
            # Reduce the spacing, not sure of the best way, so I just went the copy/pasta route
            card_x = EDGE_PADDING // 2 + ((self.position.x - 3) * (FATE_CARD_WIDTH + 125))
            # And increase y spacing to make a second row
            card_y += 200

        card_pos = Vector2(card_x, card_y)

        if selected:
            pygame.draw.rect(
                surface,
                RED,
                Rect(
                    card_pos.x - 3,
                    card_pos.y - 3,
                    self._large_sprite._sprite.get_width() + 6,
                    self._large_sprite._sprite.get_height() + 6
                )
            )

        self._large_sprite.draw(surface, card_pos)

################################################################################
