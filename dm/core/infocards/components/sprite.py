from __future__ import annotations

import pygame

from pygame         import Surface, Vector2
from typing         import TYPE_CHECKING, Optional

from ._component        import InfoCardComponent
from ...objects.room    import DMRoom
from utilities          import *

if TYPE_CHECKING:
    from dm.core    import DMInfoCard
################################################################################

__all__ = ("InfoCardMainSprite",)

################################################################################
class InfoCardMainSprite(InfoCardComponent):

    __slots__ = (
        "_flip",
        "_sprite"
    )

################################################################################
    def __init__(self, parent: DMInfoCard, flip_sprite: bool = False):

        super().__init__(
            parent,
            (parent.WIDTH * 0.90, parent.HEIGHT // 3),
            Vector2(parent.WIDTH * 0.05, parent.HEIGHT * 0.20)
        )

        self._flip: bool = flip_sprite
        self._sprite: Optional[Surface] = None
        self.prepare_surface()

################################################################################
    def prepare_surface(self) -> None:

        self._sprite = pygame.transform.scale(
            self.parent_obj.graphics.card_sprite,  # type: ignore
            (80, 60)
        )
        if isinstance(self.parent_obj, DMRoom):
            self._sprite = pygame.transform.rotate(self._sprite, -38)
            self._sprite = pygame.transform.scale(
                self._sprite,
                (self._sprite.get_width() * 0.75, self._sprite.get_height() * 0.75)
            )

        if self._flip:
            self._sprite = pygame.transform.flip(self._sprite, True, False)

################################################################################
    @property
    def room_scroll(self) -> Surface:

        raw = pygame.image.load("assets/sprites/misc/bgscroll3.png")
        image = pygame.transform.scale(
            raw, (150, 125)
        )
        image_rect = image.get_rect()
        image_rect.center = self._surface.get_rect().center

        return image

################################################################################
    def render(self, surface: Surface) -> None:

        surface_rect = self._surface.get_rect()
        obj_rect = self._sprite.get_rect()
        obj_rect.center = surface_rect.center
        obj_rect.y -= 25
        obj_rect.x -= 40

        if not isinstance(self.parent_obj, DMRoom):
            self._surface.blit(self._sprite, obj_rect.center)
        else:
            scroll_surface = self.room_scroll
            scroll_surface.blit(self._sprite, (38, 26))
            self._surface.blit(scroll_surface, (15, -10))

        surface.blit(self._surface, self._position)

################################################################################
