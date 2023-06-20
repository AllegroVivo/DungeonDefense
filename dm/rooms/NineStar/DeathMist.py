from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional, Tuple

from ..battleroom   import DMBattleRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.status import DMStatus
################################################################################

__all__ = ("DeathMist",)

################################################################################
class DeathMist(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-224",
            name="Death Mist",
            description=(
                "Once recharged, give 3 (+1 per Lv) Immortality and 1 Immortal "
                "Rage to all monsters in adjacent area. Every time Immortality "
                "is triggered, monsters deployed in adjacent rooms will get Fury "
                "as much as 100 (+5 per Lv) % of ATK."
            ),
            level=level,
            rank=9,
            unlock=UnlockPack.Myth
        )
        self.setup_charging(3.3, 3.3)

################################################################################
    def notify(self, status: DMStatus) -> None:
        """A general event response function."""

        if status.name == "Immortality":
            for monster in self.game.deployed_monsters:
                if monster.room in self.adjacent_rooms:
                    monster.add_status("Fury", self.effect_value()[1] * monster.attack)

################################################################################
    def on_charge(self) -> None:

        monsters = []
        for room in self.adjacent_rooms:
            monsters.extend(room.monsters)

        for monster in monsters:
            monster.add_status("Immortality", self.effect_value()[0])
            monster.add_status("Immortal Rage", 1)

################################################################################
    def effect_value(self) -> Tuple[int, float]:
        """The value(s) of this room's effect(s).

        Breakdown:
        ----------
        **effect = b + (a * LV)**

        In these functions:

        - b is the base effectiveness.
        - a is the additional effectiveness per level.
        - LV is the level of this room.
        """

        status = 3 + (1 * self.level)
        stat = (100 + (5 * self.level)) / 100

        return status, stat

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when this room is added to the map."""

        self.listen("status_execute")

################################################################################
