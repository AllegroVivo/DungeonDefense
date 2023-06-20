from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from ...core.objects.hero import DMHero

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
            rank=4
        )

################################################################################
    def effect_value(self) -> int:
        """The value(s) of this room's effect.

        Breakdown:
        ----------
        **effect = b + (a * LV)**

        In this function:

        - b is the base effectiveness.
        - a is the additional effectiveness per level.
        - LV is the level of this room.
        """

        return 1 + (1 * self.level)

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when this room is added to the map."""

        self.game.subscribe_event("on_death", self.on_death)

################################################################################
    def on_death(self, ctx: AttackContext) -> None:

        if ctx.room == self:
            if isinstance(ctx.defender, DMHero):
                for hero in self.game.all_heroes:
                    hero.add_status("Panic", self.effect_value())

################################################################################
