from __future__ import annotations

import pygame

from pygame     import Surface
from typing     import TYPE_CHECKING, Optional, Tuple, Type, TypeVar

from .animatable    import AnimatableComponent
from utilities      import *

if TYPE_CHECKING:
    from dm.core.objects.object    import DMObject
    from dm.core.rooms.room        import DMRoom
################################################################################

__all__ = ("MonsterGraphical",)

MG = TypeVar("MG", bound="MonsterGraphical")

################################################################################
class MonsterGraphical(AnimatableComponent):

    __slots__ = (
        "_zoom",
        "_swords",
        "_highlighted",
    )

################################################################################
    def __init__(
        self,
        parent: DMObject,
        num_frames: int = 5,
        frame_size: Optional[Tuple[int, int]] = None
    ):

        super().__init__(parent, num_frames, frame_size)

        self._zoom: Optional[Surface] = None
        self._swords: Optional[Surface] = None
        self._highlighted: bool = False

        self.load_sprites()

################################################################################
    def load_sprites(self) -> None:

        super().load_sprites()

        if self.attack is None:
            self.attack = pygame.image.load(
                f"{self.base_dir}/monsters/{self.parent.__class__.__name__.lower()}/attack.png"
            )
            self.attack = pygame.transform.flip(self.attack, True, False)
        if self._zoom is None:
            zoom = pygame.image.load(
                f"{self.base_dir}/monsters/{self.parent.__class__.__name__.lower()}/zoom.png"
            )
            self._zoom = Surface(zoom.get_size())
            self._zoom.fill(BLACK)
            self._zoom.blit(zoom, (0, 0))
            self._zoom = pygame.transform.scale(self._zoom, (self._zoom.get_width() * 1.5, self._zoom.get_height() * 1.5))

        self.spritesheet = pygame.transform.flip(self.spritesheet, True, False)
        self._split_spritesheet()

        self._swords = pygame.image.load("assets/sprites/misc/swords_wht.png")
        self._swords = pygame.transform.scale(self._swords, (10, 10))

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
    def inventory_topleft(self, index: Optional[int] = None) -> Tuple[int, int]:

        if index is None:
            raise ValueError("Index must be provided for MonsterGraphical")

        x_pos, y_pos = index, index // self.game.inventory.MONSTERS_PER_ROW
        if index >= self.game.inventory.MONSTERS_PER_ROW:
            x_pos -= self.game.inventory.MONSTERS_PER_ROW

        image_x = 30 + ((self._zoom.get_width() + 10) * x_pos)
        image_y = 50 + ((self._zoom.get_height() + 50) * y_pos)

        return image_x, image_y

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

        new_obj.zoom = self._zoom

        return new_obj

################################################################################
    def draw(self, screen: Surface) -> None:

        room = self.parent.room  # type: ignore
        idx = room.monsters.index(self.parent)
        screen.blit(self.current_frame, self.topleft(idx))

################################################################################
    def draw_zoom(self, screen: Surface) -> None:

        index = self.game.inventory.monsters.index(self.parent)  # Type: ignore

        zoom_surf = Surface(self._zoom.get_size())
        zoom_surf = pygame.transform.scale(zoom_surf, (zoom_surf.get_width() + 2, zoom_surf.get_height() + 2))
        zoom_surf.fill(ZOOM_BORDER)
        zoom_surf.blit(self._zoom, (1, 1))

        swords_rect = self._swords.get_rect(center=(zoom_surf.get_width() // 2, zoom_surf.get_height() - 8))
        zoom_surf.blit(self._swords, swords_rect)

        if self._highlighted:
            highlight_surf = Surface(self._zoom.get_size())
            highlight_surf = pygame.transform.scale(highlight_surf, (highlight_surf.get_width() +6, highlight_surf.get_height() + 6))
            highlight_surf.fill(RED)
            screen.blit(highlight_surf, (self.inventory_topleft(index)[0] - 2, self.inventory_topleft(index)[1] - 2))

        screen.blit(zoom_surf, self.inventory_topleft(index))

################################################################################
    def toggle_highlighting(self, value: bool) -> None:

        self._highlighted = value

################################################################################
