from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from ...core.objects.hero import DMHero
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Scream",)

################################################################################
class Scream(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-148",
            name="Scream",
            description=(
                "Gives {value} Panic to all enemies in the dungeon when a hero "
                "dies in this room."
            ),
            level=level,
            rank=4,
            effects=[
                Effect(name="Panic", base=1, per_lv=1),
            ]
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_death")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if ctx.room == self:
            if isinstance(ctx.target, DMHero):
                for hero in self.game.all_heroes:
                    hero.add_status("Panic", self.effects["Panic"], self)

################################################################################
