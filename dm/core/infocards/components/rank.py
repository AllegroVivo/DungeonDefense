from __future__ import annotations

import pygame

from pygame         import Surface, Vector2
from typing         import TYPE_CHECKING, Optional

from ._component    import InfoCardComponent
from utilities      import *

if TYPE_CHECKING:
    from dm.core    import DMInfoCard
################################################################################

__all__ = ("InfoCardRank",)

################################################################################
class InfoCardRank(InfoCardComponent):

    __slots__ = (
        "_sprite",
    )

################################################################################
    def __init__(self, parent: DMInfoCard):

        super().__init__(
            parent,
            (parent.WIDTH, parent.HEIGHT // 5),
            Vector2(0, 235)
        )

        self._sprite: Optional[Surface] = None
        self.prepare_surface()

################################################################################
    def prepare_surface(self) -> None:

        base = "bronze" if self.parent_obj.rank <= 5 else "silver"
        base_image = pygame.image.load(f"assets/sprites/misc/{base}star.png")
        self._sprite = pygame.transform.scale(base_image, (16, 14))

################################################################################
    def render(self, screen: Surface) -> None:

        if self.parent_obj.rank == 0:
            return

        num_stars = self.parent_obj.rank
        star_size = self._sprite.get_size()
        spacing = 2

        total_width = num_stars * star_size[0] + (num_stars - 1) * spacing

        # Calculate the x position of the first star, such that the whole row will be centered
        first_star_x = ((self._size[0] - total_width) // 2) + 7  # 7 pixels centers it.

        # Calculate the y position of the stars, so that they are a certain distance from the bottom of the card
        stars_y = self._size[1] - star_size[1] - 7  # 7 pixels from the bottom - yes, very specific

        # Draw each star
        for i in range(num_stars):
            # Calculate the x position of this star
            star_x = first_star_x + i * (star_size[0] + spacing)

            # Create a rect for the star and set its center position
            star_rect = pygame.Rect(0, 0, *star_size)
            star_rect.center = (star_x, stars_y)

            # Draw the star
            self._surface.blit(self._sprite, star_rect)

        screen.blit(self.surface, self._position)

################################################################################
