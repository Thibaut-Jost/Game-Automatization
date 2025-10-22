from __future__ import annotations

from abc import ABC, abstractmethod


class Strategy(ABC):
    """
    Strategy interface common to all algorithm variants.
    """

    @abstractmethod
    def do_algorithm(self) -> None:
        raise NotImplementedError
