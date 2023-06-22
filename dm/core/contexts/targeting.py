from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from .context import Context
from utilities import ArgumentTypeError

if TYPE_CHECKING:
    from dm.core.game.game    import DMGame
    from dm.core.objects.object import DMObject
    from dm.core.objects.unit import DMUnit
    from dm.core.objects.room import DMRoom
################################################################################

__all__ = ("TargetingContext",)

################################################################################
class TargetingContext(Context):

    __slots__ = (
        "_target",
        "_override"
    )

################################################################################
    def __init__(self, state: DMGame, source: DMObject, target: DMUnit):

        super().__init__(state)

        self._source: DMObject = source
        self._target: DMUnit = target

        self._override: Optional[DMUnit] = None

################################################################################
    @property
    def source(self) -> DMObject:

        return self._source

################################################################################
    @property
    def target(self) -> DMUnit:

        return self._target

################################################################################
    @property
    def room(self) -> DMRoom:

        # In the event of things like monsters and rooms, there will be a room
        # property. In the event of things like relics, there will not be a room
        # property, so in that case we'll just use the room of the target unit.
        try:
            return self._source.room
        except NotImplementedError:
            return self._target.room

################################################################################
    def execute(self) -> Optional[DMUnit]:

        self._state.dispatch_event("on_target", self)
        return self._override or self._target

################################################################################
    def override(self, override: DMUnit) -> None:

        if not issubclass(type(override), type(self._target)):
            raise ArgumentTypeError(
                "TargetingContext.override_target()",
                type(override),
                type(self._target)  # This definitely needs to be changed
            )

        self._override = override

################################################################################
