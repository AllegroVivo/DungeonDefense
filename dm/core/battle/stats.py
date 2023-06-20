from __future__ import annotations

from typing import Type, Union

from utilities import *
################################################################################

__all__ = ("StatComponent", "BaseStats")

################################################################################
class StatComponent:

    __slots__ = (
        "_base",
        "_flat_additional",
        "_scalar",
        "type"
    )

################################################################################
    def __init__(self, base: Union[int, float], component_type: StatComponentType):

        self._base: float = float(base)
        self.type: StatComponentType = component_type

        self._flat_additional: int = 0
        self._scalar: float = 1.0

################################################################################
    def __iadd__(self, other: Union[int, float]) -> StatComponent:

        if isinstance(other, float):
            other = int(other)

        self._flat_additional += other

        return self

################################################################################
    def __isub__(self, other: Union[int, float]) -> StatComponent:

        if isinstance(other, float):
            other = int(other)

        self._flat_additional -= other

        return self

################################################################################
    def __imul__(self, other: Union[int, float]) -> StatComponent:

        if isinstance(other, float):
            self._scalar += other
        else:
            self._scalar += other // 100

        return self

################################################################################
    def __idiv__(self, other: Union[int, float]) -> StatComponent:

        if isinstance(other, float):
            self._scalar -= other
        else:
            self._scalar -= other // 100

        return self

################################################################################
    def __eq__(self, other: Type[StatComponent]) -> bool:

        if type(self) == other:
            return True

        return False

################################################################################
    def _copy(self) -> StatComponent:

        if self.type is StatComponentType.Life:
            return LifeComponent(int(self._base))
        else:
            return StatComponent(self._base, self.type)

################################################################################
    def calculate(self) -> float:

        if self.type in (StatComponentType.Dex, StatComponentType.CombatAbility):
            return self._base * self._scalar
        elif self.type is StatComponentType.NumAttacks:
            return self._base + self._flat_additional

        return (self._base * self._scalar) + self._flat_additional

################################################################################
    def mutate(self, amount: Union[int, float]) -> None:

        if isinstance(amount, int):
            self._flat_additional += amount
        elif isinstance(amount, float):
            if amount > 4.0:
                raise ValueError(f"Amount exceeding 400% -{amount}- was passed to StatComponent.mutate().")
            self._scalar += amount
        else:
            raise ValueError("Invalid type was passed to StatComponent.mutate().")

################################################################################
    def reset(self) -> None:

        self._scalar = 1.0
        self._flat_additional = 0

################################################################################
class LifeComponent(StatComponent):

    __slots__ = (
        "current",
    )

################################################################################
    def __init__(self, base: int):
        super().__init__(base, StatComponentType.Life)

        self.current: int = int(self.calculate())

################################################################################
    def __iadd__(self, other: int) -> LifeComponent:
        super().__iadd__(other)
        self.current += other

        return self

################################################################################
    def __isub__(self, other: int) -> LifeComponent:
        super().__isub__(other)
        self.current -= other

        return self

################################################################################
    def __imul__(self, other: float) -> LifeComponent:
        super().__imul__(other)
        self.current *= other

        return self

################################################################################
    def __idiv__(self, other: float) -> LifeComponent:
        super().__idiv__(other)
        self.current /= other

        return self

################################################################################
    def mutate(self, amount: Union[int, float]) -> None:
        # Get a reference to the current value
        previous = self.calculate()
        # Then make the change
        super().mutate(amount)
        # And get the new max life.
        current = self.calculate()

        # Restore however much LIFE was increased by.
        self.current += current - previous

################################################################################
class BaseStats:

    __slots__ = (
        "_life",
        "_attack",
        "_defense",
        "_dex",
        "_combat",
        "_num_attacks",
        "_speed"
    )

################################################################################
    def __init__(self, life: int, attack: int, defense: float, dex: float):

        self._life: LifeComponent = LifeComponent(life)
        self._attack: StatComponent = StatComponent(attack, StatComponentType.Attack)
        self._defense: StatComponent = StatComponent(defense, StatComponentType.Defense)
        self._dex: StatComponent = StatComponent(dex, StatComponentType.Dex)
        self._combat: StatComponent = StatComponent(1.0, StatComponentType.CombatAbility)
        self._num_attacks: StatComponent = StatComponent(1, StatComponentType.NumAttacks)
        self._speed: StatComponent = StatComponent(1.0, StatComponentType.Speed)

################################################################################
    @property
    def life(self) -> int:

        return self._life.current

################################################################################
    def damage(self, amount: int) -> None:

        self._life.current = max(self._life.current - amount, 0)

################################################################################
    def heal(self, amount: int) -> None:

        self._life.current = min(self._life.current + amount, int(self._life.calculate()))

################################################################################
    @property
    def attack(self) -> int:

        return int(self._attack.calculate())

################################################################################
    @property
    def defense(self) -> float:

        return self._defense.calculate()

################################################################################
    @property
    def dex(self) -> float:

        return self._dex.calculate()

################################################################################
    @property
    def combat_ability(self) -> float:

        return self._combat.calculate()

################################################################################
    @property
    def num_attacks(self) -> int:

        return int(self._num_attacks.calculate())

################################################################################
    @property
    def speed(self) -> float:

        return self._speed.calculate()

###############################################################################
    def mutate_stat(self, stat: str, amount: Union[int, float]) -> None:

        if not isinstance(stat, str):
            raise ValueError("Invalid stat type passed to StatComponent.mutate_stat().")

        stat = stat.lower()
        if stat not in (
            "life", "attack", "atk", "defense", "def", "dex", "num_attacks",
            "combat", "combat_ability", "speed"
        ):
            raise ValueError("Invalid stat mention passed to StatComponent.mutate_stat().")

        if stat == "life":
            self._life.mutate(amount)
        elif stat in ("attack", "atk"):
            self._attack.mutate(amount)
        elif stat in ("defense", "def"):
            self._defense.mutate(amount)
        elif stat == "dex":
            self._dex.mutate(amount)
        elif stat == "num_attacks":
            self._num_attacks.mutate(amount)
        elif stat in ("combat", "combat_ability"):
            self._combat.mutate(amount)
        elif stat == "speed":
            self._speed.mutate(amount)

################################################################################
    def _copy(self) -> BaseStats:

        copy = type(self).__new__(type(self))

        copy._life = self._life._copy()
        copy._attack = self._attack._copy()
        copy._defense = self._defense._copy()
        copy._dex = self._dex._copy()
        copy._combat = self._combat._copy()
        copy._num_attacks = self._num_attacks._copy()

        return copy

################################################################################
    def reset(self) -> None:

        self._life.reset()
        self._attack.reset()
        self._defense.reset()
        self._dex.reset()
        self._combat.reset()
        self._num_attacks.reset()

################################################################################
