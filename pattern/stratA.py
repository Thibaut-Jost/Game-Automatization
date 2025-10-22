from typing import List

from .strategy_base import Strategy

class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        print("ConcreteStrategyA: Sorting data using normal sort.")
        return sorted(data)