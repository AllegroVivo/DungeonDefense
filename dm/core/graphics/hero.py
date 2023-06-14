from __future__ import annotations

import pygame

from pygame     import Surface, Vector2
from typing     import TYPE_CHECKING, Optional, Tuple, Type, TypeVar

from .animatable    import AnimatableComponent
from utilities      import *

if TYPE_CHECKING:
    from dm.core    import DMObject, DMRoom
################################################################################

__all__ = ("HeroGraphical",)

MG = TypeVar("MG", bound="MonsterGraphical")

################################################################################
class HeroGraphical(AnimatableComponent):

    __slots__ = (
        "zoom",
    )

################################################################################
    def __init__(
        self,
        parent: DMObject,
        num_frames: int = 5,
        frame_size: Optional[Tuple[int, int]] = None
    ):

        super().__init__(parent, num_frames, frame_size)

        self.zoom: Optional[Surface] = None

        self.load_sprites()

################################################################################
    def load_sprites(self) -> None:

        super().load_sprites()

        if self.attack is None:
            self.attack = pygame.image.load(
                f"{self.base_dir}/heroes/{self.parent.__class__.__name__.lower()}/attack.png"
            )
            self.attack = pygame.transform.flip(self.attack, True, False)
        if self.zoom is None:
            self.zoom = pygame.image.load(
                f"{self.base_dir}/heroes/{self.parent.__class__.__name__.lower()}/zoom.png"
            )

        # self.spritesheet = pygame.transform.flip(self.spritesheet, True, False)
        # self._split_spritesheet()

################################################################################
    @property
    def subdirectory(self) -> str:

        return "heroes"

################################################################################
    @property
    def room(self) -> DMRoom:

        return self.parent.room  # type: ignore

################################################################################
    @property
    def position(self) -> Vector2:

        return self.parent.screen_position  # type: ignore

################################################################################
    @property
    def card_sprite(self) -> Surface:

        return self.idle

################################################################################
    def _copy(self) -> HeroGraphical:
        """Returns a clean copy of the current monster's graphics and animation data.

        There are no kwargs available for this implementation.

        Returns:
        --------
        :class:`MonsterGraphical`
            A fresh copy of the a :class:`DMMonster`'s graphics component.
        """

        new_obj: Type[MG] = super()._copy()  # type: ignore

        new_obj.zoom = self.zoom

        return new_obj

################################################################################
    def draw(self, screen: Surface) -> None:

        # Adjust the position to center the hero
        hero_center_pos = self.position - Vector2(self.current_frame.get_size()) / 2

        # Draw the hero at the calculated position
        screen.blit(self.current_frame, hero_center_pos)

################################################################################
