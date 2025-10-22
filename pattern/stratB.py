from typing import List

from .strategy_base import Strategy

class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List) -> List:
        print("ConcreteStrategyB: Sorting data using reverse sort.")
        return reversed(sorted(data))