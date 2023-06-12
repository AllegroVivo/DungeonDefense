from __future__ import annotations

import pygame.image
from pygame         import Surface, Vector2
from pygame.font    import Font
from typing         import TYPE_CHECKING, Literal, Optional, Tuple

from ._component    import InfoCardComponent
from utilities      import *

if TYPE_CHECKING:
    from dm.core    import DMInfoCard
################################################################################

__all__ = ("InfoCardStats",)

################################################################################
class InfoCardStats(InfoCardComponent):

    __slots__ = (
        "_life_sprite",
        "_attack_sprite",
        "_defense_sprite",
        "_stat",
        "_font"
    )

################################################################################
    def __init__(self, parent: DMInfoCard):

        super().__init__(parent, (65, 50), Vector2(140, 70))

        self._life_sprite: Optional[Surface] = None
        self._attack_sprite: Optional[Surface] = None
        self._defense_sprite: Optional[Surface] = None

        self._font: Font = Font("assets/fonts/raleway.ttf", 12)

        self.prepare_surface()

################################################################################
    def prepare_surface(self) -> None:

        self._life_sprite = pygame.image.load(f"assets/sprites/misc/life.png")
        self._life_sprite = pygame.transform.scale(self._life_sprite, (16, 14))

        self._attack_sprite = pygame.image.load(f"assets/sprites/misc/attack.png")
        self._attack_sprite = pygame.transform.scale(self._attack_sprite, (16, 14))

        self._defense_sprite = pygame.image.load(f"assets/sprites/misc/defense.png")
        self._defense_sprite = pygame.transform.scale(self._defense_sprite, (16, 14))

        self._surface.set_colorkey(BLACK)

        self._life_sprite.set_colorkey(BLACK)
        self._attack_sprite.set_colorkey(BLACK)
        self._defense_sprite.set_colorkey(BLACK)

################################################################################
    def render(self, screen: Surface) -> None:

        # Apply the sprites at x = 80% of the surface length
        for i, sprite in enumerate((self._life_sprite, self._attack_sprite, self._defense_sprite)):
            sprite_x = self._surface.get_width() - sprite.get_width() - 17
            y_pos = i * sprite.get_height()  # Here, we no longer add the position of the parent surface

            self._surface.blit(sprite, (sprite_x, y_pos))

            # Then render the text.
            if self.text is None:
                return

            # Subtract the width of the text from the sprite's x position to get the x position for the text
            text_x = sprite_x - self.text(i).get_width() - 3  # type: ignore
            self._surface.blit(self.text(i), (text_x, y_pos))  # type: ignore

        screen.blit(self.surface, self._position)

################################################################################
    def text(self, index: int) -> Optional[Surface]:

        match index:
            case 0:
                value = self.parent_obj.life  # type: ignore
            case 1:
                value = self.parent_obj.attack  # type: ignore
            case 2:
                value = int(self.parent_obj.defense)  # type: ignore
            case _:
                return

        return self._font.render(str(value), True, WHITE)  # type: ignore

################################################################################
