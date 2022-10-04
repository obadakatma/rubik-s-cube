from enum import Enum


class Color(Enum):
    Indifference = 6
    ORANGE = 0
    RED = 1
    YELLOW = 2
    WHITE = 3
    GREEN = 4
    BLUE = 5

    def __repr__(self):
        return self.name
