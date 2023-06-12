from __future__ import annotations

from pygame     import Surface
from typing     import TYPE_CHECKING, Optional, TypeVar

from .fighter   import DMFighter
from utilities  import *

if TYPE_CHECKING:
    from dm.core.game import DMGame
################################################################################

__all__ = ("DMHero",)

H = TypeVar("H", bound="DMHero")

################################################################################
class DMHero(DMFighter):

    __slots__ = (

    )

################################################################################
    def __init__(
        self,
        state: DMGame,
        *,
        _id: str,
        name: str,
        description: Optional[str] = None,
        rank: int = 1,
        unlock: Optional[UnlockPack] = None,
        life: int = 100,
        attack: int = 10,
        defense: float = 7.5,
        dex: float = 10,
        idle_frames: int = 5
    ):

        super().__init__(
            state, _id, name, description, life, attack, defense, dex,
            level=1, rank=rank, unlock=unlock, graphics=None
        )

################################################################################
    # def _copy(self, **kwargs) -> DMHero:
    #     """Returns a clean copy of the current hero type with any given
    #     kwargs substituted in.
    #
    #     All parameters are optional.
    #
    #     Parameters:
    #     -----------
    #     position: :class:`DMVector`
    #         The hero's starting position if not the dng_options entrance.
    #
    #     Returns:
    #     --------
    #     :class:`DMHero`
    #         A fresh copy of the current DMObject with values substituted as defined.
    #
    #     """
    #
    #     default_start_pos = DMVector(len(self.game.dungeon.map) // 2, len(self.game.dungeon.map[0]) - 1)
    #     start_pos = kwargs.pop("position", default_start_pos)
    #     if isinstance(start_pos, tuple):
    #         position = DMVector(start_pos[1], start_pos[0])
    #     elif isinstance(start_pos, DMVector):
    #         position = DMVector(start_pos.y, start_pos.x)
    #     else:
    #         raise ValueError("Invalid type passed to DMHero._copy().")
    #
    #     new_obj: Type[H] = super()._copy(**kwargs, position=position)  # type: ignore
    #
    #     rect = self.game.dungeon.get_room_rect(new_obj.current_cell)
    #     new_obj.current_pos = DMVector(rect.centerx, rect.centery)
    #
    #     new_obj.target_cell = DMVector(new_obj.current_cell.x - 1, new_obj.current_cell.y)
    #
    #     new_obj.counter = 0
    #
    #     # room_rect = self.game.dng_options.get_room_rect(new_obj.target_cell)
    #     # new_obj.target_pos = DMVector(room_rect.centerx, room_rect.centery)
    #
    #     return new_obj

################################################################################
    def update(self, dt: float) -> None:
        """Update the hero's position and animation."""

        pass

################################################################################
    def draw(self, screen: Surface) -> None:
        """Draws the hero on the screen."""

        pass

################################################################################
