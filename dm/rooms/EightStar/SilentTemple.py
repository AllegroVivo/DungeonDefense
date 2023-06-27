from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ...core.objects.monster import DMMonster
from ..facilityroom import DMFacilityRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("SilentTemple",)

################################################################################
class SilentTemple(DMFacilityRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-216",
            name="Silent Temple",
            description=(
                "Once recharged, give {value} Focus to all monsters in the "
                "dungeon. Monsters in adjacent area will inflict 5 % extra "
                "damage per their Focus stack."
            ),
            level=level,
            rank=8,
            unlock=UnlockPack.Myth,
            effects=[
                Effect(name="Focus", base=10, per_lv=2)
            ]
        )
        self.setup_charging(3.3, 3.3)

################################################################################
    def on_charge(self) -> None:

        for monster in self.game.deployed_monsters:
            monster.add_status("Focus", self.effects["Focus"], self)

################################################################################
    def handle(self, ctx: AttackContext) -> None:

        if isinstance(ctx.source, DMMonster):
            if ctx.room in self.adjacent_rooms + [self]:
                focus = ctx.source.get_status("Focus")
                if focus is not None:
                    ctx.amplify_pct(focus.stacks * 0.05)

################################################################################
