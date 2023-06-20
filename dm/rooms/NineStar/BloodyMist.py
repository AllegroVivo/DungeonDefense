from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional, Tuple

from ..battleroom   import DMBattleRoom
from ...core.objects.monster      import DMMonster
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("BloodyMist",)

################################################################################
class BloodyMist(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-223",
            name="Bloody Mist",
            description=(
                "Once recharged, give {status} Vampire and {status} Fury to "
                "all monsters in the dungeon. When monsters in adjacent rooms "
                "receive damage, get Vampire as much as {value} % of ATK."
            ),
            level=level,
            rank=9,
            unlock=UnlockPack.Myth
        )
        self.setup_charging(3.3, 3.3)

        # I'm going to assume that ATK stands for the ATK of the monster that
        # is currently defending. (ie. The target)

################################################################################
    def on_charge(self) -> None:

        for monster in self.game.deployed_monsters:
            monster.add_status("Vampire", self.effect_value()[0])
            monster.add_status("Fury", self.effect_value()[0])

################################################################################
    def effect_value(self) -> Tuple[int, float]:
        """The value(s) of this room's effect(s).

        Breakdown:
        ----------
        **effect = b + (a * LV)**

        In this function:

        - b is the base effectiveness.
        - a is the additional effectiveness per level.
        - LV is the level of this room.
        """

        status = 96 + (72 * self.level)
        stat = (20 + (1 * self.level)) / 100  # Convert to percentage

        return status, stat

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        if isinstance(ctx.defender, DMMonster):
            if ctx.room in self.adjacent_rooms:
                ctx.register_after_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        if ctx.defender.is_alive:
            if ctx.damage > 0:
                ctx.defender.add_status("Vampire", self.effect_value()[1] * ctx.defender.attack)

################################################################################
