from abc import ABC, abstractmethod
from typing import Optional


class IIDGenerator(ABC):
    """ID generator interface

    Business Rules (enforced by implementation):
    - BR-004: IDs are never reused (monotonic increment)
    - SC-006: Deterministic behavior (no randomness)
    """

    @abstractmethod
    def next_id(self) -> str:
        """Generate next unique ID

        Returns:
            str: Next ID (never reused)
        """
        pass


class InMemoryIDGenerator(IIDGenerator):
    """In-memory ID generator with monotonic increment

    Implementation enforces:
    - BR-004: IDs are never reused
    - SC-006: Deterministic behavior (no randomness)
    """

    def __init__(self):
        self._next_id = 1

    def next_id(self) -> str:
        """Generate next unique ID

        Returns:
            str: Next ID (never reused, monotonic increment)

        Business Rules:
            - BR-004: IDs are never reused (enforced by monotonic increment)
        """
        current_id = self._next_id
        self._next_id += 1
        return str(current_id)
