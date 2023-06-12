from __future__ import annotations

from pygame         import Surface, Vector2
from typing         import TYPE_CHECKING, Optional, Tuple

from utilities      import *

if TYPE_CHECKING:
    from dm.core    import DMGame, DMInfoCard, DMObject
################################################################################

__all__ = ("InfoCardComponent",)

################################################################################
class InfoCardComponent:

    __slots__ = (
        "_parent",
        "_surface",
        "_size",
        "_position"
    )

################################################################################
    def __init__(self, parent: DMInfoCard, size: Tuple[int, int], location_on_parent: Vector2):

        self._parent: DMInfoCard = parent

        self._size: Tuple[int, int] = size
        self._position: Vector2 = location_on_parent

        self._surface: Optional[Surface] = None

        # Always prepare the parent surface without needing to always call
        # super().prepare_surface() in each child class.
        self._surface = Surface(self._size)
        self._surface.set_colorkey(BLACK)

        self._parent._children.append(self)

################################################################################
    @property
    def surface(self) -> Surface:

        return self._surface

################################################################################
    @property
    def game(self) -> DMGame:

        return self._parent._state

################################################################################
    @property
    def parent_obj(self) -> DMObject:

        return self._parent._obj

################################################################################
    def prepare_surface(self) -> None:
        """Called after component initialization. Overload for image loading and processing."""

        pass

################################################################################
    def render(self, screen: Surface) -> None:
        """Process all surface-specific rendering in a way that will allow the
        `self.surface` property to return the finished Surface to be applied
        to the card."""

        raise NotImplementedError

################################################################################
    @property
    def card_width(self) -> int:

        return self._parent.WIDTH

################################################################################
    @property
    def card_height(self) -> int:

        return self._parent.HEIGHT

################################################################################
