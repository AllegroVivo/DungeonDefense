from __future__ import annotations

import pygame

from pygame     import Rect, Surface, Vector2
from typing     import TYPE_CHECKING, Optional, Type, TypeVar

from ._graphical    import GraphicalComponent
from utilities      import *

if TYPE_CHECKING:
    from dm.core    import DMRoom
################################################################################

__all__ = ("RoomGraphical",)

RG = TypeVar("RG", bound="RoomGraphical")

################################################################################
class RoomGraphical(GraphicalComponent):

    __slots__ = (
        "_rect",
        "_highlighted",
    )

################################################################################
    def __init__(self, parent: DMRoom):

        super().__init__(parent)

        self._rect: Optional[Rect] = None
        self._highlighted: bool = False

        self.load_sprites()

################################################################################
    def load_sprites(self) -> None:

        self.idle = pygame.image.load(
            f"{self.base_dir}/rooms/{self.parent.__class__.__name__.lower()}.png"
        )
        if type(self.parent).__name__ != "BossRoom":
            self.idle = pygame.transform.scale(self.idle, (ROOM_SIZE - 30, ROOM_SIZE - 30))
        else:
            self.idle = pygame.transform.scale(self.idle, (ROOM_SIZE + 40, ROOM_SIZE + 25))

        # Flip the entry symbol. Looks better.
        if type(self.parent).__name__ == "EntranceRoom":
            self.idle = pygame.transform.flip(self.idle, True, False)

################################################################################
    def _copy(self) -> RoomGraphical:
        """Returns a clean copy of the current rooms's graphics data.

        There are no kwargs available for this implementation.

        Returns:
        --------
        :class:`RoomGraphic`
            A fresh copy of the current room's graphic component.
        """

        new_obj: Type[RG] = super()._copy()  # type: ignore

        new_obj._rect = self._rect.copy()
        new_obj._highlighted = False

        return new_obj

################################################################################
    def calculate_rect(self) -> Rect:

        self._rect = Rect(self.topleft[0], self.topleft[1], ROOM_SIZE, ROOM_SIZE)
        return self._rect

################################################################################
    def center(self) -> Vector2:

        if self._rect is not None:
            return Vector2(self._rect.center)

        return Vector2(-1, -1)

################################################################################
    @property
    def topleft(self, pos: Optional[int] = None) -> Vector2:

        return Vector2(
            self.parent.position.x * (ROOM_SIZE + GRID_PADDING) + 50,  # type: ignore
            self.parent.position.y * (ROOM_SIZE + GRID_PADDING) + 50   # type: ignore
        )

################################################################################
    def draw(self, screen: Surface) -> None:

        self.calculate_rect()
        bg = ROOM_BG if type(self.parent).__name__ != "EntranceRoom" else BLACK
        pygame.draw.rect(screen, bg, self._rect)  # type: ignore

        if self._highlighted:
            pygame.draw.rect(screen, RED, self._rect, BORDER_THICKNESS)

        idle_rect = self.idle.get_rect()
        idle_rect.center = self.center()
        screen.blit(self.idle, idle_rect)

################################################################################
    def toggle_highlighting(self, value: bool) -> None:

        self._highlighted = value

################################################################################
