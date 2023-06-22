from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.contexts.context import Context

if TYPE_CHECKING:
    from dm.core.game.game    import DMGame
    from dm.core.objects.status       import DMStatus
    from dm.core.objects.room   import DMRoom
################################################################################

__all__ = ("StatusExecutionContext",)

################################################################################
class StatusExecutionContext(Context):

    __slots__ = (
        "_status",
        "_fail"
    )

################################################################################
    def __init__(self, state: DMGame, status: DMStatus):

        super().__init__(state)

        self._status: DMStatus = status

        self._fail: bool = False

################################################################################
    @property
    def room(self) -> DMRoom:

        return self.status.room

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
