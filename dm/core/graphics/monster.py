from __future__ import annotations

import pygame

from pygame     import Surface
from typing     import TYPE_CHECKING, Optional, Tuple, Type, TypeVar

from .animatable    import AnimatableComponent
from utilities      import *

if TYPE_CHECKING:
    from dm.core    import DMObject
################################################################################

__all__ = ("MonsterGraphical",)

MG = TypeVar("MG", bound="MonsterGraphical")

################################################################################
class MonsterGraphical(AnimatableComponent):

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
                f"{self.base_dir}/monsters/{self.parent.__class__.__name__.lower()}/attack.png"
            )
            self.attack = pygame.transform.flip(self.attack, True, False)
        if self.zoom is None:
            self.zoom = pygame.image.load(
                f"{self.base_dir}/monsters/{self.parent.__class__.__name__.lower()}/zoom.png"
            )

        self.spritesheet = pygame.transform.flip(self.spritesheet, True, False)
        self._split_spritesheet()

################################################################################
    @property
    def subdirectory(self) -> str:

        return "monsters"

################################################################################
    def topleft(self, index: Optional[int] = None) -> Tuple[int, int]:

        parent_room = self.parent.room  # type: ignore
        room_x, room_y = parent_room.graphics.topleft
        monster_spacing = ROOM_SIZE / (len(parent_room.monsters) + 1)

        if index is None:
            raise ValueError("Index must be provided for MonsterGraphical")

        monster_x = room_x
        monster_y = room_y - 20 + monster_spacing * (index + 1)

        return monster_x, monster_y

################################################################################
    @property
    def card_sprite(self) -> Surface:

        return self.idle

################################################################################
    def _copy(self) -> MonsterGraphical:
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

        room = self.parent.room  # type: ignore
        idx = room.monsters.index(self.parent)
        screen.blit(self.current_frame, self.topleft(idx))

################################################################################
