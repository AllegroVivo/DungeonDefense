from __future__ import annotations

from typing     import (
    TYPE_CHECKING,
    Callable,
    List,
    Optional,
    Type,
    TypeVar,
    Union
)

from .context  import Context
from utilities  import *

if TYPE_CHECKING:
    from dm.core    import DMEncounter, DMFighter, DMGame, DMRoom, DMStatus
################################################################################

__all__ = ("AttackContext", )

CTX = TypeVar("CTX", bound="AttackContext")

################################################################################
class DamageComponent:

    __slots__ = (
        "_base",
        "_mitigation",
        "_flat_reduction",
        "final"
    )

################################################################################
    def __init__(self, damage: int):

        self._base: int = damage
        self._mitigation: float = 1.0
        self._flat_reduction: int = 0

        self.final: int = 0

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
        self._flat_reduction = max(self._flat_reduction - int(value), 0)

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

        self._mitigation -= value

################################################################################
    def calculate(self) -> int:

        self.final = int(self._base * self._mitigation + self._flat_reduction)
        return self.final

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
        attacker: Union[DMFighter],  # DMTrapRoom],
        defender: DMFighter,
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
                type(DMFighter),
                additional_info=(
                    "Must have a valid attacker and defender attached to AttackContext.\n"
                    f"<Attacker: {atk_name} || Defender: {def_name}>"
                )
            )

        self._attacker: Union[DMFighter] = attacker  # , DMTrapRoom] = attacker
        self._defender: DMFighter = defender

        self._damage: DamageComponent = DamageComponent(attacker.attack)
        # self._skill: DMSkill = skill

        self._hit_chance: float = 1.0
        self._fail: bool = False

        self._running = True

        self._type: AttackType = attack_type

################################################################################
    def __eq__(self, other: AttackContext) -> bool:

        return self._id == other._id

################################################################################
    @classmethod
    def new(cls: Type[CTX], encounter: DMEncounter) -> CTX:

        return cls(
            encounter.game,
            encounter.room,
            encounter.attacker,
            encounter.defender
        )

################################################################################
    @property
    def damage(self) -> int:

        return self._damage.calculate()

################################################################################
    @property
    def room(self) -> DMRoom:

        return self._state.get_room_at(self._attacker._room)

################################################################################
    @property
    def attacker(self) -> DMFighter:

        return self._attacker

################################################################################
    @property
    def defender(self) -> DMFighter:

        return self._defender

################################################################################
    def execute(self) -> None:

        # Publish before attack event
        self._state.dispatch_event("before_attack", ctx=self)

        # Handle status conditions
        # # Apply defensive buffs and debuffs first to give advantage ♥
        # defender_statuses = [s for s in self._defender.statuses if s.type is DMStatusType.Buff]
        # defender_statuses.extend([s for s in self._defender.statuses if s.type is DMStatusType.Debuff])
        #
        # for status in defender_statuses:
        #     status.activate(self)
        #
        # # Then offensive buffs and debuffs :(
        # attacker_statuses = [s for s in self._attacker.statuses if s.type is DMStatusType.Buff]
        # attacker_statuses.extend([s for s in self._attacker.statuses if s.type is DMStatusType.Debuff])
        #
        # for status in attacker_statuses:
        #     status.activate(self)

        # Relics here?

        # Finalize the damage.
        self.defender.damage(self._damage.calculate())

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

        return not self._fail and self.hit_chance != 0 and self.damage != 0

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
    def would_kill(self, unit: Optional[DMFighter] = None) -> bool:

        if not isinstance(unit, DMFighter):
            raise ArgumentTypeError("AttackContext.would_kill()", type(unit), type(DMFighter))

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
