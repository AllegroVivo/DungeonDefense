from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from ...core.objects.monster      import DMMonster
from utilities import UnlockPack, Effect

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
            unlock=UnlockPack.Myth,
            effects=[
                Effect(name="status", base=96, per_lv=72),
                Effect(name="on_damage", base=20, per_lv=1),
            ]
        )
        self.setup_charging(3.3, 3.3)

        # I'm going to assume that ATK stands for the ATK of the monster that
        # is currently defending. (ie. The target)

################################################################################
    def on_charge(self) -> None:

        for monster in self.game.deployed_monsters:
            monster.add_status("Vampire", self.effects["status"], self)
            monster.add_status("Fury", self.effects["status"], self)

################################################################################
    def handle(self, ctx: AttackContext) -> None:

        if ctx.room in self.adjacent_rooms:
            if isinstance(ctx.target, DMMonster):
                ctx.register_after_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        if ctx.target.is_alive:
            if ctx.damage > 0:
                ctx.target.add_status(
                    "Vampire",
                    (self.effects["on_damage"] / 100) * ctx.target.attack,  # convert to percentage
                    self
                )

################################################################################
