from copy import deepcopy

from Color import Color

goal = [
    [[Color.RED, Color.RED, Color.RED],
     [Color.RED, Color.RED, Color.RED],
     [Color.RED, Color.RED, Color.RED]],
    [[Color.GREEN, Color.GREEN, Color.GREEN],
     [Color.GREEN, Color.GREEN, Color.GREEN],
     [Color.GREEN, Color.GREEN, Color.GREEN]],
    [[Color.YELLOW, Color.YELLOW, Color.YELLOW],
     [Color.YELLOW, Color.YELLOW, Color.YELLOW],
     [Color.YELLOW, Color.YELLOW, Color.YELLOW]],
    [[Color.BLUE, Color.BLUE, Color.BLUE],
     [Color.BLUE, Color.BLUE, Color.BLUE],
     [Color.BLUE, Color.BLUE, Color.BLUE]],
    [[Color.WHITE, Color.WHITE, Color.WHITE],
     [Color.WHITE, Color.WHITE, Color.WHITE],
     [Color.WHITE, Color.WHITE, Color.WHITE]],
    [[Color.ORANGE, Color.ORANGE, Color.ORANGE],
     [Color.ORANGE, Color.ORANGE, Color.ORANGE],
     [Color.ORANGE, Color.ORANGE, Color.ORANGE]]
]

test = [
    [[Color.RED, Color.RED, Color.RED],
     [Color.YELLOW, Color.YELLOW, Color.YELLOW],
     [Color.ORANGE, Color.ORANGE, Color.ORANGE]],
    [[Color.GREEN, Color.GREEN, Color.GREEN],
     [Color.GREEN, Color.GREEN, Color.GREEN],
     [Color.GREEN, Color.GREEN, Color.GREEN]],
    [[Color.YELLOW, Color.YELLOW, Color.YELLOW],
     [Color.ORANGE, Color.ORANGE, Color.ORANGE],
     [Color.WHITE, Color.WHITE, Color.WHITE]],
    [[Color.BLUE, Color.BLUE, Color.BLUE],
     [Color.BLUE, Color.BLUE, Color.BLUE],
     [Color.BLUE, Color.BLUE, Color.BLUE]],
    [[Color.WHITE, Color.WHITE, Color.WHITE],
     [Color.RED, Color.RED, Color.RED],
     [Color.YELLOW, Color.YELLOW, Color.YELLOW]],
    [[Color.ORANGE, Color.ORANGE, Color.ORANGE],
     [Color.WHITE, Color.WHITE, Color.WHITE],
     [Color.RED, Color.RED, Color.RED]]
]

test2 = [
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]],
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]],
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]],
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]],
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]],
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
]


class State:
    def __init__(self, height, state):
        self.height = height
        self.state = state

    @staticmethod
    def circle4F(w, x, y, z):
        temp = w
        w = x
        x = y
        y = z
        z = temp
        return w, x, y, z

    @staticmethod
    def circle4B(w, x, y, z):
        temp = z
        z = y
        y = x
        x = w
        w = temp
        return w, x, y, z

    def L1R(self):
        newState = deepcopy(self)
        newState.state[0][2][0], \
        newState.state[4][2][0], \
        newState.state[5][2][0], \
        newState.state[2][2][0] = State.circle4B(newState.state[0][2][0],
                                                 newState.state[4][2][0],
                                                 newState.state[5][2][0],
                                                 newState.state[2][2][0])
        newState.state[0][2][1], \
        newState.state[4][2][1], \
        newState.state[5][2][1], \
        newState.state[2][2][1] = State.circle4B(newState.state[0][2][1],
                                                 newState.state[4][2][1],
                                                 newState.state[5][2][1],
                                                 newState.state[2][2][1])
        newState.state[0][2][2], \
        newState.state[4][2][2], \
        newState.state[5][2][2], \
        newState.state[2][2][2] = State.circle4B(newState.state[0][2][2],
                                                 newState.state[4][2][2],
                                                 newState.state[5][2][2],
                                                 newState.state[2][2][2])
        newState.state[3][0][2], \
        newState.state[3][2][2], \
        newState.state[3][2][0], \
        newState.state[3][0][0] = State.circle4B(newState.state[3][0][2],
                                                 newState.state[3][2][2],
                                                 newState.state[3][2][0],
                                                 newState.state[3][0][0])
        newState.state[3][0][1], \
        newState.state[3][1][2], \
        newState.state[3][2][1], \
        newState.state[3][1][0] = State.circle4B(newState.state[3][0][1],
                                                 newState.state[3][1][2],
                                                 newState.state[3][2][1],
                                                 newState.state[3][1][0])
        return newState

    def L1L(self):
        newState = deepcopy(self)
        newState.state[0][2][0], \
        newState.state[4][2][0], \
        newState.state[5][2][0], \
        newState.state[2][2][0] = State.circle4F(newState.state[0][2][0],
                                                 newState.state[4][2][0],
                                                 newState.state[5][2][0],
                                                 newState.state[2][2][0])
        newState.state[0][2][1], \
        newState.state[4][2][1], \
        newState.state[5][2][1], \
        newState.state[2][2][1] = State.circle4F(newState.state[0][2][1],
                                                 newState.state[4][2][1],
                                                 newState.state[5][2][1],
                                                 newState.state[2][2][1])
        newState.state[0][2][2], \
        newState.state[4][2][2], \
        newState.state[5][2][2], \
        newState.state[2][2][2] = State.circle4F(newState.state[0][2][2],
                                                 newState.state[4][2][2],
                                                 newState.state[5][2][2],
                                                 newState.state[2][2][2])
        newState.state[3][0][2], \
        newState.state[3][2][2], \
        newState.state[3][2][0], \
        newState.state[3][0][0] = State.circle4F(newState.state[3][0][2],
                                                 newState.state[3][2][2],
                                                 newState.state[3][2][0],
                                                 newState.state[3][0][0])
        newState.state[3][0][1], \
        newState.state[3][1][2], \
        newState.state[3][2][1], \
        newState.state[3][1][0] = State.circle4F(newState.state[3][0][1],
                                                 newState.state[3][1][2],
                                                 newState.state[3][2][1],
                                                 newState.state[3][1][0])
        return newState

    def L2R(self):
        newState = State.L1R(self)
        newState.state[0][1][0], \
        newState.state[4][1][0], \
        newState.state[5][1][0], \
        newState.state[2][1][0] = State.circle4B(newState.state[0][1][0],
                                                 newState.state[4][1][0],
                                                 newState.state[5][1][0],
                                                 newState.state[2][1][0])
        newState.state[0][1][1], \
        newState.state[4][1][1], \
        newState.state[5][1][1], \
        newState.state[2][1][1] = State.circle4B(newState.state[0][1][1],
                                                 newState.state[4][1][1],
                                                 newState.state[5][1][1],
                                                 newState.state[2][1][1])

        newState.state[0][1][2], \
        newState.state[4][1][2], \
        newState.state[5][1][2], \
        newState.state[2][1][2] = State.circle4B(newState.state[0][1][2],
                                                 newState.state[4][1][2],
                                                 newState.state[5][1][2],
                                                 newState.state[2][1][2])
        return newState

    def L2L(self):
        newState = State.L1L(self)
        newState.state[0][1][0], \
        newState.state[4][1][0], \
        newState.state[5][1][0], \
        newState.state[2][1][0] = State.circle4F(newState.state[0][1][0],
                                                 newState.state[4][1][0],
                                                 newState.state[5][1][0],
                                                 newState.state[2][1][0])
        newState.state[0][1][1], \
        newState.state[4][1][1], \
        newState.state[5][1][1], \
        newState.state[2][1][1] = State.circle4F(newState.state[0][1][1],
                                                 newState.state[4][1][1],
                                                 newState.state[5][1][1],
                                                 newState.state[2][1][1])

        newState.state[0][1][2], \
        newState.state[4][1][2], \
        newState.state[5][1][2], \
        newState.state[2][1][2] = State.circle4F(newState.state[0][1][2],
                                                 newState.state[4][1][2],
                                                 newState.state[5][1][2],
                                                 newState.state[2][1][2])
        return newState

    def RotateR(self):
        newState = State.L2R(self)
        newState.state[0][0][0], \
        newState.state[4][0][0], \
        newState.state[5][0][0], \
        newState.state[2][0][0] = State.circle4B(newState.state[0][0][0],
                                                 newState.state[4][0][0],
                                                 newState.state[5][0][0],
                                                 newState.state[2][0][0])
        newState.state[0][0][1], \
        newState.state[4][0][1], \
        newState.state[5][0][1], \
        newState.state[2][0][1] = State.circle4B(newState.state[0][0][1],
                                                 newState.state[4][0][1],
                                                 newState.state[5][0][1],
                                                 newState.state[2][0][1])
        newState.state[0][0][2], \
        newState.state[4][0][2], \
        newState.state[5][0][2], \
        newState.state[2][0][2] = State.circle4B(newState.state[0][0][2],
                                                 newState.state[4][0][2],
                                                 newState.state[5][0][2],
                                                 newState.state[2][0][2])
        newState.state[1][0][2], \
        newState.state[1][2][2], \
        newState.state[1][2][0], \
        newState.state[1][0][0] = State.circle4F(newState.state[1][0][2],
                                                 newState.state[1][2][2],
                                                 newState.state[1][2][0],
                                                 newState.state[1][0][0])
        newState.state[1][0][1], \
        newState.state[1][1][2], \
        newState.state[1][2][1], \
        newState.state[1][1][0] = State.circle4F(newState.state[1][0][1],
                                                 newState.state[1][1][2],
                                                 newState.state[1][2][1],
                                                 newState.state[1][1][0])
        return newState

    def RotateL(self):
        newState = State.L2L(self)
        newState.state[0][0][0], \
        newState.state[4][0][0], \
        newState.state[5][0][0], \
        newState.state[2][0][0] = State.circle4F(newState.state[0][0][0],
                                                 newState.state[4][0][0],
                                                 newState.state[5][0][0],
                                                 newState.state[2][0][0])
        newState.state[0][0][1], \
        newState.state[4][0][1], \
        newState.state[5][0][1], \
        newState.state[2][0][1] = State.circle4F(newState.state[0][0][1],
                                                 newState.state[4][0][1],
                                                 newState.state[5][0][1],
                                                 newState.state[2][0][1])
        newState.state[0][0][2], \
        newState.state[4][0][2], \
        newState.state[5][0][2], \
        newState.state[2][0][2] = State.circle4F(newState.state[0][0][2],
                                                 newState.state[4][0][2],
                                                 newState.state[5][0][2],
                                                 newState.state[2][0][2])
        newState.state[1][0][2], \
        newState.state[1][2][2], \
        newState.state[1][2][0], \
        newState.state[1][0][0] = State.circle4B(newState.state[1][0][2],
                                                 newState.state[1][2][2],
                                                 newState.state[1][2][0],
                                                 newState.state[1][0][0])
        newState.state[1][0][1], \
        newState.state[1][1][2], \
        newState.state[1][2][1], \
        newState.state[1][1][0] = State.circle4B(newState.state[1][0][1],
                                                 newState.state[1][1][2],
                                                 newState.state[1][2][1],
                                                 newState.state[1][1][0])
        return newState

    def FlipForward(self):
        newState = deepcopy(self)
        newState.state[0][0][0], \
        newState.state[1][0][0], \
        newState.state[5][2][2], \
        newState.state[3][0][0] = State.circle4F(newState.state[0][0][0],
                                                 newState.state[1][0][0],
                                                 newState.state[5][2][2],
                                                 newState.state[3][0][0])
        newState.state[0][0][1], \
        newState.state[1][0][1], \
        newState.state[5][2][1], \
        newState.state[3][0][1] = State.circle4F(newState.state[0][0][1],
                                                 newState.state[1][0][1],
                                                 newState.state[5][2][1],
                                                 newState.state[3][0][1])
        newState.state[0][0][2], \
        newState.state[1][0][2], \
        newState.state[5][2][0], \
        newState.state[3][0][2] = State.circle4F(newState.state[0][0][2],
                                                 newState.state[1][0][2],
                                                 newState.state[5][2][0],
                                                 newState.state[3][0][2])
        newState.state[0][1][0], \
        newState.state[1][1][0], \
        newState.state[5][1][2], \
        newState.state[3][1][0] = State.circle4F(newState.state[0][1][0],
                                                 newState.state[1][1][0],
                                                 newState.state[5][1][2],
                                                 newState.state[3][1][0])
        newState.state[0][1][1], \
        newState.state[1][1][1], \
        newState.state[5][1][1], \
        newState.state[3][1][1] = State.circle4F(newState.state[0][1][1],
                                                 newState.state[1][1][1],
                                                 newState.state[5][1][1],
                                                 newState.state[3][1][1])
        newState.state[0][1][2], \
        newState.state[1][1][2], \
        newState.state[5][1][0], \
        newState.state[3][1][2] = State.circle4F(newState.state[0][1][2],
                                                 newState.state[1][1][2],
                                                 newState.state[5][1][0],
                                                 newState.state[3][1][2])
        newState.state[0][2][0], \
        newState.state[1][2][0], \
        newState.state[5][0][2], \
        newState.state[3][2][0] = State.circle4F(newState.state[0][2][0],
                                                 newState.state[1][2][0],
                                                 newState.state[5][0][2],
                                                 newState.state[3][2][0])
        newState.state[0][2][1], \
        newState.state[1][2][1], \
        newState.state[5][0][1], \
        newState.state[3][2][1] = State.circle4F(newState.state[0][2][1],
                                                 newState.state[1][2][1],
                                                 newState.state[5][0][1],
                                                 newState.state[3][2][1])
        newState.state[0][2][2], \
        newState.state[1][2][2], \
        newState.state[5][0][0], \
        newState.state[3][2][2] = State.circle4F(newState.state[0][2][2],
                                                 newState.state[1][2][2],
                                                 newState.state[5][0][0],
                                                 newState.state[3][2][2])
        newState.state[2][0][0], \
        newState.state[2][0][2], \
        newState.state[2][2][2], \
        newState.state[2][2][0] = State.circle4B(newState.state[2][0][0],
                                                 newState.state[2][0][2],
                                                 newState.state[2][2][2],
                                                 newState.state[2][2][0])
        newState.state[2][0][1], \
        newState.state[2][1][2], \
        newState.state[2][2][1], \
        newState.state[2][1][0] = State.circle4B(newState.state[2][0][1],
                                                 newState.state[2][1][2],
                                                 newState.state[2][2][1],
                                                 newState.state[2][1][0])
        newState.state[4][0][0], \
        newState.state[4][0][2], \
        newState.state[4][2][2], \
        newState.state[4][2][0] = State.circle4F(newState.state[4][0][0],
                                                 newState.state[4][0][2],
                                                 newState.state[4][2][2],
                                                 newState.state[4][2][0])
        newState.state[4][0][1], \
        newState.state[4][1][2], \
        newState.state[4][2][1], \
        newState.state[4][1][0] = State.circle4F(newState.state[4][0][1],
                                                 newState.state[4][1][2],
                                                 newState.state[4][2][1],
                                                 newState.state[4][1][0])
        return newState

    def FlipBackward(self):
        newState = deepcopy(self)
        newState.state[0][0][0], \
        newState.state[1][0][0], \
        newState.state[5][2][2], \
        newState.state[3][0][0] = State.circle4B(newState.state[0][0][0],
                                                 newState.state[1][0][0],
                                                 newState.state[5][2][2],
                                                 newState.state[3][0][0])
        newState.state[0][0][1], \
        newState.state[1][0][1], \
        newState.state[5][2][1], \
        newState.state[3][0][1] = State.circle4B(newState.state[0][0][1],
                                                 newState.state[1][0][1],
                                                 newState.state[5][2][1],
                                                 newState.state[3][0][1])
        newState.state[0][0][2], \
        newState.state[1][0][2], \
        newState.state[5][2][0], \
        newState.state[3][0][2] = State.circle4B(newState.state[0][0][2],
                                                 newState.state[1][0][2],
                                                 newState.state[5][2][0],
                                                 newState.state[3][0][2])
        newState.state[0][1][0], \
        newState.state[1][1][0], \
        newState.state[5][1][2], \
        newState.state[3][1][0] = State.circle4B(newState.state[0][1][0],
                                                 newState.state[1][1][0],
                                                 newState.state[5][1][2],
                                                 newState.state[3][1][0])
        newState.state[0][1][1], \
        newState.state[1][1][1], \
        newState.state[5][1][1], \
        newState.state[3][1][1] = State.circle4B(newState.state[0][1][1],
                                                 newState.state[1][1][1],
                                                 newState.state[5][1][1],
                                                 newState.state[3][1][1])
        newState.state[0][1][2], \
        newState.state[1][1][2], \
        newState.state[5][1][0], \
        newState.state[3][1][2] = State.circle4B(newState.state[0][1][2],
                                                 newState.state[1][1][2],
                                                 newState.state[5][1][0],
                                                 newState.state[3][1][2])
        newState.state[0][2][0], \
        newState.state[1][2][0], \
        newState.state[5][0][2], \
        newState.state[3][2][0] = State.circle4B(newState.state[0][2][0],
                                                 newState.state[1][2][0],
                                                 newState.state[5][0][2],
                                                 newState.state[3][2][0])
        newState.state[0][2][1], \
        newState.state[1][2][1], \
        newState.state[5][0][1], \
        newState.state[3][2][1] = State.circle4B(newState.state[0][2][1],
                                                 newState.state[1][2][1],
                                                 newState.state[5][0][1],
                                                 newState.state[3][2][1])
        newState.state[0][2][2], \
        newState.state[1][2][2], \
        newState.state[5][0][0], \
        newState.state[3][2][2] = State.circle4B(newState.state[0][2][2],
                                                 newState.state[1][2][2],
                                                 newState.state[5][0][0],
                                                 newState.state[3][2][2])
        newState.state[2][0][0], \
        newState.state[2][0][2], \
        newState.state[2][2][2], \
        newState.state[2][2][0] = State.circle4F(newState.state[2][0][0],
                                                 newState.state[2][0][2],
                                                 newState.state[2][2][2],
                                                 newState.state[2][2][0])
        newState.state[2][0][1], \
        newState.state[2][1][2], \
        newState.state[2][2][1], \
        newState.state[2][1][0] = State.circle4F(newState.state[2][0][1],
                                                 newState.state[2][1][2],
                                                 newState.state[2][2][1],
                                                 newState.state[2][1][0])
        newState.state[4][0][0], \
        newState.state[4][0][2], \
        newState.state[4][2][2], \
        newState.state[4][2][0] = State.circle4B(newState.state[4][0][0],
                                                 newState.state[4][0][2],
                                                 newState.state[4][2][2],
                                                 newState.state[4][2][0])
        newState.state[4][0][1], \
        newState.state[4][1][2], \
        newState.state[4][2][1], \
        newState.state[4][1][0] = State.circle4B(newState.state[4][0][1],
                                                 newState.state[4][1][2],
                                                 newState.state[4][2][1],
                                                 newState.state[4][1][0])
        return newState

    def FlipRight(self):
        newState = deepcopy(self)
        newState.state[1][0][0], \
        newState.state[2][2][0], \
        newState.state[3][2][2], \
        newState.state[4][0][2] = State.circle4F(newState.state[1][0][0],
                                                 newState.state[2][2][0],
                                                 newState.state[3][2][2],
                                                 newState.state[4][0][2])
        newState.state[1][0][1], \
        newState.state[2][1][0], \
        newState.state[3][2][1], \
        newState.state[4][1][2] = State.circle4F(newState.state[1][0][1],
                                                 newState.state[2][1][0],
                                                 newState.state[3][2][1],
                                                 newState.state[4][1][2])
        newState.state[1][0][2], \
        newState.state[2][0][0], \
        newState.state[3][2][0], \
        newState.state[4][2][2] = State.circle4F(newState.state[1][0][2],
                                                 newState.state[2][0][0],
                                                 newState.state[3][2][0],
                                                 newState.state[4][2][2])
        newState.state[1][1][0], \
        newState.state[2][2][1], \
        newState.state[3][1][2], \
        newState.state[4][0][1] = State.circle4F(newState.state[1][1][0],
                                                 newState.state[2][2][1],
                                                 newState.state[3][1][2],
                                                 newState.state[4][0][1])
        newState.state[1][1][1], \
        newState.state[2][1][1], \
        newState.state[3][1][1], \
        newState.state[4][1][1] = State.circle4F(newState.state[1][1][1],
                                                 newState.state[2][1][1],
                                                 newState.state[3][1][1],
                                                 newState.state[4][1][1])
        newState.state[1][1][2], \
        newState.state[2][0][1], \
        newState.state[3][1][0], \
        newState.state[4][2][1] = State.circle4F(newState.state[1][1][2],
                                                 newState.state[2][0][1],
                                                 newState.state[3][1][0],
                                                 newState.state[4][2][1])
        newState.state[1][2][0], \
        newState.state[2][2][2], \
        newState.state[3][0][2], \
        newState.state[4][0][0] = State.circle4F(newState.state[1][2][0],
                                                 newState.state[2][2][2],
                                                 newState.state[3][0][2],
                                                 newState.state[4][0][0])
        newState.state[1][2][1], \
        newState.state[2][1][2], \
        newState.state[3][0][1], \
        newState.state[4][1][0] = State.circle4F(newState.state[1][2][1],
                                                 newState.state[2][1][2],
                                                 newState.state[3][0][1],
                                                 newState.state[4][1][0])
        newState.state[1][2][2], \
        newState.state[2][0][2], \
        newState.state[3][0][0], \
        newState.state[4][2][0] = State.circle4F(newState.state[1][2][2],
                                                 newState.state[2][0][2],
                                                 newState.state[3][0][0],
                                                 newState.state[4][2][0])
        newState.state[0][0][0], \
        newState.state[0][0][2], \
        newState.state[0][2][2], \
        newState.state[0][2][0] = State.circle4B(newState.state[0][0][0],
                                                 newState.state[0][0][2],
                                                 newState.state[0][2][2],
                                                 newState.state[0][2][0])
        newState.state[0][0][1], \
        newState.state[0][1][2], \
        newState.state[0][2][1], \
        newState.state[0][1][0] = State.circle4B(newState.state[0][0][1],
                                                 newState.state[0][1][2],
                                                 newState.state[0][2][1],
                                                 newState.state[0][1][0])
        newState.state[5][0][0], \
        newState.state[5][0][2], \
        newState.state[5][2][2], \
        newState.state[5][2][0] = State.circle4F(newState.state[5][0][0],
                                                 newState.state[5][0][2],
                                                 newState.state[5][2][2],
                                                 newState.state[5][2][0])
        newState.state[5][0][1], \
        newState.state[5][1][2], \
        newState.state[5][2][1], \
        newState.state[5][1][0] = State.circle4F(newState.state[5][0][1],
                                                 newState.state[5][1][2],
                                                 newState.state[5][2][1],
                                                 newState.state[5][1][0])
        return newState

    def FlipLeft(self):
        newState = deepcopy(self)
        newState.state[1][0][0], \
        newState.state[2][2][0], \
        newState.state[3][2][2], \
        newState.state[4][0][2] = State.circle4B(newState.state[1][0][0],
                                                 newState.state[2][2][0],
                                                 newState.state[3][2][2],
                                                 newState.state[4][0][2])
        newState.state[1][0][1], \
        newState.state[2][1][0], \
        newState.state[3][2][1], \
        newState.state[4][1][2] = State.circle4B(newState.state[1][0][1],
                                                 newState.state[2][1][0],
                                                 newState.state[3][2][1],
                                                 newState.state[4][1][2])
        newState.state[1][0][2], \
        newState.state[2][0][0], \
        newState.state[3][2][0], \
        newState.state[4][2][2] = State.circle4B(newState.state[1][0][2],
                                                 newState.state[2][0][0],
                                                 newState.state[3][2][0],
                                                 newState.state[4][2][2])
        newState.state[1][1][0], \
        newState.state[2][2][1], \
        newState.state[3][1][2], \
        newState.state[4][0][1] = State.circle4B(newState.state[1][1][0],
                                                 newState.state[2][2][1],
                                                 newState.state[3][1][2],
                                                 newState.state[4][0][1])
        newState.state[1][1][1], \
        newState.state[2][1][1], \
        newState.state[3][1][1], \
        newState.state[4][1][1] = State.circle4B(newState.state[1][1][1],
                                                 newState.state[2][1][1],
                                                 newState.state[3][1][1],
                                                 newState.state[4][1][1])
        newState.state[1][1][2], \
        newState.state[2][0][1], \
        newState.state[3][1][0], \
        newState.state[4][2][1] = State.circle4B(newState.state[1][1][2],
                                                 newState.state[2][0][1],
                                                 newState.state[3][1][0],
                                                 newState.state[4][2][1])
        newState.state[1][2][0], \
        newState.state[2][2][2], \
        newState.state[3][0][2], \
        newState.state[4][0][0] = State.circle4B(newState.state[1][2][0],
                                                 newState.state[2][2][2],
                                                 newState.state[3][0][2],
                                                 newState.state[4][0][0])
        newState.state[1][2][1], \
        newState.state[2][1][2], \
        newState.state[3][0][1], \
        newState.state[4][1][0] = State.circle4B(newState.state[1][2][1],
                                                 newState.state[2][1][2],
                                                 newState.state[3][0][1],
                                                 newState.state[4][1][0])
        newState.state[1][2][2], \
        newState.state[2][0][2], \
        newState.state[3][0][0], \
        newState.state[4][2][0] = State.circle4B(newState.state[1][2][2],
                                                 newState.state[2][0][2],
                                                 newState.state[3][0][0],
                                                 newState.state[4][2][0])
        newState.state[0][0][0], \
        newState.state[0][0][2], \
        newState.state[0][2][2], \
        newState.state[0][2][0] = State.circle4F(newState.state[0][0][0],
                                                 newState.state[0][0][2],
                                                 newState.state[0][2][2],
                                                 newState.state[0][2][0])
        newState.state[0][0][1], \
        newState.state[0][1][2], \
        newState.state[0][2][1], \
        newState.state[0][1][0] = State.circle4F(newState.state[0][0][1],
                                                 newState.state[0][1][2],
                                                 newState.state[0][2][1],
                                                 newState.state[0][1][0])
        newState.state[5][0][0], \
        newState.state[5][0][2], \
        newState.state[5][2][2], \
        newState.state[5][2][0] = State.circle4B(newState.state[5][0][0],
                                                 newState.state[5][0][2],
                                                 newState.state[5][2][2],
                                                 newState.state[5][2][0])
        newState.state[5][0][1], \
        newState.state[5][1][2], \
        newState.state[5][2][1], \
        newState.state[5][1][0] = State.circle4B(newState.state[5][0][1],
                                                 newState.state[5][1][2],
                                                 newState.state[5][2][1],
                                                 newState.state[5][1][0])
        return newState

    def lUp(self):
        height = deepcopy(self)
        height.height += 1
        return height

    def lDown(self):
        height = deepcopy(self)
        height.height -= 1
        return height

    def switchIndexes(self, num_of_rotate):
        newState = deepcopy(self)
        for j in range(6):
            for k in range(num_of_rotate[j]):
                newState.state[j][0][2], \
                newState.state[j][2][2], \
                newState.state[j][2][0], \
                newState.state[j][0][0] = State.circle4F(newState.state[j][0][2],
                                                         newState.state[j][2][2],
                                                         newState.state[j][2][0],
                                                         newState.state[j][0][0])
                newState.state[j][0][1], \
                newState.state[j][1][2], \
                newState.state[j][2][1], \
                newState.state[j][1][0] = State.circle4F(newState.state[j][0][1],
                                                         newState.state[j][1][2],
                                                         newState.state[j][2][1],
                                                         newState.state[j][1][0])
        return newState
