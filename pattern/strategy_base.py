from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


class Strategy(ABC):
    """
    Strategy interface common to all algorithm variants.
    """

    @abstractmethod
    def do_algorithm(self, data: List):
        raise NotImplementedError
