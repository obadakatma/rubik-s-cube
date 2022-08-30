from enum import Enum


class Color(Enum):
    Indifference = 0
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4
    WHITE = 5
    ORANGE = 6
    def __repr__(self):
        return self.name