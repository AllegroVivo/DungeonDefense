from __future__ import annotations

from pygame     import Surface
from typing     import TYPE_CHECKING, List
from uuid       import UUID, uuid4

from ..contexts import AttackContext
from utilities  import DMFateType

if TYPE_CHECKING:
    from dm.core    import DMFighter, DMGame, DMHero
################################################################################

__all__ = ("DMEncounter",)

################################################################################
class DMEncounter:

    __slots__ = (
        "_id",
        "_state",
        "_attacker",
        "_defender",
        "_attacks",
        "_actions_elapsed",
    )

################################################################################
    def __init__(self, state: DMGame, attacker: DMFighter, defender: DMFighter):

        self._id: UUID = uuid4()
        self._state: DMGame = state

        self._attacker: DMFighter = attacker
        self._defender: DMFighter = defender

        self._attacks: List[AttackContext]
        self._actions_elapsed: int = 0

        self._attacker.engage()
        self._defender.engage()

################################################################################
    def __eq__(self, other: DMEncounter) -> bool:

        return self._id == other._id

################################################################################
    @property
    def game(self) -> DMGame:

        return self._state

################################################################################
    @property
    def in_progress(self) -> bool:

        return self._defender.life > 0 and self._actions_elapsed < 12.0

################################################################################
    @property
    def attacker(self) -> DMFighter:

        return self._attacker

################################################################################
    @property
    def defender(self) -> DMFighter:

        return self._defender

################################################################################
    def run_turn(self) -> None:

        # Monster attack
        if self.attacker.action_timer <= 0:
            # Create and log the CTX
            ctx = AttackContext(self.game, self.attacker, self.defender)
            self._attacks.append(ctx)

            # Probably need to notify some events before execution.
            ctx.execute()

            # Reset action_timer after attack
            self.attacker.reset_action_timer()

        # Check battle over?

        # Hero attack
        if self.defender.action_timer <= 0:
            ctx = AttackContext(self.game, self.defender, self.attacker)
            self._attacks.append(ctx)

            # Probably need to notify some events before execution.
            ctx.execute()

            # Reset action_timer after attack
            self.defender.reset_action_timer()

        # Check battle over?

################################################################################
################################################################################
