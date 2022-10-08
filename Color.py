from enum import Enum


class Color(Enum):
    Indifference = 0
    ORANGE = 2
    RED = 4
    YELLOW = 6
    WHITE = 1
    GREEN = 3
    BLUE = 5

    def __repr__(self):
        return self.name
