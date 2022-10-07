from copy import deepcopy

from Color import Color

goal = [
    [[Color.RED, Color.RED, Color.RED, Color.RED, Color.RED],
     [Color.RED, Color.RED, Color.RED, Color.RED, Color.RED],
     [Color.RED, Color.RED, Color.RED, Color.RED, Color.RED],
     [Color.RED, Color.RED, Color.RED, Color.RED, Color.RED],
     [Color.RED, Color.RED, Color.RED, Color.RED, Color.RED]],
    [[Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN],
     [Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN],
     [Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN],
     [Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN],
     [Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN]],
    [[Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW],
     [Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW],
     [Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW],
     [Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW],
     [Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW]],
    [[Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE],
     [Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE],
     [Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE],
     [Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE],
     [Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE]],
    [[Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE],
     [Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE],
     [Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE],
     [Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE],
     [Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE]],
    [[Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE],
     [Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE],
     [Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE],
     [Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE],
     [Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE]]
]

test = [
    [[Color.YELLOW, Color.BLUE, Color.YELLOW, Color.BLUE, Color.RED],
     [Color.RED, Color.RED, Color.WHITE, Color.WHITE, Color.ORANGE],
     [Color.BLUE, Color.BLUE, Color.RED, Color.GREEN, Color.WHITE],
     [Color.BLUE, Color.GREEN, Color.ORANGE, Color.WHITE, Color.GREEN],
     [Color.RED, Color.RED, Color.YELLOW, Color.GREEN, Color.BLUE]],
    [[Color.GREEN, Color.GREEN, Color.RED, Color.GREEN, Color.ORANGE],
     [Color.BLUE, Color.BLUE, Color.RED, Color.YELLOW, Color.RED],
     [Color.YELLOW, Color.RED, Color.GREEN, Color.YELLOW, Color.ORANGE],
     [Color.BLUE, Color.YELLOW, Color.WHITE, Color.WHITE, Color.BLUE],
     [Color.BLUE, Color.ORANGE, Color.BLUE, Color.WHITE, Color.WHITE]],
    [[Color.ORANGE, Color.YELLOW, Color.GREEN, Color.WHITE, Color.RED],
     [Color.GREEN, Color.BLUE, Color.YELLOW, Color.GREEN, Color.GREEN],
     [Color.RED, Color.BLUE, Color.YELLOW, Color.WHITE, Color.ORANGE],
     [Color.ORANGE, Color.ORANGE, Color.GREEN, Color.RED, Color.RED],
     [Color.ORANGE, Color.RED, Color.GREEN, Color.GREEN, Color.WHITE]],
    [[Color.GREEN, Color.YELLOW, Color.ORANGE, Color.WHITE, Color.YELLOW],
     [Color.YELLOW, Color.GREEN, Color.YELLOW, Color.GREEN, Color.YELLOW],
     [Color.ORANGE, Color.ORANGE, Color.BLUE, Color.BLUE, Color.RED],
     [Color.WHITE, Color.BLUE, Color.ORANGE, Color.RED, Color.BLUE],
     [Color.BLUE, Color.YELLOW, Color.GREEN, Color.ORANGE, Color.GREEN]],
    [[Color.BLUE, Color.ORANGE, Color.WHITE, Color.WHITE, Color.YELLOW],
     [Color.YELLOW, Color.ORANGE, Color.ORANGE, Color.YELLOW, Color.BLUE],
     [Color.BLUE, Color.BLUE, Color.WHITE, Color.YELLOW, Color.GREEN],
     [Color.WHITE, Color.WHITE, Color.RED, Color.RED, Color.ORANGE],
     [Color.ORANGE, Color.ORANGE, Color.BLUE, Color.RED, Color.RED]],
    [[Color.GREEN, Color.YELLOW, Color.YELLOW, Color.ORANGE, Color.WHITE],
     [Color.YELLOW, Color.BLUE, Color.GREEN, Color.YELLOW, Color.RED],
     [Color.WHITE, Color.RED, Color.ORANGE, Color.WHITE, Color.WHITE],
     [Color.WHITE, Color.ORANGE, Color.GREEN, Color.ORANGE, Color.GREEN],
     [Color.YELLOW, Color.WHITE, Color.RED, Color.RED, Color.WHITE]]
]

test2 = [
    [[0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0]]
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
        newState.state[0][4][0], \
        newState.state[4][4][0], \
        newState.state[5][4][0], \
        newState.state[2][4][0] = State.circle4B(newState.state[0][4][0],
                                                 newState.state[4][4][0],
                                                 newState.state[5][4][0],
                                                 newState.state[2][4][0])
        newState.state[0][4][1], \
        newState.state[4][4][1], \
        newState.state[5][4][1], \
        newState.state[2][4][1] = State.circle4B(newState.state[0][4][1],
                                                 newState.state[4][4][1],
                                                 newState.state[5][4][1],
                                                 newState.state[2][4][1])
        newState.state[0][4][2], \
        newState.state[4][4][2], \
        newState.state[5][4][2], \
        newState.state[2][4][2] = State.circle4B(newState.state[0][4][2],
                                                 newState.state[4][4][2],
                                                 newState.state[5][4][2],
                                                 newState.state[2][4][2])

        newState.state[0][4][3], \
        newState.state[4][4][3], \
        newState.state[5][4][3], \
        newState.state[2][4][3] = State.circle4B(newState.state[0][4][3],
                                                 newState.state[4][4][3],
                                                 newState.state[5][4][3],
                                                 newState.state[2][4][3])

        newState.state[0][4][4], \
        newState.state[4][4][4], \
        newState.state[5][4][4], \
        newState.state[2][4][4] = State.circle4B(newState.state[0][4][4],
                                                 newState.state[4][4][4],
                                                 newState.state[5][4][4],
                                                 newState.state[2][4][4])

        newState.state[3][0][4], \
        newState.state[3][4][4], \
        newState.state[3][4][0], \
        newState.state[3][0][0] = State.circle4B(newState.state[3][0][4],
                                                 newState.state[3][4][4],
                                                 newState.state[3][4][0],
                                                 newState.state[3][0][0])
        newState.state[3][0][1], \
        newState.state[3][1][4], \
        newState.state[3][4][3], \
        newState.state[3][3][0] = State.circle4B(newState.state[3][0][1],
                                                 newState.state[3][1][4],
                                                 newState.state[3][4][3],
                                                 newState.state[3][3][0])
        newState.state[3][0][2], \
        newState.state[3][2][4], \
        newState.state[3][4][2], \
        newState.state[3][2][0] = State.circle4B(newState.state[3][0][2],
                                                 newState.state[3][2][4],
                                                 newState.state[3][4][2],
                                                 newState.state[3][2][0])

        newState.state[3][0][3], \
        newState.state[3][3][4], \
        newState.state[3][4][1], \
        newState.state[3][1][0] = State.circle4B(newState.state[3][0][3],
                                                 newState.state[3][3][4],
                                                 newState.state[3][4][1],
                                                 newState.state[3][1][0])

        newState.state[3][1][1], \
        newState.state[3][1][3], \
        newState.state[3][3][3], \
        newState.state[3][3][1] = State.circle4B(newState.state[3][1][1],
                                                 newState.state[3][1][3],
                                                 newState.state[3][3][3],
                                                 newState.state[3][3][1])

        newState.state[3][1][2], \
        newState.state[3][2][3], \
        newState.state[3][3][2], \
        newState.state[3][2][1] = State.circle4B(newState.state[3][1][2],
                                                 newState.state[3][2][3],
                                                 newState.state[3][3][2],
                                                 newState.state[3][2][1])

        return newState

    def L1L(self):
        newState = deepcopy(self)
        newState.state[0][4][0], \
        newState.state[4][4][0], \
        newState.state[5][4][0], \
        newState.state[2][4][0] = State.circle4F(newState.state[0][4][0],
                                                 newState.state[4][4][0],
                                                 newState.state[5][4][0],
                                                 newState.state[2][4][0])
        newState.state[0][4][1], \
        newState.state[4][4][1], \
        newState.state[5][4][1], \
        newState.state[2][4][1] = State.circle4F(newState.state[0][4][1],
                                                 newState.state[4][4][1],
                                                 newState.state[5][4][1],
                                                 newState.state[2][4][1])
        newState.state[0][4][2], \
        newState.state[4][4][2], \
        newState.state[5][4][2], \
        newState.state[2][4][2] = State.circle4F(newState.state[0][4][2],
                                                 newState.state[4][4][2],
                                                 newState.state[5][4][2],
                                                 newState.state[2][4][2])

        newState.state[0][4][3], \
        newState.state[4][4][3], \
        newState.state[5][4][3], \
        newState.state[2][4][3] = State.circle4F(newState.state[0][4][3],
                                                 newState.state[4][4][3],
                                                 newState.state[5][4][3],
                                                 newState.state[2][4][3])

        newState.state[0][4][4], \
        newState.state[4][4][4], \
        newState.state[5][4][4], \
        newState.state[2][4][4] = State.circle4F(newState.state[0][4][4],
                                                 newState.state[4][4][4],
                                                 newState.state[5][4][4],
                                                 newState.state[2][4][4])

        newState.state[3][0][4], \
        newState.state[3][4][4], \
        newState.state[3][4][0], \
        newState.state[3][0][0] = State.circle4F(newState.state[3][0][4],
                                                 newState.state[3][4][4],
                                                 newState.state[3][4][0],
                                                 newState.state[3][0][0])
        newState.state[3][0][1], \
        newState.state[3][1][4], \
        newState.state[3][4][3], \
        newState.state[3][3][0] = State.circle4F(newState.state[3][0][1],
                                                 newState.state[3][1][4],
                                                 newState.state[3][4][3],
                                                 newState.state[3][3][0])
        newState.state[3][0][2], \
        newState.state[3][2][4], \
        newState.state[3][4][2], \
        newState.state[3][2][0] = State.circle4F(newState.state[3][0][2],
                                                 newState.state[3][2][4],
                                                 newState.state[3][4][2],
                                                 newState.state[3][2][0])

        newState.state[3][0][3], \
        newState.state[3][3][4], \
        newState.state[3][4][1], \
        newState.state[3][1][0] = State.circle4F(newState.state[3][0][3],
                                                 newState.state[3][3][4],
                                                 newState.state[3][4][1],
                                                 newState.state[3][1][0])

        newState.state[3][1][1], \
        newState.state[3][1][3], \
        newState.state[3][3][3], \
        newState.state[3][3][1] = State.circle4F(newState.state[3][1][1],
                                                 newState.state[3][1][3],
                                                 newState.state[3][3][3],
                                                 newState.state[3][3][1])

        newState.state[3][1][2], \
        newState.state[3][2][3], \
        newState.state[3][3][2], \
        newState.state[3][2][1] = State.circle4F(newState.state[3][1][2],
                                                 newState.state[3][2][3],
                                                 newState.state[3][3][2],
                                                 newState.state[3][2][1])

        return newState

    def L2R(self):
        newState = State.L1R(self)

        newState.state[0][3][0], \
        newState.state[4][3][0], \
        newState.state[5][3][0], \
        newState.state[2][3][0] = State.circle4B(newState.state[0][3][0],
                                                 newState.state[4][3][0],
                                                 newState.state[5][3][0],
                                                 newState.state[2][3][0])
        newState.state[0][3][1], \
        newState.state[4][3][1], \
        newState.state[5][3][1], \
        newState.state[2][3][1] = State.circle4B(newState.state[0][3][1],
                                                 newState.state[4][3][1],
                                                 newState.state[5][3][1],
                                                 newState.state[2][3][1])

        newState.state[0][3][2], \
        newState.state[4][3][2], \
        newState.state[5][3][2], \
        newState.state[2][3][2] = State.circle4B(newState.state[0][3][2],
                                                 newState.state[4][3][2],
                                                 newState.state[5][3][2],
                                                 newState.state[2][3][2])

        newState.state[0][3][3], \
        newState.state[4][3][3], \
        newState.state[5][3][3], \
        newState.state[2][3][3] = State.circle4B(newState.state[0][3][3],
                                                 newState.state[4][3][3],
                                                 newState.state[5][3][3],
                                                 newState.state[2][3][3])

        newState.state[0][3][4], \
        newState.state[4][3][4], \
        newState.state[5][3][4], \
        newState.state[2][3][4] = State.circle4B(newState.state[0][3][4],
                                                 newState.state[4][3][4],
                                                 newState.state[5][3][4],
                                                 newState.state[2][3][4])
        return newState

    def L2L(self):
        newState = State.L1L(self)

        newState.state[0][3][0], \
        newState.state[4][3][0], \
        newState.state[5][3][0], \
        newState.state[2][3][0] = State.circle4F(newState.state[0][3][0],
                                                 newState.state[4][3][0],
                                                 newState.state[5][3][0],
                                                 newState.state[2][3][0])
        newState.state[0][3][1], \
        newState.state[4][3][1], \
        newState.state[5][3][1], \
        newState.state[2][3][1] = State.circle4F(newState.state[0][3][1],
                                                 newState.state[4][3][1],
                                                 newState.state[5][3][1],
                                                 newState.state[2][3][1])

        newState.state[0][3][2], \
        newState.state[4][3][2], \
        newState.state[5][3][2], \
        newState.state[2][3][2] = State.circle4F(newState.state[0][3][2],
                                                 newState.state[4][3][2],
                                                 newState.state[5][3][2],
                                                 newState.state[2][3][2])

        newState.state[0][3][3], \
        newState.state[4][3][3], \
        newState.state[5][3][3], \
        newState.state[2][3][3] = State.circle4F(newState.state[0][3][3],
                                                 newState.state[4][3][3],
                                                 newState.state[5][3][3],
                                                 newState.state[2][3][3])

        newState.state[0][3][4], \
        newState.state[4][3][4], \
        newState.state[5][3][4], \
        newState.state[2][3][4] = State.circle4F(newState.state[0][3][4],
                                                 newState.state[4][3][4],
                                                 newState.state[5][3][4],
                                                 newState.state[2][3][4])
        return newState

    def L3R(self):
        newState = State.L2R(self)

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

        newState.state[0][2][3], \
        newState.state[4][2][3], \
        newState.state[5][2][3], \
        newState.state[2][2][3] = State.circle4B(newState.state[0][2][3],
                                                 newState.state[4][2][3],
                                                 newState.state[5][2][3],
                                                 newState.state[2][2][3])

        newState.state[0][2][4], \
        newState.state[4][2][4], \
        newState.state[5][2][4], \
        newState.state[2][2][4] = State.circle4B(newState.state[0][2][4],
                                                 newState.state[4][2][4],
                                                 newState.state[5][2][4],
                                                 newState.state[2][2][4])
        return newState

    def L3L(self):
        newState = State.L2L(self)

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

        newState.state[0][2][3], \
        newState.state[4][2][3], \
        newState.state[5][2][3], \
        newState.state[2][2][3] = State.circle4F(newState.state[0][2][3],
                                                 newState.state[4][2][3],
                                                 newState.state[5][2][3],
                                                 newState.state[2][2][3])

        newState.state[0][2][4], \
        newState.state[4][2][4], \
        newState.state[5][2][4], \
        newState.state[2][2][4] = State.circle4F(newState.state[0][2][4],
                                                 newState.state[4][2][4],
                                                 newState.state[5][2][4],
                                                 newState.state[2][2][4])
        return newState

    def L4R(self):
        newState = State.L3R(self)

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

        newState.state[0][1][3], \
        newState.state[4][1][3], \
        newState.state[5][1][3], \
        newState.state[2][1][3] = State.circle4B(newState.state[0][1][3],
                                                 newState.state[4][1][3],
                                                 newState.state[5][1][3],
                                                 newState.state[2][1][3])

        newState.state[0][1][4], \
        newState.state[4][1][4], \
        newState.state[5][1][4], \
        newState.state[2][1][4] = State.circle4B(newState.state[0][1][4],
                                                 newState.state[4][1][4],
                                                 newState.state[5][1][4],
                                                 newState.state[2][1][4])
        return newState

    def L4L(self):
        newState = State.L3L(self)

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

        newState.state[0][1][3], \
        newState.state[4][1][3], \
        newState.state[5][1][3], \
        newState.state[2][1][3] = State.circle4F(newState.state[0][1][3],
                                                 newState.state[4][1][3],
                                                 newState.state[5][1][3],
                                                 newState.state[2][1][3])

        newState.state[0][1][4], \
        newState.state[4][1][4], \
        newState.state[5][1][4], \
        newState.state[2][1][4] = State.circle4F(newState.state[0][1][4],
                                                 newState.state[4][1][4],
                                                 newState.state[5][1][4],
                                                 newState.state[2][1][4])
        return newState

    def RotateR(self):
        newState = deepcopy(self)
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

        newState.state[0][0][3], \
        newState.state[4][0][3], \
        newState.state[5][0][3], \
        newState.state[2][0][3] = State.circle4B(newState.state[0][0][3],
                                                 newState.state[4][0][3],
                                                 newState.state[5][0][3],
                                                 newState.state[2][0][3])

        newState.state[0][0][4], \
        newState.state[4][0][4], \
        newState.state[5][0][4], \
        newState.state[2][0][4] = State.circle4B(newState.state[0][0][4],
                                                 newState.state[4][0][4],
                                                 newState.state[5][0][4],
                                                 newState.state[2][0][4])

        newState.state[1][0][4], \
        newState.state[1][4][4], \
        newState.state[1][4][0], \
        newState.state[1][0][0] = State.circle4F(newState.state[1][0][4],
                                                 newState.state[1][4][4],
                                                 newState.state[1][4][0],
                                                 newState.state[1][0][0])
        newState.state[1][0][1], \
        newState.state[1][1][4], \
        newState.state[1][4][3], \
        newState.state[1][3][0] = State.circle4F(newState.state[1][0][1],
                                                 newState.state[1][1][4],
                                                 newState.state[1][4][3],
                                                 newState.state[1][3][0])
        newState.state[1][0][2], \
        newState.state[1][2][4], \
        newState.state[1][4][2], \
        newState.state[1][2][0] = State.circle4F(newState.state[1][0][2],
                                                 newState.state[1][2][4],
                                                 newState.state[1][4][2],
                                                 newState.state[1][2][0])

        newState.state[1][0][3], \
        newState.state[1][3][4], \
        newState.state[1][4][1], \
        newState.state[1][1][0] = State.circle4F(newState.state[1][0][3],
                                                 newState.state[1][3][4],
                                                 newState.state[1][4][1],
                                                 newState.state[1][1][0])

        newState.state[1][1][1], \
        newState.state[1][1][3], \
        newState.state[1][3][3], \
        newState.state[1][3][1] = State.circle4F(newState.state[1][1][1],
                                                 newState.state[1][1][3],
                                                 newState.state[1][3][3],
                                                 newState.state[1][3][1])

        newState.state[1][1][2], \
        newState.state[1][2][3], \
        newState.state[1][3][2], \
        newState.state[1][2][1] = State.circle4F(newState.state[1][1][2],
                                                 newState.state[1][2][3],
                                                 newState.state[1][3][2],
                                                 newState.state[1][2][1])
        return newState

    def RotateL(self):
        newState = deepcopy(self)
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

        newState.state[0][0][3], \
        newState.state[4][0][3], \
        newState.state[5][0][3], \
        newState.state[2][0][3] = State.circle4F(newState.state[0][0][3],
                                                 newState.state[4][0][3],
                                                 newState.state[5][0][3],
                                                 newState.state[2][0][3])

        newState.state[0][0][4], \
        newState.state[4][0][4], \
        newState.state[5][0][4], \
        newState.state[2][0][4] = State.circle4F(newState.state[0][0][4],
                                                 newState.state[4][0][4],
                                                 newState.state[5][0][4],
                                                 newState.state[2][0][4])

        newState.state[1][0][4], \
        newState.state[1][4][4], \
        newState.state[1][4][0], \
        newState.state[1][0][0] = State.circle4B(newState.state[1][0][4],
                                                 newState.state[1][4][4],
                                                 newState.state[1][4][0],
                                                 newState.state[1][0][0])
        newState.state[1][0][1], \
        newState.state[1][1][4], \
        newState.state[1][4][3], \
        newState.state[1][3][0] = State.circle4B(newState.state[1][0][1],
                                                 newState.state[1][1][4],
                                                 newState.state[1][4][3],
                                                 newState.state[1][3][0])
        newState.state[1][0][2], \
        newState.state[1][2][4], \
        newState.state[1][4][2], \
        newState.state[1][2][0] = State.circle4B(newState.state[1][0][2],
                                                 newState.state[1][2][4],
                                                 newState.state[1][4][2],
                                                 newState.state[1][2][0])

        newState.state[1][0][3], \
        newState.state[1][3][4], \
        newState.state[1][4][1], \
        newState.state[1][1][0] = State.circle4B(newState.state[1][0][3],
                                                 newState.state[1][3][4],
                                                 newState.state[1][4][1],
                                                 newState.state[1][1][0])

        newState.state[1][1][1], \
        newState.state[1][1][3], \
        newState.state[1][3][3], \
        newState.state[1][3][1] = State.circle4B(newState.state[1][1][1],
                                                 newState.state[1][1][3],
                                                 newState.state[1][3][3],
                                                 newState.state[1][3][1])

        newState.state[1][1][2], \
        newState.state[1][2][3], \
        newState.state[1][3][2], \
        newState.state[1][2][1] = State.circle4B(newState.state[1][1][2],
                                                 newState.state[1][2][3],
                                                 newState.state[1][3][2],
                                                 newState.state[1][2][1])
        return newState

    def FlipForward(self):
        newState = deepcopy(self)
        newState.state[0][0][0], \
        newState.state[1][0][0], \
        newState.state[5][4][4], \
        newState.state[3][0][0] = State.circle4F(newState.state[0][0][0],
                                                 newState.state[1][0][0],
                                                 newState.state[5][4][4],
                                                 newState.state[3][0][0])
        newState.state[0][0][1], \
        newState.state[1][0][1], \
        newState.state[5][4][3], \
        newState.state[3][0][1] = State.circle4F(newState.state[0][0][1],
                                                 newState.state[1][0][1],
                                                 newState.state[5][4][3],
                                                 newState.state[3][0][1])
        newState.state[0][0][2], \
        newState.state[1][0][2], \
        newState.state[5][4][2], \
        newState.state[3][0][2] = State.circle4F(newState.state[0][0][2],
                                                 newState.state[1][0][2],
                                                 newState.state[5][4][2],
                                                 newState.state[3][0][2])

        newState.state[0][0][3], \
        newState.state[1][0][3], \
        newState.state[5][4][1], \
        newState.state[3][0][3] = State.circle4F(newState.state[0][0][3],
                                                 newState.state[1][0][3],
                                                 newState.state[5][4][1],
                                                 newState.state[3][0][3])

        newState.state[0][0][4], \
        newState.state[1][0][4], \
        newState.state[5][4][0], \
        newState.state[3][0][4] = State.circle4F(newState.state[0][0][4],
                                                 newState.state[1][0][4],
                                                 newState.state[5][4][0],
                                                 newState.state[3][0][4])

        newState.state[0][1][0], \
        newState.state[1][1][0], \
        newState.state[5][3][4], \
        newState.state[3][1][0] = State.circle4F(newState.state[0][1][0],
                                                 newState.state[1][1][0],
                                                 newState.state[5][3][4],
                                                 newState.state[3][1][0])
        newState.state[0][1][1], \
        newState.state[1][1][1], \
        newState.state[5][3][3], \
        newState.state[3][1][1] = State.circle4F(newState.state[0][1][1],
                                                 newState.state[1][1][1],
                                                 newState.state[5][3][3],
                                                 newState.state[3][1][1])
        newState.state[0][1][2], \
        newState.state[1][1][2], \
        newState.state[5][3][2], \
        newState.state[3][1][2] = State.circle4F(newState.state[0][1][2],
                                                 newState.state[1][1][2],
                                                 newState.state[5][3][1],
                                                 newState.state[3][1][2])

        newState.state[0][1][3], \
        newState.state[1][1][3], \
        newState.state[5][3][1], \
        newState.state[3][1][3] = State.circle4F(newState.state[0][1][3],
                                                 newState.state[1][1][3],
                                                 newState.state[5][3][1],
                                                 newState.state[3][1][3])

        newState.state[0][1][4], \
        newState.state[1][1][4], \
        newState.state[5][3][0], \
        newState.state[3][1][4] = State.circle4F(newState.state[0][1][4],
                                                 newState.state[1][1][4],
                                                 newState.state[5][3][0],
                                                 newState.state[3][1][4])

        newState.state[0][2][0], \
        newState.state[1][2][0], \
        newState.state[5][2][4], \
        newState.state[3][2][0] = State.circle4F(newState.state[0][2][0],
                                                 newState.state[1][2][0],
                                                 newState.state[5][2][4],
                                                 newState.state[3][2][0])
        newState.state[0][2][1], \
        newState.state[1][2][1], \
        newState.state[5][2][3], \
        newState.state[3][2][1] = State.circle4F(newState.state[0][2][1],
                                                 newState.state[1][2][1],
                                                 newState.state[5][2][3],
                                                 newState.state[3][2][1])
        newState.state[0][2][2], \
        newState.state[1][2][2], \
        newState.state[5][2][2], \
        newState.state[3][2][2] = State.circle4F(newState.state[0][2][2],
                                                 newState.state[1][2][2],
                                                 newState.state[5][2][2],
                                                 newState.state[3][2][2])

        newState.state[0][2][3], \
        newState.state[1][2][3], \
        newState.state[5][2][1], \
        newState.state[3][2][3] = State.circle4F(newState.state[0][2][3],
                                                 newState.state[1][2][3],
                                                 newState.state[5][2][1],
                                                 newState.state[3][2][3])

        newState.state[0][2][4], \
        newState.state[1][2][4], \
        newState.state[5][2][0], \
        newState.state[3][2][4] = State.circle4F(newState.state[0][2][4],
                                                 newState.state[1][2][4],
                                                 newState.state[5][2][0],
                                                 newState.state[3][2][4])

        newState.state[0][3][0], \
        newState.state[1][3][0], \
        newState.state[5][1][4], \
        newState.state[3][3][0] = State.circle4F(newState.state[0][3][0],
                                                 newState.state[1][3][0],
                                                 newState.state[5][1][4],
                                                 newState.state[3][3][0])

        newState.state[0][3][1], \
        newState.state[1][3][1], \
        newState.state[5][1][3], \
        newState.state[3][3][1] = State.circle4F(newState.state[0][3][1],
                                                 newState.state[1][3][1],
                                                 newState.state[5][1][3],
                                                 newState.state[3][3][1])

        newState.state[0][3][2], \
        newState.state[1][3][2], \
        newState.state[5][1][2], \
        newState.state[3][3][2] = State.circle4F(newState.state[0][3][2],
                                                 newState.state[1][3][2],
                                                 newState.state[5][1][2],
                                                 newState.state[3][3][2])

        newState.state[0][3][3], \
        newState.state[1][3][3], \
        newState.state[5][1][1], \
        newState.state[3][3][3] = State.circle4F(newState.state[0][3][3],
                                                 newState.state[1][3][3],
                                                 newState.state[5][1][1],
                                                 newState.state[3][3][3])

        newState.state[0][3][4], \
        newState.state[1][3][4], \
        newState.state[5][1][0], \
        newState.state[3][3][4] = State.circle4F(newState.state[0][3][4],
                                                 newState.state[1][3][4],
                                                 newState.state[5][1][0],
                                                 newState.state[3][3][4])

        newState.state[0][4][0], \
        newState.state[1][4][0], \
        newState.state[5][0][4], \
        newState.state[3][4][0] = State.circle4F(newState.state[0][4][0],
                                                 newState.state[1][4][0],
                                                 newState.state[5][0][4],
                                                 newState.state[3][4][0])

        newState.state[0][4][1], \
        newState.state[1][4][1], \
        newState.state[5][0][3], \
        newState.state[3][4][1] = State.circle4F(newState.state[0][4][1],
                                                 newState.state[1][4][1],
                                                 newState.state[5][0][3],
                                                 newState.state[3][4][1])

        newState.state[0][4][2], \
        newState.state[1][4][2], \
        newState.state[5][0][2], \
        newState.state[3][4][2] = State.circle4F(newState.state[0][4][2],
                                                 newState.state[1][4][2],
                                                 newState.state[5][0][2],
                                                 newState.state[3][4][2])

        newState.state[0][4][3], \
        newState.state[1][4][3], \
        newState.state[5][0][1], \
        newState.state[3][4][3] = State.circle4F(newState.state[0][4][3],
                                                 newState.state[1][4][3],
                                                 newState.state[5][0][1],
                                                 newState.state[3][4][3])

        newState.state[0][4][4], \
        newState.state[1][4][4], \
        newState.state[5][0][0], \
        newState.state[3][4][4] = State.circle4F(newState.state[0][4][4],
                                                 newState.state[1][4][4],
                                                 newState.state[5][0][0],
                                                 newState.state[3][4][4])

        newState.state[2][0][0], \
        newState.state[2][0][4], \
        newState.state[2][4][4], \
        newState.state[2][4][0] = State.circle4B(newState.state[2][0][0],
                                                 newState.state[2][0][4],
                                                 newState.state[2][4][4],
                                                 newState.state[2][4][0])
        newState.state[2][0][1], \
        newState.state[2][1][4], \
        newState.state[2][4][3], \
        newState.state[2][3][0] = State.circle4B(newState.state[2][0][1],
                                                 newState.state[2][1][4],
                                                 newState.state[2][4][3],
                                                 newState.state[2][3][0])

        newState.state[2][0][2], \
        newState.state[2][2][4], \
        newState.state[2][4][2], \
        newState.state[2][2][0] = State.circle4B(newState.state[2][0][2],
                                                 newState.state[2][2][4],
                                                 newState.state[2][4][2],
                                                 newState.state[2][2][0])

        newState.state[2][0][3], \
        newState.state[2][3][4], \
        newState.state[2][4][1], \
        newState.state[2][1][0] = State.circle4B(newState.state[2][0][3],
                                                 newState.state[2][3][4],
                                                 newState.state[2][4][1],
                                                 newState.state[2][1][0])

        newState.state[2][1][1], \
        newState.state[2][1][3], \
        newState.state[2][3][3], \
        newState.state[2][3][1] = State.circle4B(newState.state[2][1][1],
                                                 newState.state[2][1][3],
                                                 newState.state[2][3][3],
                                                 newState.state[2][3][1])

        newState.state[2][1][2], \
        newState.state[2][2][3], \
        newState.state[2][3][2], \
        newState.state[2][2][1] = State.circle4B(newState.state[2][1][2],
                                                 newState.state[2][2][3],
                                                 newState.state[2][3][2],
                                                 newState.state[2][2][1])

        newState.state[4][0][0], \
        newState.state[4][0][3], \
        newState.state[4][3][3], \
        newState.state[4][3][0] = State.circle4F(newState.state[4][0][0],
                                                 newState.state[4][0][3],
                                                 newState.state[4][3][3],
                                                 newState.state[4][3][0])
        newState.state[4][0][1], \
        newState.state[4][1][3], \
        newState.state[4][3][2], \
        newState.state[4][2][0] = State.circle4F(newState.state[4][0][1],
                                                 newState.state[4][1][3],
                                                 newState.state[4][3][2],
                                                 newState.state[4][2][0])

        newState.state[4][0][2], \
        newState.state[4][2][3], \
        newState.state[4][3][1], \
        newState.state[4][1][0] = State.circle4F(newState.state[4][0][2],
                                                 newState.state[4][2][3],
                                                 newState.state[4][3][1],
                                                 newState.state[4][1][0])

        newState.state[4][1][1], \
        newState.state[4][1][2], \
        newState.state[4][2][2], \
        newState.state[4][2][1] = State.circle4F(newState.state[4][1][1],
                                                 newState.state[4][1][2],
                                                 newState.state[4][2][2],
                                                 newState.state[4][2][1])
        return newState

    def FlipBackward(self):
        newState = deepcopy(self)
        newState.state[0][0][0], \
        newState.state[1][0][0], \
        newState.state[5][4][4], \
        newState.state[3][0][0] = State.circle4B(newState.state[0][0][0],
                                                 newState.state[1][0][0],
                                                 newState.state[5][4][4],
                                                 newState.state[3][0][0])
        newState.state[0][0][1], \
        newState.state[1][0][1], \
        newState.state[5][4][3], \
        newState.state[3][0][1] = State.circle4B(newState.state[0][0][1],
                                                 newState.state[1][0][1],
                                                 newState.state[5][4][3],
                                                 newState.state[3][0][1])
        newState.state[0][0][2], \
        newState.state[1][0][2], \
        newState.state[5][4][2], \
        newState.state[3][0][2] = State.circle4B(newState.state[0][0][2],
                                                 newState.state[1][0][2],
                                                 newState.state[5][4][2],
                                                 newState.state[3][0][2])

        newState.state[0][0][3], \
        newState.state[1][0][3], \
        newState.state[5][4][1], \
        newState.state[3][0][3] = State.circle4B(newState.state[0][0][3],
                                                 newState.state[1][0][3],
                                                 newState.state[5][4][1],
                                                 newState.state[3][0][3])

        newState.state[0][0][4], \
        newState.state[1][0][4], \
        newState.state[5][4][0], \
        newState.state[3][0][4] = State.circle4B(newState.state[0][0][4],
                                                 newState.state[1][0][4],
                                                 newState.state[5][4][0],
                                                 newState.state[3][0][4])

        newState.state[0][1][0], \
        newState.state[1][1][0], \
        newState.state[5][3][4], \
        newState.state[3][1][0] = State.circle4B(newState.state[0][1][0],
                                                 newState.state[1][1][0],
                                                 newState.state[5][3][4],
                                                 newState.state[3][1][0])
        newState.state[0][1][1], \
        newState.state[1][1][1], \
        newState.state[5][3][3], \
        newState.state[3][1][1] = State.circle4B(newState.state[0][1][1],
                                                 newState.state[1][1][1],
                                                 newState.state[5][3][3],
                                                 newState.state[3][1][1])
        newState.state[0][1][2], \
        newState.state[1][1][2], \
        newState.state[5][3][2], \
        newState.state[3][1][2] = State.circle4B(newState.state[0][1][2],
                                                 newState.state[1][1][2],
                                                 newState.state[5][3][1],
                                                 newState.state[3][1][2])

        newState.state[0][1][3], \
        newState.state[1][1][3], \
        newState.state[5][3][1], \
        newState.state[3][1][3] = State.circle4B(newState.state[0][1][3],
                                                 newState.state[1][1][3],
                                                 newState.state[5][3][1],
                                                 newState.state[3][1][3])

        newState.state[0][1][4], \
        newState.state[1][1][4], \
        newState.state[5][3][0], \
        newState.state[3][1][4] = State.circle4B(newState.state[0][1][4],
                                                 newState.state[1][1][4],
                                                 newState.state[5][3][0],
                                                 newState.state[3][1][4])

        newState.state[0][2][0], \
        newState.state[1][2][0], \
        newState.state[5][2][4], \
        newState.state[3][2][0] = State.circle4B(newState.state[0][2][0],
                                                 newState.state[1][2][0],
                                                 newState.state[5][2][4],
                                                 newState.state[3][2][0])
        newState.state[0][2][1], \
        newState.state[1][2][1], \
        newState.state[5][2][3], \
        newState.state[3][2][1] = State.circle4B(newState.state[0][2][1],
                                                 newState.state[1][2][1],
                                                 newState.state[5][2][3],
                                                 newState.state[3][2][1])
        newState.state[0][2][2], \
        newState.state[1][2][2], \
        newState.state[5][2][2], \
        newState.state[3][2][2] = State.circle4B(newState.state[0][2][2],
                                                 newState.state[1][2][2],
                                                 newState.state[5][2][2],
                                                 newState.state[3][2][2])

        newState.state[0][2][3], \
        newState.state[1][2][3], \
        newState.state[5][2][1], \
        newState.state[3][2][3] = State.circle4B(newState.state[0][2][3],
                                                 newState.state[1][2][3],
                                                 newState.state[5][2][1],
                                                 newState.state[3][2][3])

        newState.state[0][2][4], \
        newState.state[1][2][4], \
        newState.state[5][2][0], \
        newState.state[3][2][4] = State.circle4B(newState.state[0][2][4],
                                                 newState.state[1][2][4],
                                                 newState.state[5][2][0],
                                                 newState.state[3][2][4])

        newState.state[0][3][0], \
        newState.state[1][3][0], \
        newState.state[5][1][4], \
        newState.state[3][3][0] = State.circle4B(newState.state[0][3][0],
                                                 newState.state[1][3][0],
                                                 newState.state[5][1][4],
                                                 newState.state[3][3][0])

        newState.state[0][3][1], \
        newState.state[1][3][1], \
        newState.state[5][1][3], \
        newState.state[3][3][1] = State.circle4B(newState.state[0][3][1],
                                                 newState.state[1][3][1],
                                                 newState.state[5][1][3],
                                                 newState.state[3][3][1])

        newState.state[0][3][2], \
        newState.state[1][3][2], \
        newState.state[5][1][2], \
        newState.state[3][3][2] = State.circle4B(newState.state[0][3][2],
                                                 newState.state[1][3][2],
                                                 newState.state[5][1][2],
                                                 newState.state[3][3][2])

        newState.state[0][3][3], \
        newState.state[1][3][3], \
        newState.state[5][1][1], \
        newState.state[3][3][3] = State.circle4B(newState.state[0][3][3],
                                                 newState.state[1][3][3],
                                                 newState.state[5][1][1],
                                                 newState.state[3][3][3])

        newState.state[0][3][4], \
        newState.state[1][3][4], \
        newState.state[5][1][0], \
        newState.state[3][3][4] = State.circle4B(newState.state[0][3][4],
                                                 newState.state[1][3][4],
                                                 newState.state[5][1][0],
                                                 newState.state[3][3][4])

        newState.state[0][4][0], \
        newState.state[1][4][0], \
        newState.state[5][0][4], \
        newState.state[3][4][0] = State.circle4B(newState.state[0][4][0],
                                                 newState.state[1][4][0],
                                                 newState.state[5][0][4],
                                                 newState.state[3][4][0])

        newState.state[0][4][1], \
        newState.state[1][4][1], \
        newState.state[5][0][3], \
        newState.state[3][4][1] = State.circle4B(newState.state[0][4][1],
                                                 newState.state[1][4][1],
                                                 newState.state[5][0][3],
                                                 newState.state[3][4][1])

        newState.state[0][4][2], \
        newState.state[1][4][2], \
        newState.state[5][0][2], \
        newState.state[3][4][2] = State.circle4B(newState.state[0][4][2],
                                                 newState.state[1][4][2],
                                                 newState.state[5][0][2],
                                                 newState.state[3][4][2])

        newState.state[0][4][3], \
        newState.state[1][4][3], \
        newState.state[5][0][1], \
        newState.state[3][4][3] = State.circle4B(newState.state[0][4][3],
                                                 newState.state[1][4][3],
                                                 newState.state[5][0][1],
                                                 newState.state[3][4][3])

        newState.state[0][4][4], \
        newState.state[1][4][4], \
        newState.state[5][0][0], \
        newState.state[3][4][4] = State.circle4B(newState.state[0][4][4],
                                                 newState.state[1][4][4],
                                                 newState.state[5][0][0],
                                                 newState.state[3][4][4])

        newState.state[2][0][0], \
        newState.state[2][0][4], \
        newState.state[2][4][4], \
        newState.state[2][4][0] = State.circle4F(newState.state[2][0][0],
                                                 newState.state[2][0][4],
                                                 newState.state[2][4][4],
                                                 newState.state[2][4][0])
        newState.state[2][0][1], \
        newState.state[2][1][4], \
        newState.state[2][4][3], \
        newState.state[2][3][0] = State.circle4F(newState.state[2][0][1],
                                                 newState.state[2][1][4],
                                                 newState.state[2][4][3],
                                                 newState.state[2][3][0])

        newState.state[2][0][2], \
        newState.state[2][2][4], \
        newState.state[2][4][2], \
        newState.state[2][2][0] = State.circle4F(newState.state[2][0][2],
                                                 newState.state[2][2][4],
                                                 newState.state[2][4][2],
                                                 newState.state[2][2][0])

        newState.state[2][0][3], \
        newState.state[2][3][4], \
        newState.state[2][4][1], \
        newState.state[2][1][0] = State.circle4F(newState.state[2][0][3],
                                                 newState.state[2][3][4],
                                                 newState.state[2][4][1],
                                                 newState.state[2][1][0])

        newState.state[2][1][1], \
        newState.state[2][1][3], \
        newState.state[2][3][3], \
        newState.state[2][3][1] = State.circle4F(newState.state[2][1][1],
                                                 newState.state[2][1][3],
                                                 newState.state[2][3][3],
                                                 newState.state[2][3][1])

        newState.state[2][1][2], \
        newState.state[2][2][3], \
        newState.state[2][3][2], \
        newState.state[2][2][1] = State.circle4F(newState.state[2][1][2],
                                                 newState.state[2][2][3],
                                                 newState.state[2][3][2],
                                                 newState.state[2][2][1])

        newState.state[4][0][0], \
        newState.state[4][0][3], \
        newState.state[4][3][3], \
        newState.state[4][3][0] = State.circle4B(newState.state[4][0][0],
                                                 newState.state[4][0][3],
                                                 newState.state[4][3][3],
                                                 newState.state[4][3][0])
        newState.state[4][0][1], \
        newState.state[4][1][3], \
        newState.state[4][3][2], \
        newState.state[4][2][0] = State.circle4B(newState.state[4][0][1],
                                                 newState.state[4][1][3],
                                                 newState.state[4][3][2],
                                                 newState.state[4][2][0])

        newState.state[4][0][2], \
        newState.state[4][2][3], \
        newState.state[4][3][1], \
        newState.state[4][1][0] = State.circle4B(newState.state[4][0][2],
                                                 newState.state[4][2][3],
                                                 newState.state[4][3][1],
                                                 newState.state[4][1][0])

        newState.state[4][1][1], \
        newState.state[4][1][2], \
        newState.state[4][2][2], \
        newState.state[4][2][1] = State.circle4B(newState.state[4][1][1],
                                                 newState.state[4][1][2],
                                                 newState.state[4][2][2],
                                                 newState.state[4][2][1])
        return newState

    def FlipRight(self):
        newState = deepcopy(self)
        newState.state[1][0][0], \
        newState.state[2][4][0], \
        newState.state[3][4][4], \
        newState.state[4][0][4] = State.circle4F(newState.state[1][0][0],
                                                 newState.state[2][4][0],
                                                 newState.state[3][4][4],
                                                 newState.state[4][0][4])
        newState.state[1][0][1], \
        newState.state[2][3][0], \
        newState.state[3][4][3], \
        newState.state[4][1][4] = State.circle4F(newState.state[1][0][1],
                                                 newState.state[2][3][0],
                                                 newState.state[3][4][3],
                                                 newState.state[4][1][4])
        newState.state[1][0][2], \
        newState.state[2][2][0], \
        newState.state[3][4][2], \
        newState.state[4][2][4] = State.circle4F(newState.state[1][0][2],
                                                 newState.state[2][2][0],
                                                 newState.state[3][4][2],
                                                 newState.state[4][2][4])

        newState.state[1][0][3], \
        newState.state[2][1][0], \
        newState.state[3][4][1], \
        newState.state[4][3][4] = State.circle4F(newState.state[1][0][3],
                                                 newState.state[2][1][0],
                                                 newState.state[3][4][1],
                                                 newState.state[4][3][4])

        newState.state[1][0][4], \
        newState.state[2][0][0], \
        newState.state[3][4][0], \
        newState.state[4][4][4] = State.circle4F(newState.state[1][0][4],
                                                 newState.state[2][0][0],
                                                 newState.state[3][4][0],
                                                 newState.state[4][4][4])

        newState.state[1][1][0], \
        newState.state[2][4][1], \
        newState.state[3][3][4], \
        newState.state[4][0][3] = State.circle4F(newState.state[1][1][0],
                                                 newState.state[2][4][1],
                                                 newState.state[3][3][4],
                                                 newState.state[4][0][3])
        newState.state[1][1][1], \
        newState.state[2][3][1], \
        newState.state[3][3][3], \
        newState.state[4][1][3] = State.circle4F(newState.state[1][1][1],
                                                 newState.state[2][3][1],
                                                 newState.state[3][3][3],
                                                 newState.state[4][1][3])
        newState.state[1][1][2], \
        newState.state[2][2][1], \
        newState.state[3][3][2], \
        newState.state[4][2][3] = State.circle4F(newState.state[1][1][2],
                                                 newState.state[2][2][1],
                                                 newState.state[3][3][2],
                                                 newState.state[4][2][3])

        newState.state[1][1][3], \
        newState.state[2][1][1], \
        newState.state[3][3][1], \
        newState.state[4][3][3] = State.circle4F(newState.state[1][1][3],
                                                 newState.state[2][1][1],
                                                 newState.state[3][3][1],
                                                 newState.state[4][3][3])

        newState.state[1][1][4], \
        newState.state[2][0][1], \
        newState.state[3][3][0], \
        newState.state[4][4][3] = State.circle4F(newState.state[1][1][4],
                                                 newState.state[2][0][1],
                                                 newState.state[3][3][0],
                                                 newState.state[4][4][3])

        newState.state[1][2][0], \
        newState.state[2][4][2], \
        newState.state[3][2][4], \
        newState.state[4][0][2] = State.circle4F(newState.state[1][2][0],
                                                 newState.state[2][4][2],
                                                 newState.state[3][2][4],
                                                 newState.state[4][0][2])
        newState.state[1][2][1], \
        newState.state[2][3][2], \
        newState.state[3][2][3], \
        newState.state[4][1][2] = State.circle4F(newState.state[1][2][1],
                                                 newState.state[2][3][2],
                                                 newState.state[3][2][3],
                                                 newState.state[4][1][2])
        newState.state[1][2][2], \
        newState.state[2][2][2], \
        newState.state[3][2][2], \
        newState.state[4][2][2] = State.circle4F(newState.state[1][2][2],
                                                 newState.state[2][2][2],
                                                 newState.state[3][2][2],
                                                 newState.state[4][2][2])

        newState.state[1][2][3], \
        newState.state[2][1][2], \
        newState.state[3][2][1], \
        newState.state[4][3][2] = State.circle4F(newState.state[1][2][3],
                                                 newState.state[2][1][2],
                                                 newState.state[3][2][1],
                                                 newState.state[4][3][2])

        newState.state[1][2][4], \
        newState.state[2][0][2], \
        newState.state[3][2][0], \
        newState.state[4][4][2] = State.circle4F(newState.state[1][2][4],
                                                 newState.state[2][0][2],
                                                 newState.state[3][2][0],
                                                 newState.state[4][4][2])

        newState.state[1][3][0], \
        newState.state[2][4][3], \
        newState.state[3][1][4], \
        newState.state[4][0][1] = State.circle4F(newState.state[1][3][0],
                                                 newState.state[2][4][3],
                                                 newState.state[3][1][4],
                                                 newState.state[4][0][1])

        newState.state[1][3][1], \
        newState.state[2][3][3], \
        newState.state[3][1][3], \
        newState.state[4][1][1] = State.circle4F(newState.state[1][3][1],
                                                 newState.state[2][3][3],
                                                 newState.state[3][1][3],
                                                 newState.state[4][1][1])
        newState.state[1][3][2], \
        newState.state[2][2][3], \
        newState.state[3][1][2], \
        newState.state[4][2][1] = State.circle4F(newState.state[1][3][2],
                                                 newState.state[2][2][3],
                                                 newState.state[3][1][2],
                                                 newState.state[4][2][1])

        newState.state[1][3][3], \
        newState.state[2][1][3], \
        newState.state[3][1][1], \
        newState.state[4][3][1] = State.circle4F(newState.state[1][3][3],
                                                 newState.state[2][1][3],
                                                 newState.state[3][1][1],
                                                 newState.state[4][3][1])

        newState.state[1][3][4], \
        newState.state[2][0][3], \
        newState.state[3][1][0], \
        newState.state[4][4][1] = State.circle4F(newState.state[1][3][4],
                                                 newState.state[2][0][3],
                                                 newState.state[3][1][0],
                                                 newState.state[4][4][1])

        newState.state[1][4][0], \
        newState.state[2][4][4], \
        newState.state[3][0][4], \
        newState.state[4][0][0] = State.circle4F(newState.state[1][4][0],
                                                 newState.state[2][4][4],
                                                 newState.state[3][0][4],
                                                 newState.state[4][0][0])
        newState.state[1][4][1], \
        newState.state[2][3][4], \
        newState.state[3][0][3], \
        newState.state[4][1][0] = State.circle4F(newState.state[1][4][1],
                                                 newState.state[2][3][4],
                                                 newState.state[3][0][3],
                                                 newState.state[4][1][0])

        newState.state[1][4][2], \
        newState.state[2][2][4], \
        newState.state[3][0][2], \
        newState.state[4][2][0] = State.circle4F(newState.state[1][4][2],
                                                 newState.state[2][2][4],
                                                 newState.state[3][0][2],
                                                 newState.state[4][2][0])

        newState.state[1][4][3], \
        newState.state[2][1][4], \
        newState.state[3][0][1], \
        newState.state[4][3][0] = State.circle4F(newState.state[1][4][3],
                                                 newState.state[2][1][4],
                                                 newState.state[3][0][1],
                                                 newState.state[4][3][0])

        newState.state[1][4][4], \
        newState.state[2][0][4], \
        newState.state[3][0][0], \
        newState.state[4][4][0] = State.circle4F(newState.state[1][4][4],
                                                 newState.state[2][0][4],
                                                 newState.state[3][0][0],
                                                 newState.state[4][4][0])

        newState.state[0][0][0], \
        newState.state[0][0][4], \
        newState.state[0][4][4], \
        newState.state[0][4][0] = State.circle4B(newState.state[0][0][0],
                                                 newState.state[0][0][4],
                                                 newState.state[0][4][4],
                                                 newState.state[0][4][0])
        newState.state[0][0][1], \
        newState.state[0][1][4], \
        newState.state[0][4][3], \
        newState.state[0][3][0] = State.circle4B(newState.state[0][0][1],
                                                 newState.state[0][1][4],
                                                 newState.state[0][4][3],
                                                 newState.state[0][3][0])

        newState.state[0][0][2], \
        newState.state[0][2][4], \
        newState.state[0][4][2], \
        newState.state[0][2][0] = State.circle4B(newState.state[0][0][2],
                                                 newState.state[0][2][4],
                                                 newState.state[0][4][2],
                                                 newState.state[0][2][0])

        newState.state[0][0][3], \
        newState.state[0][3][4], \
        newState.state[0][4][1], \
        newState.state[0][1][0] = State.circle4B(newState.state[0][0][3],
                                                 newState.state[0][3][4],
                                                 newState.state[0][4][1],
                                                 newState.state[0][1][0])

        newState.state[0][1][1], \
        newState.state[0][1][3], \
        newState.state[0][3][3], \
        newState.state[0][3][1] = State.circle4B(newState.state[0][1][1],
                                                 newState.state[0][1][3],
                                                 newState.state[0][3][3],
                                                 newState.state[0][3][1])

        newState.state[0][1][2], \
        newState.state[0][2][3], \
        newState.state[0][3][2], \
        newState.state[0][2][1] = State.circle4B(newState.state[0][1][2],
                                                 newState.state[0][2][3],
                                                 newState.state[0][3][2],
                                                 newState.state[0][2][1])

        newState.state[5][0][0], \
        newState.state[5][0][4], \
        newState.state[5][4][4], \
        newState.state[5][4][0] = State.circle4F(newState.state[5][0][0],
                                                 newState.state[5][0][4],
                                                 newState.state[5][4][4],
                                                 newState.state[5][4][0])
        newState.state[5][0][1], \
        newState.state[5][1][4], \
        newState.state[5][4][3], \
        newState.state[5][3][0] = State.circle4F(newState.state[5][0][1],
                                                 newState.state[5][1][4],
                                                 newState.state[5][4][3],
                                                 newState.state[5][3][0])

        newState.state[5][0][2], \
        newState.state[5][2][4], \
        newState.state[5][4][2], \
        newState.state[5][2][0] = State.circle4F(newState.state[5][0][2],
                                                 newState.state[5][2][4],
                                                 newState.state[5][4][2],
                                                 newState.state[5][2][0])

        newState.state[5][0][3], \
        newState.state[5][3][4], \
        newState.state[5][4][1], \
        newState.state[5][1][0] = State.circle4F(newState.state[5][0][3],
                                                 newState.state[5][3][4],
                                                 newState.state[5][4][1],
                                                 newState.state[5][1][0])

        newState.state[5][1][1], \
        newState.state[5][1][3], \
        newState.state[5][3][3], \
        newState.state[5][3][1] = State.circle4F(newState.state[5][1][1],
                                                 newState.state[5][1][3],
                                                 newState.state[5][3][3],
                                                 newState.state[5][3][1])

        newState.state[5][1][2], \
        newState.state[5][2][3], \
        newState.state[5][3][2], \
        newState.state[5][2][1] = State.circle4F(newState.state[5][1][2],
                                                 newState.state[5][2][3],
                                                 newState.state[5][3][2],
                                                 newState.state[5][2][1])

        return newState

    def FlipLeft(self):
        newState = deepcopy(self)
        newState.state[1][0][0], \
        newState.state[2][4][0], \
        newState.state[3][4][4], \
        newState.state[4][0][4] = State.circle4B(newState.state[1][0][0],
                                                 newState.state[2][4][0],
                                                 newState.state[3][4][4],
                                                 newState.state[4][0][4])
        newState.state[1][0][1], \
        newState.state[2][3][0], \
        newState.state[3][4][3], \
        newState.state[4][1][4] = State.circle4B(newState.state[1][0][1],
                                                 newState.state[2][3][0],
                                                 newState.state[3][4][3],
                                                 newState.state[4][1][4])
        newState.state[1][0][2], \
        newState.state[2][2][0], \
        newState.state[3][4][2], \
        newState.state[4][2][4] = State.circle4B(newState.state[1][0][2],
                                                 newState.state[2][2][0],
                                                 newState.state[3][4][2],
                                                 newState.state[4][2][4])

        newState.state[1][0][3], \
        newState.state[2][1][0], \
        newState.state[3][4][1], \
        newState.state[4][3][4] = State.circle4B(newState.state[1][0][3],
                                                 newState.state[2][1][0],
                                                 newState.state[3][4][1],
                                                 newState.state[4][3][4])

        newState.state[1][0][4], \
        newState.state[2][0][0], \
        newState.state[3][4][0], \
        newState.state[4][4][4] = State.circle4B(newState.state[1][0][4],
                                                 newState.state[2][0][0],
                                                 newState.state[3][4][0],
                                                 newState.state[4][4][4])

        newState.state[1][1][0], \
        newState.state[2][4][1], \
        newState.state[3][3][4], \
        newState.state[4][0][3] = State.circle4B(newState.state[1][1][0],
                                                 newState.state[2][4][1],
                                                 newState.state[3][3][4],
                                                 newState.state[4][0][3])
        newState.state[1][1][1], \
        newState.state[2][3][1], \
        newState.state[3][3][3], \
        newState.state[4][1][3] = State.circle4B(newState.state[1][1][1],
                                                 newState.state[2][3][1],
                                                 newState.state[3][3][3],
                                                 newState.state[4][1][3])
        newState.state[1][1][2], \
        newState.state[2][2][1], \
        newState.state[3][3][2], \
        newState.state[4][2][3] = State.circle4B(newState.state[1][1][2],
                                                 newState.state[2][2][1],
                                                 newState.state[3][3][2],
                                                 newState.state[4][2][3])

        newState.state[1][1][3], \
        newState.state[2][1][1], \
        newState.state[3][3][1], \
        newState.state[4][3][3] = State.circle4B(newState.state[1][1][3],
                                                 newState.state[2][1][1],
                                                 newState.state[3][3][1],
                                                 newState.state[4][3][3])

        newState.state[1][1][4], \
        newState.state[2][0][1], \
        newState.state[3][3][0], \
        newState.state[4][4][3] = State.circle4B(newState.state[1][1][4],
                                                 newState.state[2][0][1],
                                                 newState.state[3][3][0],
                                                 newState.state[4][4][3])

        newState.state[1][2][0], \
        newState.state[2][4][2], \
        newState.state[3][2][4], \
        newState.state[4][0][2] = State.circle4B(newState.state[1][2][0],
                                                 newState.state[2][4][2],
                                                 newState.state[3][2][4],
                                                 newState.state[4][0][2])
        newState.state[1][2][1], \
        newState.state[2][3][2], \
        newState.state[3][2][3], \
        newState.state[4][1][2] = State.circle4B(newState.state[1][2][1],
                                                 newState.state[2][3][2],
                                                 newState.state[3][2][3],
                                                 newState.state[4][1][2])
        newState.state[1][2][2], \
        newState.state[2][2][2], \
        newState.state[3][2][2], \
        newState.state[4][2][2] = State.circle4B(newState.state[1][2][2],
                                                 newState.state[2][2][2],
                                                 newState.state[3][2][2],
                                                 newState.state[4][2][2])

        newState.state[1][2][3], \
        newState.state[2][1][2], \
        newState.state[3][2][1], \
        newState.state[4][3][2] = State.circle4B(newState.state[1][2][3],
                                                 newState.state[2][1][2],
                                                 newState.state[3][2][1],
                                                 newState.state[4][3][2])

        newState.state[1][2][4], \
        newState.state[2][0][2], \
        newState.state[3][2][0], \
        newState.state[4][4][2] = State.circle4B(newState.state[1][2][4],
                                                 newState.state[2][0][2],
                                                 newState.state[3][2][0],
                                                 newState.state[4][4][2])

        newState.state[1][3][0], \
        newState.state[2][4][3], \
        newState.state[3][1][4], \
        newState.state[4][0][1] = State.circle4B(newState.state[1][3][0],
                                                 newState.state[2][4][3],
                                                 newState.state[3][1][4],
                                                 newState.state[4][0][1])

        newState.state[1][3][1], \
        newState.state[2][3][3], \
        newState.state[3][1][3], \
        newState.state[4][1][1] = State.circle4B(newState.state[1][3][1],
                                                 newState.state[2][3][3],
                                                 newState.state[3][1][3],
                                                 newState.state[4][1][1])
        newState.state[1][3][2], \
        newState.state[2][2][3], \
        newState.state[3][1][2], \
        newState.state[4][2][1] = State.circle4B(newState.state[1][3][2],
                                                 newState.state[2][2][3],
                                                 newState.state[3][1][2],
                                                 newState.state[4][2][1])

        newState.state[1][3][3], \
        newState.state[2][1][3], \
        newState.state[3][1][1], \
        newState.state[4][3][1] = State.circle4B(newState.state[1][3][3],
                                                 newState.state[2][1][3],
                                                 newState.state[3][1][1],
                                                 newState.state[4][3][1])

        newState.state[1][3][4], \
        newState.state[2][0][3], \
        newState.state[3][1][0], \
        newState.state[4][4][1] = State.circle4B(newState.state[1][3][4],
                                                 newState.state[2][0][3],
                                                 newState.state[3][1][0],
                                                 newState.state[4][4][1])

        newState.state[1][4][0], \
        newState.state[2][4][4], \
        newState.state[3][0][4], \
        newState.state[4][0][0] = State.circle4B(newState.state[1][4][0],
                                                 newState.state[2][4][4],
                                                 newState.state[3][0][4],
                                                 newState.state[4][0][0])
        newState.state[1][4][1], \
        newState.state[2][3][4], \
        newState.state[3][0][3], \
        newState.state[4][1][0] = State.circle4B(newState.state[1][4][1],
                                                 newState.state[2][3][4],
                                                 newState.state[3][0][3],
                                                 newState.state[4][1][0])

        newState.state[1][4][2], \
        newState.state[2][2][4], \
        newState.state[3][0][2], \
        newState.state[4][2][0] = State.circle4B(newState.state[1][4][2],
                                                 newState.state[2][2][4],
                                                 newState.state[3][0][2],
                                                 newState.state[4][2][0])

        newState.state[1][4][3], \
        newState.state[2][1][4], \
        newState.state[3][0][1], \
        newState.state[4][3][0] = State.circle4B(newState.state[1][4][3],
                                                 newState.state[2][1][4],
                                                 newState.state[3][0][1],
                                                 newState.state[4][3][0])

        newState.state[1][4][4], \
        newState.state[2][0][4], \
        newState.state[3][0][0], \
        newState.state[4][4][0] = State.circle4B(newState.state[1][4][4],
                                                 newState.state[2][0][4],
                                                 newState.state[3][0][0],
                                                 newState.state[4][4][0])

        newState.state[0][0][0], \
        newState.state[0][0][4], \
        newState.state[0][4][4], \
        newState.state[0][4][0] = State.circle4F(newState.state[0][0][0],
                                                 newState.state[0][0][4],
                                                 newState.state[0][4][4],
                                                 newState.state[0][4][0])
        newState.state[0][0][1], \
        newState.state[0][1][4], \
        newState.state[0][4][3], \
        newState.state[0][3][0] = State.circle4F(newState.state[0][0][1],
                                                 newState.state[0][1][4],
                                                 newState.state[0][4][3],
                                                 newState.state[0][3][0])

        newState.state[0][0][2], \
        newState.state[0][2][4], \
        newState.state[0][4][2], \
        newState.state[0][2][0] = State.circle4F(newState.state[0][0][2],
                                                 newState.state[0][2][4],
                                                 newState.state[0][4][2],
                                                 newState.state[0][2][0])

        newState.state[0][0][3], \
        newState.state[0][3][4], \
        newState.state[0][4][1], \
        newState.state[0][1][0] = State.circle4F(newState.state[0][0][3],
                                                 newState.state[0][3][4],
                                                 newState.state[0][4][1],
                                                 newState.state[0][1][0])

        newState.state[0][1][1], \
        newState.state[0][1][3], \
        newState.state[0][3][3], \
        newState.state[0][3][1] = State.circle4F(newState.state[0][1][1],
                                                 newState.state[0][1][3],
                                                 newState.state[0][3][3],
                                                 newState.state[0][3][1])

        newState.state[0][1][2], \
        newState.state[0][2][3], \
        newState.state[0][3][2], \
        newState.state[0][2][1] = State.circle4F(newState.state[0][1][2],
                                                 newState.state[0][2][3],
                                                 newState.state[0][3][2],
                                                 newState.state[0][2][1])

        newState.state[5][0][0], \
        newState.state[5][0][4], \
        newState.state[5][4][4], \
        newState.state[5][4][0] = State.circle4B(newState.state[5][0][0],
                                                 newState.state[5][0][4],
                                                 newState.state[5][4][4],
                                                 newState.state[5][4][0])
        newState.state[5][0][1], \
        newState.state[5][1][4], \
        newState.state[5][4][3], \
        newState.state[5][3][0] = State.circle4B(newState.state[5][0][1],
                                                 newState.state[5][1][4],
                                                 newState.state[5][4][3],
                                                 newState.state[5][3][0])

        newState.state[5][0][2], \
        newState.state[5][2][4], \
        newState.state[5][4][2], \
        newState.state[5][2][0] = State.circle4B(newState.state[5][0][2],
                                                 newState.state[5][2][4],
                                                 newState.state[5][4][2],
                                                 newState.state[5][2][0])

        newState.state[5][0][3], \
        newState.state[5][3][4], \
        newState.state[5][4][1], \
        newState.state[5][1][0] = State.circle4B(newState.state[5][0][3],
                                                 newState.state[5][3][4],
                                                 newState.state[5][4][1],
                                                 newState.state[5][1][0])

        newState.state[5][1][1], \
        newState.state[5][1][3], \
        newState.state[5][3][3], \
        newState.state[5][3][1] = State.circle4B(newState.state[5][1][1],
                                                 newState.state[5][1][3],
                                                 newState.state[5][3][3],
                                                 newState.state[5][3][1])

        newState.state[5][1][2], \
        newState.state[5][2][3], \
        newState.state[5][3][2], \
        newState.state[5][2][1] = State.circle4B(newState.state[5][1][2],
                                                 newState.state[5][2][3],
                                                 newState.state[5][3][2],
                                                 newState.state[5][2][1])

        return newState

    def switchIndexes(self, num_of_rotate):
        newState = deepcopy(self)
        for j in range(6):
            for k in range(num_of_rotate[j]):
                newState.state[j][0][4], \
                newState.state[j][4][4], \
                newState.state[j][4][0], \
                newState.state[j][0][0] = State.circle4F(newState.state[j][0][4],
                                                         newState.state[j][4][4],
                                                         newState.state[j][4][0],
                                                         newState.state[j][0][0])
                newState.state[j][0][1], \
                newState.state[j][1][4], \
                newState.state[j][4][3], \
                newState.state[j][3][0] = State.circle4F(newState.state[j][0][1],
                                                         newState.state[j][1][4],
                                                         newState.state[j][4][3],
                                                         newState.state[j][3][0])
                newState.state[j][0][2], \
                newState.state[j][2][4], \
                newState.state[j][4][2], \
                newState.state[j][2][0] = State.circle4F(newState.state[j][0][2],
                                                         newState.state[j][2][4],
                                                         newState.state[j][4][2],
                                                         newState.state[j][2][0])

                newState.state[j][0][3], \
                newState.state[j][3][4], \
                newState.state[j][4][1], \
                newState.state[j][1][0] = State.circle4F(newState.state[j][0][3],
                                                         newState.state[j][3][4],
                                                         newState.state[j][4][1],
                                                         newState.state[j][1][0])

                newState.state[j][1][1], \
                newState.state[j][1][3], \
                newState.state[j][3][3], \
                newState.state[j][3][1] = State.circle4F(newState.state[j][1][1],
                                                         newState.state[j][1][3],
                                                         newState.state[j][3][3],
                                                         newState.state[j][3][1])

                newState.state[j][1][2], \
                newState.state[j][2][3], \
                newState.state[j][3][2], \
                newState.state[j][2][1] = State.circle4F(newState.state[j][1][2],
                                                         newState.state[j][2][3],
                                                         newState.state[j][3][2],
                                                         newState.state[j][2][1])
        return newState
