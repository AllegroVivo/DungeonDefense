from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.contexts import StatusExecutionContext
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
                "Once recharged, give {status} Immortality and 1 Immortal "
                "Rage to all monsters in adjacent area. Every time Immortality "
                "is triggered, monsters deployed in adjacent rooms will get Fury "
                "as much as {buff} % of ATK."
            ),
            level=level,
            rank=9,
            unlock=UnlockPack.Myth,
            effects=[
                Effect(name="Immortality", base=3, per_lv=1),
                Effect(name="buff", base=100, per_lv=5),
            ]
        )
        self.setup_charging(3.3, 3.3)

################################################################################
    def notify(self, ctx: StatusExecutionContext) -> None:

        if ctx.status.name == "Immortality":
            for monster in self.game.deployed_monsters:
                if monster.room in self.adjacent_rooms:
                    monster.add_status(
                        "Fury",
                        (self.effects["buff"] / 100) * monster.attack,  # Convert to %
                        self
                    )

################################################################################
    def on_charge(self) -> None:

        for room in self.adjacent_rooms + [self]:
            for monster in room.monsters:
                monster.add_status("Immortality", self.effects["Immortality"], self)
                monster.add_status("Immortal Rage", 1, self)

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_execute")

################################################################################
