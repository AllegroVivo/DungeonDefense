from __future__ import annotations

from typing     import TYPE_CHECKING

from .adjustable  import AdjustableContext

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.levelable import DMLevelable
    from dm.core.objects.room import DMRoom
################################################################################

__all__ = ("ExperienceContext",)

################################################################################
class ExperienceContext(AdjustableContext):

    def __init__(self, state: DMGame, obj: DMLevelable):

        super().__init__(state, _obj=obj)

################################################################################
    @property
    def room(self) -> DMRoom:

        return self.object.room

################################################################################
    def execute(self) -> None:

        if self._scalar < 0:
            self._scalar = 0

        self._obj.grant_exp(self.calculate())  # type: ignore

################################################################################
    def calculate_exp(self) -> int:

        obj = self.object

        # Initialize variables
        exp_normal = 5
        exp_elite = 10
        exp_required_start = 100
        exp_required_end = 20000

        # Calculate number of heroes invading
        hero_increase_start = 5
        hero_increase_end = 20
        hero_increase_rate = hero_increase_start + (hero_increase_end - hero_increase_start) * (day / 2000)
        heroes = 8 + int(day / hero_increase_rate)

        # Calculate experience gained
        if battle_type == 'normal':
            exp_gained_day = heroes * exp_normal
        else:  # battle_type == 'elite'
            exp_gained_day = heroes * exp_elite

        # Calculate experience required to level up
        exp_required_day = exp_required_start + (exp_required_end - exp_required_start) * (day / 2000)

        return heroes, exp_gained_day, exp_required_day

################################################################################
