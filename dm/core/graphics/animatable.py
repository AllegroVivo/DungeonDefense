from __future__ import annotations

import pygame

from pygame     import Rect, Surface
from typing     import TYPE_CHECKING, List, Optional, Tuple, Type, TypeVar

from ._graphical    import GraphicalComponent

if TYPE_CHECKING:
    from dm.core    import DMObject
################################################################################

__all__ = ("AnimatableComponent",)

AC = TypeVar("AC", bound="AnimatableComponent")

################################################################################
class AnimatableComponent(GraphicalComponent):

    __slots__ = (
        "frame_count",
        "frame_size",
        "frames",
        "_current_frame",
        "cooldown",
        "spritesheet"
    )

################################################################################
    def __init__(
        self,
        parent: DMObject,
        num_frames: int,
        frame_size: Optional[Tuple[int, int]]
    ):

        super().__init__(parent)

        self.spritesheet: Optional[Surface] = None

        self.frame_count: int = num_frames
        self.frame_size: Optional[Tuple[int, int]] = frame_size
        self.frames: List[Surface] = []
        self._current_frame: int = 0
        self.cooldown: float = 0

################################################################################
    def _assert_frame_size(self) -> None:

        if self.frame_size is None:
            sheet_width, sheet_height = self.spritesheet.get_size()
            self.frame_size = sheet_width // self.frame_count, sheet_height

################################################################################
    def load_sprites(self) -> None:

        if self.idle is None:
            self.idle = pygame.image.load(
                f"{self.base_dir}/{self.subdirectory}/{self.parent.__class__.__name__.lower()}/static.png"
            )
            self.idle = pygame.transform.flip(self.idle, True, False)
        if self.spritesheet is None:
            self.spritesheet = pygame.image.load(
                f"{self.base_dir}/{self.subdirectory}/{self.parent.__class__.__name__.lower()}/idle.png"
            )
            self._assert_frame_size()
            self._split_spritesheet()

################################################################################
    def update(self, dt: float) -> None:

        self.cooldown += dt
        if self.cooldown >= 0.1:  # Assuming 10 FPS for the animation
            self.cooldown = 0
            self._current_frame = (self._current_frame + 1) % len(self.frames)

################################################################################
    def _split_spritesheet(self) -> None:

        self.frames = []
        for i in range(self.frame_count):
            frame_location = (i * self.frame_size[0], 0)
            self.frames.append(self.spritesheet.subsurface(Rect(frame_location, self.frame_size)))

################################################################################
    @property
    def current_frame(self) -> Surface:

        return self.frames[self._current_frame]

################################################################################
    def _copy(self) -> AnimatableComponent:
        """Returns a clean copy of the current object's animation data.

        There are no kwargs available for this implementation.

        Returns:
        --------
        :class:`AnimatableComponent`
            A fresh copy of the current Animatable component.
        """

        new_obj: Type[AC] = super()._copy()  # type: ignore

        new_obj.spritesheet = self.spritesheet

        new_obj.frame_count = self.frame_count
        new_obj.frame_size = self.frame_size
        new_obj.frames = self.frames

        new_obj._current_frame = 0
        new_obj.cooldown = 0

        return new_obj

################################################################################
