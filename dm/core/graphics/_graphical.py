from __future__ import annotations

from pygame     import Surface
from typing     import TYPE_CHECKING, Optional, Tuple, Type, TypeVar

if TYPE_CHECKING:
    from dm.core.objects.object    import DMObject
################################################################################

__all__ = ("GraphicalComponent",)

GC = TypeVar("GC", bound="GraphicalComponent")

################################################################################
class GraphicalComponent:

    __slots__ = (
        "parent",
        "idle",
        "attack",
        "death",
    )

################################################################################
    def __init__(self, parent: DMObject):

        self.parent: DMObject = parent

        self.idle: Optional[Surface] = None
        self.attack: Optional[Surface] = None
        self.death: Optional[Surface] = None

################################################################################
    @property
    def base_dir(self) -> str:

        return "assets/sprites"

################################################################################
    @property
    def subdirectory(self) -> str:

        raise NotImplementedError

################################################################################
    def load_sprites(self) -> None:

        raise NotImplementedError

################################################################################
    def draw(self, screen: Surface) -> None:

        raise NotImplementedError

################################################################################
    def update(self, dt: float) -> None:

        pass

################################################################################
    def topleft(self, pos: Optional[int] = None) -> Tuple[int, int]:

        raise NotImplementedError

################################################################################
    @property
    def card_sprite(self) -> Surface:

        return self.idle

################################################################################
    def _copy(self) -> GraphicalComponent:
        """Returns a clean copy of the current object's graphics data.

        There are no kwargs available for this implementation.

        Returns:
        --------
        :class:`GraphicalComponent`
            A fresh copy of the current Graphical component.
        """

        cls: Type[GC] = type(self)
        new_obj = cls.__new__(cls)

        new_obj.parent = self.parent

        new_obj.idle = self.idle
        new_obj.attack = self.attack
        new_obj.death = self.death

        return new_obj

################################################################################
