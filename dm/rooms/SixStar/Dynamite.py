from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Dynamite",)

################################################################################
class Dynamite(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-193",
            name="Dynamite",
            description=(
                "When a hero in this room dies, inflict {value} % of the dead "
                "hero's Burn stat to all heroes in adjacent rooms."
            ),
            level=level,
            rank=6,
            unlock=UnlockPack.Awakening,
            effects=[
                Effect(name="Burn", base=300, per_lv=50),
            ]
        )

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if ctx.room == self:
            burn = ctx.target.get_status("Burn")
            if burn is not None:
                for room in self.adjacent_rooms:
                    for hero in room.heroes:
                        hero.damage(burn.stacks * (self.effects["Burn"] / 100))

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_death")

################################################################################
