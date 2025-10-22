try:
    from .Logic.AntiAFK import ClickAndMove
except ImportError:
    from Logic.AntiAFK import ClickAndMove

class BeeSwarm():
    def do_algorithm(self) -> None:
        ClickAndMove()
