from __future__ import annotations

from typing     import (
    TYPE_CHECKING,
    Callable,
    Optional,
    TypeVar,
    Union
)

from .context  import Context
from utilities  import *

if TYPE_CHECKING:
    from ...core.game.game  import DMGame
    from ...core.objects.unit import DMUnit
    from ...core.objects.room import DMRoom
    from ...rooms.traproom import DMTrapRoom
################################################################################

__all__ = ("AttackContext", )

CTX = TypeVar("CTX", bound="AttackContext")

################################################################################
class DamageComponent:

    __slots__ = (
        "_base",
        "_scalar",
        "_flat_reduction",
        "_damage_override",
        "_final"
    )

################################################################################
    def __init__(self, damage: int):

        self._base: int = damage
        self._scalar: float = 0.0
        self._flat_reduction: int = 0

        self._damage_override: Optional[int] = None

        self._final: int = 0

################################################################################
    @property
    def final(self) -> int:

        return self._final

################################################################################
    def mitigate_flat(self, value: int) -> None:
        """Applies a flat damage reduction to this attack's damage
        calculation.

        Arguments should be of class :class:`int` and any floating point numbers
        will be converted to an integer and included in the calculations as such.

        Note:
        -----
            Positive values will **reduce** the damage value and negative values will
            **increase** it.

        Parameters:
        -----------
        value: :class:`int`
            The amount to add or remove from this attack's damage.

        """

        if not isinstance(value, int):
            raise ArgumentTypeError("DamageComponent.mitigate_flat()", type(value), type(int))

        # Can't go below 0 or that would heal the unit.
        self._flat_reduction = min(self._flat_reduction + int(value), self.calculate())

################################################################################
    def mitigate_pct(self, value: float) -> None:
        """Applies a percentage-based damage reduction to this attack's damage
        calculation.

        Arguments should be of class :class:`float` and any integer values will
        be divided by 100 to convert to a percentage, then included in the
        calculations as such.

        Note:
        -----
            Positive values will **reduce** the damage value and negative values will
            **increase** it.

        Parameters:
        -----------
        value: :class:`float`
            The amount to add or remove from this attack's damage.

        """

        if not isinstance(value, float):
            raise ArgumentTypeError("DamageComponent.mitigate_pct()", type(value), type(float))

        self._scalar += value

################################################################################
    def override(self, amount: Union[int, float]) -> None:

        if not isinstance(amount, (int, float)):
            raise ArgumentTypeError(
                "AttackContext.override_damage()",
                type(amount),
                type(int)
            )

        self._damage_override = int(amount)

################################################################################
    def calculate(self) -> int:

        if self._damage_override is not None:
            self._final = self._damage_override
        else:
            self._final = (self._base * (1 - self._scalar)) - self._flat_reduction

        return max(int(self._final), 0)

################################################################################
class AttackContext(Context):

    __slots__ = (
        "_type",
        "_attacker",
        "_defender",
        "_damage",
        "_hit_chance",
        "_fail",
        "_skill",
        "_running",
    )

################################################################################
    def __init__(
        self,
        state: DMGame,
        attacker: Union[DMUnit],  # DMTrapRoom],
        defender: DMUnit,
        attack_type: AttackType = AttackType.Attack,
        # skill: Optional[DMSkill] = None
    ):

        super().__init__(state)

        if attacker is None or defender is None:
            atk_name = attacker.name if attacker is not None else None
            def_name = defender.name if defender is not None else None

            raise ArgumentMissingError(
                "AttackContext.__init__()",
                "attacker'/'defender",
                type(DMUnit),
                additional_info=(
                    "Must have a valid attacker and defender attached to AttackContext.\n"
                    f"<Attacker: {atk_name} || Defender: {def_name}>"
                )
            )

        self._attacker: Union[DMUnit] = attacker  # , DMTrapRoom] = attacker
        self._defender: DMUnit = defender

        self._damage: DamageComponent = DamageComponent(attacker.attack)
        # self._skill: DMSkill = skill

        self._hit_chance: float = 1.0
        self._fail: bool = False

        self._running = True

        self._type: AttackType = attack_type

################################################################################
    def __repr__(self) -> str:

        return(
            "<AttackContext:\n"
            f"attacker: {self.attacker}, defender: {self.defender}\n"
            f"cur dmg: {self.damage}>"
        )

################################################################################
    def __eq__(self, other: AttackContext) -> bool:

        return self._id == other._id

################################################################################
    @property
    def damage(self) -> int:

        if self._fail or self._hit_chance <= 0:
            return 0

        return self._damage.calculate()

################################################################################
    @property
    def room(self) -> DMRoom:

        return self._state.get_room_at(self._attacker._room)

################################################################################
    @property
    def attacker(self) -> Union[DMUnit, DMTrapRoom]:

        return self._attacker

################################################################################
    @property
    def defender(self) -> DMUnit:

        return self._defender

################################################################################
    @property
    def type(self) -> AttackType:

        return self._type

################################################################################
    def override_damage(self, amount: Union[int, float]) -> None:

        self._damage.override(amount)

################################################################################
    def execute(self) -> None:

        # Publish before attack event
        self._state.dispatch_event("before_attack", ctx=self)
        # Reset stats so statuses can do their newly scaled effects (after stack removal last turn)
        self._attacker.refresh_stats()
        self._defender.refresh_stats()

        # Factor in relic effects
        for relic in self._state.relics:
            relic.handle(self)

        # Handle status conditions
        # Apply defensive buffs and debuffs first to give advantage ♥
        defender_statuses = [s for s in self._defender.statuses if s.type is DMStatusType.Buff]
        defender_statuses.extend([s for s in self._defender.statuses if s.type is DMStatusType.Debuff])

        # `status.handle()` specifically applies any mid-battle effects.
        for status in defender_statuses:
            status.handle(self)
            # As soon as the attack is marked as a fail for whatever reason,
            # we can stop applying statuses.
            if self.will_fail:
                break

        # Avoid status processing if we've already marked the attack as failed.
        if not self.will_fail:
            # Then offensive buffs and debuffs :(
            attacker_statuses = [s for s in self._attacker.statuses if s.type is DMStatusType.Buff]
            attacker_statuses.extend([s for s in self._attacker.statuses if s.type is DMStatusType.Debuff])

            for status in attacker_statuses:
                status.handle(self)
                # Might as well break here too if a status nullifies the attack.
                if self.will_fail:
                    break

        # Finalize the damage.
        self.defender.damage(self.damage)

        # Run any post-execution callbacks:
        for callback in self._post_execution_callbacks:
            callback(self)

        # Publish after attack event
        self._state.dispatch_event("after_attack", ctx=self)

        # End this attack
        self._running = False

################################################################################
    def mitigate_flat(self, value: int) -> None:
        """Applies reduction to this attack's damage calculation.

        Arguments of class :class:`float` will **NOT** be interpreted as a
        percentage and will be converted to a flat amount of reduction.

        Example:
        --------
        `ctx.mitigate_flat(25000)` == -25,000 removed from damage total

        Note:
        -----
            Just for clarification, positive values will **reduce** damage and
            negative values will **increase** damage.

        Parameters:
        -----------
        value: :class:`int`
            The amount to remove from this attack's damage.
        """

        self._damage.mitigate_flat(value)

################################################################################
    def mitigate_pct(self, value: float) -> None:
        """Applies reduction to this attack's damage calculation.

        Arguments of class :class:`int` will **NOT** be interpreted as flat
        damage reduction and will be converted to a float and calculated as such.
        Values should be how much additional you want the damage reduced.

        Example:
        --------
        `ctx.mitigate_pct(0.25)` == -25% less damage overall

        Note:
        -----
            Just for clarification, positive values will **reduce** damage and
            negative values will **increase** damage.

        Parameters:
        -----------
        value: :class:`float`
            The percent to remove from this attack's damage.
        """

        self._damage.mitigate_pct(value)

################################################################################
    def amplify_flat(self, value: int) -> None:
        """Applies an increase to this attack's damage calculation.

        Arguments of class :class:`float` will **NOT** be interpreted as a
        percentage and will be converted to a flat amount of bonus damage.

        Example:
        --------
        `ctx.amplify_flat(25000)` == +25,000 additional damage added to total

        Note:
        -----
            Just for clarification, positive values will **increase** damage and
            negative values will **reduce** damage.

        Parameters:
        -----------
        value: :class:`int`
            The amount to add to this attack's damage.
        """

        self._damage.mitigate_flat(-value)

################################################################################
    def amplify_pct(self, value: float) -> None:
        """Applies an increase to this attack's damage calculation.

        Arguments of class :class:`int` will **NOT** be interpreted as flat
        damage bonus and will be converted to a float and calculated as such.
        Values should be how much additional you want the damage increased.

        Example:
        --------
        `ctx.amplify_pct(0.25)` == +25% additional damage overall

        Note:
        -----
            Just for clarification, positive values will **increase** damage and
            negative values will **reduce** damage.

        Parameters:
        -----------
        value: :class:`float`
            The percent to remove from this attack's damage.
        """

        self._damage.mitigate_pct(-value)

################################################################################
    @property
    def will_fail(self) -> bool:

        return self.damage == 0

################################################################################
    @will_fail.setter
    def will_fail(self, value: bool) -> None:

        if not isinstance(value, bool):
            raise ArgumentTypeError(
                "AttackContext.will_fail",
                type(value),
                type(bool),
                additional_info="This is the setter for a property."
            )

        self._fail = value

################################################################################
    def would_kill(self, unit: Optional[DMUnit] = None) -> bool:

        if not isinstance(unit, DMUnit):
            raise ArgumentTypeError("AttackContext.would_kill()", type(unit), type(DMUnit))

        # If the attack is already marked to fail, we can just return.
        if self.will_fail:
            return False

        # Select the ctx's defender as the default check.
        if unit is None:
            unit = self.defender

        return unit.life + unit.defense - self.damage <= 0

################################################################################
    def register_after_execute(self, callback: Callable[[AttackContext], None]) -> None:

        self._post_execution_callbacks.append(callback)

################################################################################
