from __future__ import annotations

import pygame

from pygame     import Surface
from typing     import TYPE_CHECKING, Optional, Tuple, Type, TypeVar

from .animatable    import AnimatableComponent
from utilities      import *

if TYPE_CHECKING:
    from dm.core    import DMDarkLord
################################################################################

__all__ = ("DarkLordGraphical",)

DLG = TypeVar("DLG", bound="DarkLordGraphical")

################################################################################
class DarkLordGraphical(AnimatableComponent):

    def __init__(
        self,
        parent: DMDarkLord,
        num_frames: int = 5,
        frame_size: Optional[Tuple[int, int]] = None
    ):

        super().__init__(parent, num_frames, frame_size)

        self.load_sprites()

################################################################################
    def load_sprites(self) -> None:

        if self.idle is None:
            self.idle = pygame.image.load(
                f"{self.base_dir}/{self.subdirectory}/static.png"
            )
            self.idle = pygame.transform.flip(self.idle, True, False)
            self.idle = pygame.transform.scale(
                self.idle, (self.idle.get_width() * 1.5, self.idle.get_height() * 1.5)
            )
        if self.spritesheet is None:
            self.spritesheet = pygame.image.load(
                f"{self.base_dir}/{self.subdirectory}/idle.png"
            )
            self.spritesheet = pygame.transform.scale(
                self.spritesheet,
                (self.spritesheet.get_width() * 2, self.spritesheet.get_height() * 2)
            )
        if self.attack is None:
            self.attack = pygame.image.load(
                f"{self.base_dir}/{self.subdirectory}/attack.png"
            )
            self.attack = pygame.transform.flip(self.attack, True, False)
            self.attack = pygame.transform.scale(
                self.attack, (self.attack.get_width() * 1.5, self.attack.get_height() * 1.5)
            )
        if self.death is None:
            self.death = pygame.image.load(
                f"{self.base_dir}/{self.subdirectory}/death.png"
            )
            self.death = pygame.transform.scale(
                self.death, (self.death.get_width() * 1.5, self.death.get_height() * 1.5)
            )

        self._assert_frame_size()
        self.spritesheet = pygame.transform.flip(self.spritesheet, True, False)
        self._split_spritesheet()

################################################################################
    @property
    def subdirectory(self) -> str:

        return "darklord/elizabeth"

################################################################################
    def topleft(self, index: Optional[int] = None) -> Tuple[int, int]:

        parent_room = self.parent.room  # type: ignore
        room_y, room_x = parent_room.graphics.topleft
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
    def draw(self, screen: Surface) -> None:

        dl_rect = self.current_frame.get_rect()
        dl_rect.center = (0, self.parent.game.dungeon.map.boss_tile.get_rect().center[1])
        dl_rect.x += 70
        dl_rect.y -= 25

        screen.blit(self.current_frame, dl_rect)

################################################################################
