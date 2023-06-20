from __future__ import annotations

from typing     import TYPE_CHECKING

from utilities  import ArgumentTypeError

if TYPE_CHECKING:
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("DMChargeable",)

################################################################################
class DMChargeable:

    def __init__(self):

        self._enabled: bool = False

        # Default values. Must be setup to be enabled, and setup requires passing new values.
        self._current_charge: float = 0
        self._manual_charge: float = 0
        self._max_charge: float = 0

################################################################################
    def update(self, dt: float) -> None:

        if self._enabled:
            self._current_charge += dt
            self.check_activation()

################################################################################
    def check_activation(self) -> None:

        if self._current_charge >= self._max_charge:
            self.on_charge()
            self._reduce_charge()

################################################################################
    def on_charge(self) -> None:
        """This is the override method for the specific behavior of the
        chargeable object. Note that charge reduction happens automatically."""

        pass

################################################################################
    def setup_charging(self, charge_time: float, on_enter: float = 0.50) -> None:

        if not isinstance(charge_time, float):
            raise ArgumentTypeError(
                "DMChargeable.set_charge_rate()",
                type(charge_time),
                type(float)
            )
        self._max_charge = charge_time

        if not isinstance(on_enter, float):
            raise ArgumentTypeError(
                "DMChargeable.set_charge_rate()",
                type(on_enter),
                type(float)
            )
        self._manual_charge = on_enter

        # Will always be attached to a DMObject, which has an instance of the game.
        self.game.subscribe_event("room_enter", self._room_enter)  # type: ignore

        # Mark it as good to go.
        self._enabled = True

################################################################################
    def _reduce_charge(self) -> None:

        # Keep this line here so we can separate the logic from the
        # activation logic, which will get overridden in the subclasses.
        self._current_charge -= self._max_charge

################################################################################
    def _room_enter(self, unit: DMUnit) -> None:

        if unit.room == self:
            self._current_charge += self._manual_charge
            self.check_activation()

################################################################################
