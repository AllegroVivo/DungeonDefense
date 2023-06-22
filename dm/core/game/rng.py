from __future__ import annotations

from typing     import TYPE_CHECKING, Any, Dict, List, Optional, Union

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.object import DMObject
    from dm.core.objects.hero import DMHero
    from dm.core.objects.monster import DMMonster
    from dm.core.objects.room import DMRoom
################################################################################

__all__ = ("DMGenerator",)

################################################################################
class DMGenerator:

    __slots__ = (
        "_state",
        "_MT",
        "_seed",
        "_index",
    )

################################################################################
    def __init__(self, state: DMGame, seed: int = None):

        self._state: DMGame = state

        self._MT: List[int] = [0] * 624
        self._seed: int = seed
        self._MT[0] = seed
        self._index: int = 624

        self._generate_initial_array()

################################################################################
    def _generate_initial_array(self) -> None:

        for i in range(1, 624):
            self._MT[i] = (
                (0x6c078965 * (self._MT[i - 1] ^ (self._MT[i - 1] >> 30)) + i) & 0xFFFFFFFF
            )

################################################################################
    def _generate(self):

        for i in range(624):
            y = (self._MT[i] & 0x80000000) + (self._MT[(i+1) % 624] & 0x7fffffff)
            self._MT[i] = self._MT[(i+397) % 624] ^ (y >> 1)
            if y % 2 != 0:
                self._MT[i] ^= 0x9908b0df

################################################################################
    def next(self) -> float:

        if self._index >= 624:
            self._generate()
            self._index = 0

        y = self._MT[self._index]
        y ^= (y >> 11)
        y ^= ((y << 7) & 0x9d2c5680)
        y ^= ((y << 15) & 0xefc60000)
        y ^= (y >> 18)

        self._index += 1
        return y / 0xFFFFFFFF

################################################################################
    def choice(self, seq: List[Any], *, exclude: Optional[Any] = None) -> Optional[Any]:
        """Return a random element from the sequence `seq`. If seq is empty, it
        will return nothing.
         
        You may optionally exclude a specific element from the sequence.
         
        Parameters:
        -----------
        seq : List[Any]
            The sequence to choose from.
        exclude : Optional[Any]
            An element to exclude from the sequence. Defaults to None.
            
        Returns:
        --------
        Optional[Any]
            A random element from the sequence, or None if the sequence was empty.
         """

        if exclude is not None:
            seq = [item for item in seq if item != exclude]

        try:
            return seq[int(self.next() * len(seq))]
        except IndexError:
            return None

################################################################################
    def choices(self, seq: List[Any], k: int = 1, *, exclude: Optional[Any] = None) -> List[Any]:
        """Return a list of k elements from the sequence `seq`. If seq is empty,
        it will return an empty list.
        
        You may optionally exclude a specific element from the sequence.
        
        Parameters:
        -----------
        seq : List[Any]
            The sequence to choose from.
        k : :class:`int`
            The number of elements to choose. Defaults to 1.
        exclude : Optional[Any]
            An element to exclude from the sequence. Defaults to None.
            
        Returns:
        --------
        List[Any]
            A list of k elements from the sequence, or an empty list if the
            sequence was empty.
        """

        if exclude is not None:
            seq = [item for item in seq if item != exclude]

        return [self.choice(seq, exclude=exclude) for _ in range(k)]

################################################################################
    def weighted_choice(self, seq: List[Any], _weights: Dict[int, float], k: int) -> List[Any]:

        weights = [_weights.get(item.rank, 0) for item in seq]

        assert len(seq) == len(weights), "Array and weights must have the same length"
        assert all(weight >= 0 for weight in weights), "Weights must be non-negative"
        assert any(weight > 0 for weight in weights), "At least one weight must be positive"

        total_weight = sum(weights)
        scaled_weights = [weight / total_weight for weight in weights]

        choices = []
        for _ in range(k):
            r = self.next()
            for i, weight in enumerate(scaled_weights):
                if r < weight:
                    choices.append(seq[i])
                    break
                r -= weight

        return choices

################################################################################
    def calculate_damage(self, _obj: DMObject) -> int:
        """Intended to calculate the damage to objects that deal a random amount
        per level."""

        return 0

################################################################################
    def from_range(self, start: int, stop: int) -> int:

        return self.choice([i for i in range(start, stop + 1)])

################################################################################
    def hero(self, room: Optional[DMRoom] = None, *, exclude: Optional[DMHero] = None) -> Optional[DMHero]:
        """Return a random hero from the provided room, or from the dungeon if
        no room is provided.
        
        Parameters:
        -----------
        room : Optional[:class:`DMRoom`]
            The room to choose a hero from. Defaults to None.
        exclude : Optional[:class:`DMHero`]
            A hero to exclude from the selection. Defaults to None.
            
        Returns:
        --------
        Optional[:class:`DMHero`]
            A random hero from the room, or from the dungeon if no room is
            provided.
        """

        # If we've provided a room, we'll choose a hero from that room.
        if room is not None:
            return self.choice(room.heroes, exclude=exclude)

        # Otherwise, we'll choose a hero from the dungeon overall.
        return self.choice(self._state.dungeon.heroes, exclude=exclude)

################################################################################
    def monster(
        self,
        room: Optional[DMRoom] = None,
        *,
        exclude: Optional[DMMonster] = None,
        inventory: bool = False
    ) -> Optional[DMHero]:
        """Return a random monster from the provided room, or from the dungeon if
        no room is provided. Alternatively, if `inventory` is True, this will
        override any other behavior and return a random monster from the player's
        inventory.
        
        Parameters:
        -----------
        room : Optional[:class:`DMRoom`]
            The room to choose a monster from. Defaults to None.
        exclude : Optional[:class:`DMMonster`]
            A monster to exclude from the selection. Defaults to None.
        inventory : :class:`bool`
            Whether to choose a monster from the inventory. Defaults to False.
            Silently overrides all other behavior if True.
            
        Returns:
        --------
        Optional[:class:`DMMonster`]
            A random monster from the room, dungeon, or player's inventory,
            depending on the parameters.
        """

        # If we're choosing from the player's inventory, we'll do that.
        if inventory:
            return self.choice(self._state.inventory.monsters, exclude=exclude)

        # If we've provided a room, we'll choose a monster from that room.
        if room is not None:
            return self.choice(room.monsters)

        # Otherwise, we'll choose a monster from the dungeon overall.
        return self.choice(self._state.dungeon.deployed_monsters)

################################################################################
    def chance(self, n: Union[int, float]) -> bool:
        """Return True with a probability of n/100. If n is greater than 1, it
        will be divided by 100.

        Parameters:
        -----------
        n : Union[:class:`int`, :class:`float`]
            The probability of returning True. For readability, it can be an
            integer (will be divided by 100) or a float (used as is).
        """

        if n > 1:
            n /= 100

        return self.next() <= n

################################################################################
