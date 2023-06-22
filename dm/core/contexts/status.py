from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.contexts.context import Context

if TYPE_CHECKING:
    from dm.core.game.game    import DMGame
    from dm.core.objects.unit   import DMUnit
    from dm.core.objects.status       import DMStatus
    from dm.core.objects.object import DMObject
################################################################################

__all__ = ("StatusAcquireContext",)

################################################################################
class StatusAcquireContext(Context):

    __slots__ = (
        "_source",
        "_target",
        "_status",
        "_fail"
    )

################################################################################
    def __init__(self, state: DMGame, source: DMObject, target: DMUnit, status: DMStatus):

        super().__init__(state)

        self._source: DMObject = source
        self._target: DMUnit = target
        self._status: DMStatus = status

        self._fail: bool = False

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
    def status(self) -> DMStatus:

        return self._status

################################################################################
    @property
    def will_fail(self) -> bool:

        return self._status.stacks <= 0 or self._fail

################################################################################
    @will_fail.setter
    def will_fail(self, value: bool) -> None:

        self._fail = value

################################################################################
    def execute(self) -> None:

        # No point adding an empty status.
        if self.will_fail:
            return

        # Use the internal method because we already have an instance of DMStatus
        self.target._add_status(self._status)

################################################################################
