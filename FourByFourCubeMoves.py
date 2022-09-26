from copy import deepcopy

from Color import Color

goal = [
    [[Color.RED, Color.RED, Color.RED, Color.RED],
     [Color.RED, Color.RED, Color.RED, Color.RED],
     [Color.RED, Color.RED, Color.RED, Color.RED],
     [Color.RED, Color.RED, Color.RED, Color.RED]],
    [[Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN],
     [Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN],
     [Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN],
     [Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN]],
    [[Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW],
     [Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW],
     [Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW],
     [Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW]],
    [[Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE],
     [Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE],
     [Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE],
     [Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE]],
    [[Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE],
     [Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE],
     [Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE],
     [Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE]],
    [[Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE],
     [Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE],
     [Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE],
     [Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE]]
]
# by default F:red  U:green

test = [
    [[Color.ORANGE, Color.GREEN, Color.YELLOW, Color.WHITE],
     [Color.GREEN, Color.RED, Color.YELLOW, Color.ORANGE],
     [Color.RED, Color.BLUE, Color.RED, Color.ORANGE],
     [Color.ORANGE, Color.BLUE, Color.RED, Color.WHITE]],
    [[Color.YELLOW, Color.WHITE, Color.BLUE, Color.RED],
     [Color.GREEN, Color.YELLOW, Color.GREEN, Color.YELLOW],
     [Color.RED, Color.ORANGE, Color.GREEN, Color.YELLOW],
     [Color.BLUE, Color.ORANGE, Color.BLUE, Color.ORANGE]],
    [[Color.GREEN, Color.YELLOW, Color.WHITE, Color.YELLOW],
     [Color.ORANGE, Color.BLUE, Color.RED, Color.ORANGE],
     [Color.BLUE, Color.YELLOW, Color.GREEN, Color.BLUE],
     [Color.RED, Color.RED, Color.GREEN, Color.YELLOW]],
    [[Color.GREEN, Color.ORANGE, Color.GREEN, Color.ORANGE],
     [Color.YELLOW, Color.ORANGE, Color.BLUE, Color.GREEN],
     [Color.WHITE, Color.RED, Color.BLUE, Color.WHITE],
     [Color.WHITE, Color.RED, Color.ORANGE, Color.GREEN]],
    [[Color.BLUE, Color.RED, Color.RED, Color.YELLOW],
     [Color.YELLOW, Color.GREEN, Color.YELLOW, Color.WHITE],
     [Color.YELLOW, Color.WHITE, Color.WHITE, Color.ORANGE],
     [Color.GREEN, Color.WHITE, Color.BLUE, Color.WHITE]],
    [[Color.BLUE, Color.YELLOW, Color.GREEN, Color.RED],
     [Color.BLUE, Color.WHITE, Color.WHITE, Color.BLUE],
     [Color.WHITE, Color.ORANGE, Color.ORANGE, Color.RED],
     [Color.RED, Color.WHITE, Color.GREEN, Color.BLUE]]
]


def circle4F(w, x, y, z):
    temp = w
    w = x
    x = y
    y = z
    z = temp
    return w, x, y, z


def circle4B(w, x, y, z):
    temp = z
    z = y
    y = x
    x = w
    w = temp
    return w, x, y, z


def L1R(state):
    newState = deepcopy(state)
    newState[0][3][0], \
    newState[4][3][0], \
    newState[5][3][0], \
    newState[2][3][0] = circle4B(newState[0][3][0],
                                 newState[4][3][0],
                                 newState[5][3][0],
                                 newState[2][3][0])
    newState[0][3][1], \
    newState[4][3][1], \
    newState[5][3][1], \
    newState[2][3][1] = circle4B(newState[0][3][1],
                                 newState[4][3][1],
                                 newState[5][3][1],
                                 newState[2][3][1])
    newState[0][3][2], \
    newState[4][3][2], \
    newState[5][3][2], \
    newState[2][3][2] = circle4B(newState[0][3][2],
                                 newState[4][3][2],
                                 newState[5][3][2],
                                 newState[2][3][2])

    newState[0][3][3], \
    newState[4][3][3], \
    newState[5][3][3], \
    newState[2][3][3] = circle4B(newState[0][3][3],
                                 newState[4][3][3],
                                 newState[5][3][3],
                                 newState[2][3][3])

    newState[3][0][3], \
    newState[3][3][3], \
    newState[3][3][0], \
    newState[3][0][0] = circle4B(newState[3][0][3],
                                 newState[3][3][3],
                                 newState[3][3][0],
                                 newState[3][0][0])
    newState[3][0][1], \
    newState[3][1][3], \
    newState[3][3][2], \
    newState[3][2][0] = circle4B(newState[3][0][1],
                                 newState[3][1][3],
                                 newState[3][3][2],
                                 newState[3][2][0])
    newState[3][0][2], \
    newState[3][2][3], \
    newState[3][3][1], \
    newState[3][1][0] = circle4B(newState[3][0][2],
                                 newState[3][2][3],
                                 newState[3][3][1],
                                 newState[3][1][0])

    newState[3][1][1], \
    newState[3][1][2], \
    newState[3][2][2], \
    newState[3][2][1] = circle4B(newState[3][1][1],
                                 newState[3][1][2],
                                 newState[3][2][2],
                                 newState[3][2][1])

    return newState


# for line in L1R(test):
#     for line1 in line:
#         print(line1)

def L1L(state):
    newState = deepcopy(state)
    newState[0][3][0], \
    newState[4][3][0], \
    newState[5][3][0], \
    newState[2][3][0] = circle4F(newState[0][3][0],
                                 newState[4][3][0],
                                 newState[5][3][0],
                                 newState[2][3][0])
    newState[0][3][1], \
    newState[4][3][1], \
    newState[5][3][1], \
    newState[2][3][1] = circle4F(newState[0][3][1],
                                 newState[4][3][1],
                                 newState[5][3][1],
                                 newState[2][3][1])
    newState[0][3][2], \
    newState[4][3][2], \
    newState[5][3][2], \
    newState[2][3][2] = circle4F(newState[0][3][2],
                                 newState[4][3][2],
                                 newState[5][3][2],
                                 newState[2][3][2])

    newState[0][3][3], \
    newState[4][3][3], \
    newState[5][3][3], \
    newState[2][3][3] = circle4F(newState[0][3][3],
                                 newState[4][3][3],
                                 newState[5][3][3],
                                 newState[2][3][3])

    newState[3][0][3], \
    newState[3][3][3], \
    newState[3][3][0], \
    newState[3][0][0] = circle4F(newState[3][0][3],
                                 newState[3][3][3],
                                 newState[3][3][0],
                                 newState[3][0][0])
    newState[3][0][1], \
    newState[3][1][3], \
    newState[3][3][2], \
    newState[3][2][0] = circle4F(newState[3][0][1],
                                 newState[3][1][3],
                                 newState[3][3][2],
                                 newState[3][2][0])
    newState[3][0][2], \
    newState[3][2][3], \
    newState[3][3][1], \
    newState[3][1][0] = circle4F(newState[3][0][2],
                                 newState[3][2][3],
                                 newState[3][3][1],
                                 newState[3][1][0])

    newState[3][1][1], \
    newState[3][1][2], \
    newState[3][2][2], \
    newState[3][2][1] = circle4F(newState[3][1][1],
                                 newState[3][1][2],
                                 newState[3][2][2],
                                 newState[3][2][1])

    return newState


# for line in L1L(test):
#     for line1 in line:
#         print(line1)


def L2R(state):
    newState = L1R(state)

    newState[0][2][0], \
    newState[4][2][0], \
    newState[5][2][0], \
    newState[2][2][0] = circle4B(newState[0][2][0],
                                 newState[4][2][0],
                                 newState[5][2][0],
                                 newState[2][2][0])
    newState[0][2][1], \
    newState[4][2][1], \
    newState[5][2][1], \
    newState[2][2][1] = circle4B(newState[0][2][1],
                                 newState[4][2][1],
                                 newState[5][2][1],
                                 newState[2][2][1])

    newState[0][2][2], \
    newState[4][2][2], \
    newState[5][2][2], \
    newState[2][2][2] = circle4B(newState[0][2][2],
                                 newState[4][2][2],
                                 newState[5][2][2],
                                 newState[2][2][2])

    newState[0][2][3], \
    newState[4][2][3], \
    newState[5][2][3], \
    newState[2][2][3] = circle4B(newState[0][2][3],
                                 newState[4][2][3],
                                 newState[5][2][3],
                                 newState[2][2][3])

    return newState


# for line in L2R(test):
#     for line1 in line:
#         print(line1)


def L2L(state):
    newState = L1L(state)

    newState[0][2][0], \
    newState[4][2][0], \
    newState[5][2][0], \
    newState[2][2][0] = circle4F(newState[0][2][0],
                                 newState[4][2][0],
                                 newState[5][2][0],
                                 newState[2][2][0])
    newState[0][2][1], \
    newState[4][2][1], \
    newState[5][2][1], \
    newState[2][2][1] = circle4F(newState[0][2][1],
                                 newState[4][2][1],
                                 newState[5][2][1],
                                 newState[2][2][1])

    newState[0][2][2], \
    newState[4][2][2], \
    newState[5][2][2], \
    newState[2][2][2] = circle4F(newState[0][2][2],
                                 newState[4][2][2],
                                 newState[5][2][2],
                                 newState[2][2][2])

    newState[0][2][3], \
    newState[4][2][3], \
    newState[5][2][3], \
    newState[2][2][3] = circle4F(newState[0][2][3],
                                 newState[4][2][3],
                                 newState[5][2][3],
                                 newState[2][2][3])

    return newState


# for line in L2L(test):
#     for line1 in line:
#         print(line1)


def L3R(state):
    newState = L2R(state)

    newState[0][1][0], \
    newState[4][1][0], \
    newState[5][1][0], \
    newState[2][1][0] = circle4B(newState[0][1][0],
                                 newState[4][1][0],
                                 newState[5][1][0],
                                 newState[2][1][0])
    newState[0][1][1], \
    newState[4][1][1], \
    newState[5][1][1], \
    newState[2][1][1] = circle4B(newState[0][1][1],
                                 newState[4][1][1],
                                 newState[5][1][1],
                                 newState[2][1][1])

    newState[0][1][2], \
    newState[4][1][2], \
    newState[5][1][2], \
    newState[2][1][2] = circle4B(newState[0][1][2],
                                 newState[4][1][2],
                                 newState[5][1][2],
                                 newState[2][1][2])

    newState[0][1][3], \
    newState[4][1][3], \
    newState[5][1][3], \
    newState[2][1][3] = circle4B(newState[0][1][3],
                                 newState[4][1][3],
                                 newState[5][1][3],
                                 newState[2][1][3])

    return newState


# for line in L3R(test):
#     for line1 in line:
#         print(line1)


def L3L(state):
    newState = L2L(state)

    newState[0][1][0], \
    newState[4][1][0], \
    newState[5][1][0], \
    newState[2][1][0] = circle4F(newState[0][1][0],
                                 newState[4][1][0],
                                 newState[5][1][0],
                                 newState[2][1][0])
    newState[0][1][1], \
    newState[4][1][1], \
    newState[5][1][1], \
    newState[2][1][1] = circle4F(newState[0][1][1],
                                 newState[4][1][1],
                                 newState[5][1][1],
                                 newState[2][1][1])

    newState[0][1][2], \
    newState[4][1][2], \
    newState[5][1][2], \
    newState[2][1][2] = circle4F(newState[0][1][2],
                                 newState[4][1][2],
                                 newState[5][1][2],
                                 newState[2][1][2])

    newState[0][1][3], \
    newState[4][1][3], \
    newState[5][1][3], \
    newState[2][1][3] = circle4F(newState[0][1][3],
                                 newState[4][1][3],
                                 newState[5][1][3],
                                 newState[2][1][3])

    return newState


# for line in L3L(test):
#     for line1 in line:
#         print(line1)

def L4R(state):
    newState = deepcopy(state)
    newState[0][0][0], \
    newState[4][0][0], \
    newState[5][0][0], \
    newState[2][0][0] = circle4B(newState[0][0][0],
                                 newState[4][0][0],
                                 newState[5][0][0],
                                 newState[2][0][0])
    newState[0][0][1], \
    newState[4][0][1], \
    newState[5][0][1], \
    newState[2][0][1] = circle4B(newState[0][0][1],
                                 newState[4][0][1],
                                 newState[5][0][1],
                                 newState[2][0][1])
    newState[0][0][2], \
    newState[4][0][2], \
    newState[5][0][2], \
    newState[2][0][2] = circle4B(newState[0][0][2],
                                 newState[4][0][2],
                                 newState[5][0][2],
                                 newState[2][0][2])

    newState[0][0][3], \
    newState[4][0][3], \
    newState[5][0][3], \
    newState[2][0][3] = circle4B(newState[0][0][3],
                                 newState[4][0][3],
                                 newState[5][0][3],
                                 newState[2][0][3])

    newState[1][0][3], \
    newState[1][3][3], \
    newState[1][3][0], \
    newState[1][0][0] = circle4F(newState[1][0][3],
                                 newState[1][3][3],
                                 newState[1][3][0],
                                 newState[1][0][0])
    newState[1][0][1], \
    newState[1][1][3], \
    newState[1][3][2], \
    newState[1][2][0] = circle4F(newState[1][0][1],
                                 newState[1][1][3],
                                 newState[1][3][2],
                                 newState[1][2][0])
    newState[1][0][2], \
    newState[1][2][3], \
    newState[1][3][1], \
    newState[1][1][0] = circle4F(newState[1][0][2],
                                 newState[1][2][3],
                                 newState[1][3][1],
                                 newState[1][1][0])

    newState[1][1][1], \
    newState[1][1][2], \
    newState[1][2][2], \
    newState[1][2][1] = circle4F(newState[1][1][1],
                                 newState[1][1][2],
                                 newState[1][2][2],
                                 newState[1][2][1])

    return newState


# for line in L4R(test):
#     for line1 in line:
#         print(line1)


def L4L(state):
    newState = deepcopy(state)
    newState[0][0][0], \
    newState[4][0][0], \
    newState[5][0][0], \
    newState[2][0][0] = circle4F(newState[0][0][0],
                                 newState[4][0][0],
                                 newState[5][0][0],
                                 newState[2][0][0])
    newState[0][0][1], \
    newState[4][0][1], \
    newState[5][0][1], \
    newState[2][0][1] = circle4F(newState[0][0][1],
                                 newState[4][0][1],
                                 newState[5][0][1],
                                 newState[2][0][1])
    newState[0][0][2], \
    newState[4][0][2], \
    newState[5][0][2], \
    newState[2][0][2] = circle4F(newState[0][0][2],
                                 newState[4][0][2],
                                 newState[5][0][2],
                                 newState[2][0][2])

    newState[0][0][3], \
    newState[4][0][3], \
    newState[5][0][3], \
    newState[2][0][3] = circle4F(newState[0][0][3],
                                 newState[4][0][3],
                                 newState[5][0][3],
                                 newState[2][0][3])

    newState[1][0][3], \
    newState[1][3][3], \
    newState[1][3][0], \
    newState[1][0][0] = circle4B(newState[1][0][3],
                                 newState[1][3][3],
                                 newState[1][3][0],
                                 newState[1][0][0])
    newState[1][0][1], \
    newState[1][1][3], \
    newState[1][3][2], \
    newState[1][2][0] = circle4B(newState[1][0][1],
                                 newState[1][1][3],
                                 newState[1][3][2],
                                 newState[1][2][0])
    newState[1][0][2], \
    newState[1][2][3], \
    newState[1][3][1], \
    newState[1][1][0] = circle4B(newState[1][0][2],
                                 newState[1][2][3],
                                 newState[1][3][1],
                                 newState[1][1][0])

    newState[1][1][1], \
    newState[1][1][2], \
    newState[1][2][2], \
    newState[1][2][1] = circle4B(newState[1][1][1],
                                 newState[1][1][2],
                                 newState[1][2][2],
                                 newState[1][2][1])

    return newState


# for line in L4L(test):
#     for line1 in line:
#         print(line1)


def RotateR(state):
    temp = L3R(state)
    newState = L4R(temp)
    return newState


# for line in RotateR(test):
#     for line1 in line:
#         print(line1)


def RotateL(state):
    temp = L3L(state)
    newState = L4L(temp)
    return newState


# for line in RotateL(test):
#     for line1 in line:
#         print(line1)


def FlipForward(state):
    newState = deepcopy(state)
    newState[0][0][0], \
    newState[1][0][0], \
    newState[5][3][3], \
    newState[3][0][0] = circle4F(newState[0][0][0],
                                 newState[1][0][0],
                                 newState[5][3][3],
                                 newState[3][0][0])
    newState[0][0][1], \
    newState[1][0][1], \
    newState[5][3][2], \
    newState[3][0][1] = circle4F(newState[0][0][1],
                                 newState[1][0][1],
                                 newState[5][3][2],
                                 newState[3][0][1])
    newState[0][0][2], \
    newState[1][0][2], \
    newState[5][3][1], \
    newState[3][0][2] = circle4F(newState[0][0][2],
                                 newState[1][0][2],
                                 newState[5][3][1],
                                 newState[3][0][2])

    newState[0][0][3], \
    newState[1][0][3], \
    newState[5][3][0], \
    newState[3][0][3] = circle4F(newState[0][0][3],
                                 newState[1][0][3],
                                 newState[5][3][0],
                                 newState[3][0][3])

    newState[0][1][0], \
    newState[1][1][0], \
    newState[5][2][3], \
    newState[3][1][0] = circle4F(newState[0][1][0],
                                 newState[1][1][0],
                                 newState[5][2][3],
                                 newState[3][1][0])
    newState[0][1][1], \
    newState[1][1][1], \
    newState[5][2][2], \
    newState[3][1][1] = circle4F(newState[0][1][1],
                                 newState[1][1][1],
                                 newState[5][2][2],
                                 newState[3][1][1])
    newState[0][1][2], \
    newState[1][1][2], \
    newState[5][2][1], \
    newState[3][1][2] = circle4F(newState[0][1][2],
                                 newState[1][1][2],
                                 newState[5][2][1],
                                 newState[3][1][2])

    newState[0][1][3], \
    newState[1][1][3], \
    newState[5][2][0], \
    newState[3][1][3] = circle4F(newState[0][1][3],
                                 newState[1][1][3],
                                 newState[5][2][0],
                                 newState[3][1][3])

    newState[0][2][0], \
    newState[1][2][0], \
    newState[5][1][3], \
    newState[3][2][0] = circle4F(newState[0][2][0],
                                 newState[1][2][0],
                                 newState[5][1][3],
                                 newState[3][2][0])
    newState[0][2][1], \
    newState[1][2][1], \
    newState[5][1][2], \
    newState[3][2][1] = circle4F(newState[0][2][1],
                                 newState[1][2][1],
                                 newState[5][1][2],
                                 newState[3][2][1])
    newState[0][2][2], \
    newState[1][2][2], \
    newState[5][1][1], \
    newState[3][2][2] = circle4F(newState[0][2][2],
                                 newState[1][2][2],
                                 newState[5][1][1],
                                 newState[3][2][2])

    newState[0][2][3], \
    newState[1][2][3], \
    newState[5][1][0], \
    newState[3][2][3] = circle4F(newState[0][2][3],
                                 newState[1][2][3],
                                 newState[5][1][0],
                                 newState[3][2][3])

    newState[0][3][0], \
    newState[1][3][0], \
    newState[5][0][3], \
    newState[3][3][0] = circle4F(newState[0][3][0],
                                 newState[1][3][0],
                                 newState[5][0][3],
                                 newState[3][3][0])

    newState[0][3][1], \
    newState[1][3][1], \
    newState[5][0][2], \
    newState[3][3][1] = circle4F(newState[0][3][1],
                                 newState[1][3][1],
                                 newState[5][0][2],
                                 newState[3][3][1])

    newState[0][3][2], \
    newState[1][3][2], \
    newState[5][0][1], \
    newState[3][3][2] = circle4F(newState[0][3][2],
                                 newState[1][3][2],
                                 newState[5][0][1],
                                 newState[3][3][2])

    newState[0][3][3], \
    newState[1][3][3], \
    newState[5][0][0], \
    newState[3][3][3] = circle4F(newState[0][3][3],
                                 newState[1][3][3],
                                 newState[5][0][0],
                                 newState[3][3][3])

    newState[2][0][0], \
    newState[2][0][3], \
    newState[2][3][3], \
    newState[2][3][0] = circle4B(newState[2][0][0],
                                 newState[2][0][3],
                                 newState[2][3][3],
                                 newState[2][3][0])
    newState[2][0][1], \
    newState[2][1][3], \
    newState[2][3][2], \
    newState[2][2][0] = circle4B(newState[2][0][1],
                                 newState[2][1][3],
                                 newState[2][3][2],
                                 newState[2][2][0])

    newState[2][0][2], \
    newState[2][2][3], \
    newState[2][3][1], \
    newState[2][1][0] = circle4B(newState[2][0][2],
                                 newState[2][2][3],
                                 newState[2][3][1],
                                 newState[2][1][0])

    newState[2][1][1], \
    newState[2][1][2], \
    newState[2][2][2], \
    newState[2][2][1] = circle4B(newState[2][1][1],
                                 newState[2][1][2],
                                 newState[2][2][2],
                                 newState[2][2][1])

    newState[4][0][0], \
    newState[4][0][3], \
    newState[4][3][3], \
    newState[4][3][0] = circle4F(newState[4][0][0],
                                 newState[4][0][3],
                                 newState[4][3][3],
                                 newState[4][3][0])
    newState[4][0][1], \
    newState[4][1][3], \
    newState[4][3][2], \
    newState[4][2][0] = circle4F(newState[4][0][1],
                                 newState[4][1][3],
                                 newState[4][3][2],
                                 newState[4][2][0])

    newState[4][0][2], \
    newState[4][2][3], \
    newState[4][3][1], \
    newState[4][1][0] = circle4F(newState[4][0][2],
                                 newState[4][2][3],
                                 newState[4][3][1],
                                 newState[4][1][0])

    newState[4][1][1], \
    newState[4][1][2], \
    newState[4][2][2], \
    newState[4][2][1] = circle4F(newState[4][1][1],
                                 newState[4][1][2],
                                 newState[4][2][2],
                                 newState[4][2][1])
    return newState


# for line in FlipForward(test):
#     for line1 in line:
#         print(line1)


def FlipBackward(state):
    newState = deepcopy(state)
    newState[0][0][0], \
    newState[1][0][0], \
    newState[5][3][3], \
    newState[3][0][0] = circle4B(newState[0][0][0],
                                 newState[1][0][0],
                                 newState[5][3][3],
                                 newState[3][0][0])
    newState[0][0][1], \
    newState[1][0][1], \
    newState[5][3][2], \
    newState[3][0][1] = circle4B(newState[0][0][1],
                                 newState[1][0][1],
                                 newState[5][3][2],
                                 newState[3][0][1])
    newState[0][0][2], \
    newState[1][0][2], \
    newState[5][3][1], \
    newState[3][0][2] = circle4B(newState[0][0][2],
                                 newState[1][0][2],
                                 newState[5][3][1],
                                 newState[3][0][2])

    newState[0][0][3], \
    newState[1][0][3], \
    newState[5][3][0], \
    newState[3][0][3] = circle4B(newState[0][0][3],
                                 newState[1][0][3],
                                 newState[5][3][0],
                                 newState[3][0][3])

    newState[0][1][0], \
    newState[1][1][0], \
    newState[5][2][3], \
    newState[3][1][0] = circle4B(newState[0][1][0],
                                 newState[1][1][0],
                                 newState[5][2][3],
                                 newState[3][1][0])
    newState[0][1][1], \
    newState[1][1][1], \
    newState[5][2][2], \
    newState[3][1][1] = circle4B(newState[0][1][1],
                                 newState[1][1][1],
                                 newState[5][2][2],
                                 newState[3][1][1])
    newState[0][1][2], \
    newState[1][1][2], \
    newState[5][2][1], \
    newState[3][1][2] = circle4B(newState[0][1][2],
                                 newState[1][1][2],
                                 newState[5][2][1],
                                 newState[3][1][2])

    newState[0][1][3], \
    newState[1][1][3], \
    newState[5][2][0], \
    newState[3][1][3] = circle4B(newState[0][1][3],
                                 newState[1][1][3],
                                 newState[5][2][0],
                                 newState[3][1][3])

    newState[0][2][0], \
    newState[1][2][0], \
    newState[5][1][3], \
    newState[3][2][0] = circle4B(newState[0][2][0],
                                 newState[1][2][0],
                                 newState[5][1][3],
                                 newState[3][2][0])
    newState[0][2][1], \
    newState[1][2][1], \
    newState[5][1][2], \
    newState[3][2][1] = circle4B(newState[0][2][1],
                                 newState[1][2][1],
                                 newState[5][1][2],
                                 newState[3][2][1])
    newState[0][2][2], \
    newState[1][2][2], \
    newState[5][1][1], \
    newState[3][2][2] = circle4B(newState[0][2][2],
                                 newState[1][2][2],
                                 newState[5][1][1],
                                 newState[3][2][2])

    newState[0][2][3], \
    newState[1][2][3], \
    newState[5][1][0], \
    newState[3][2][3] = circle4B(newState[0][2][3],
                                 newState[1][2][3],
                                 newState[5][1][0],
                                 newState[3][2][3])

    newState[0][3][0], \
    newState[1][3][0], \
    newState[5][0][3], \
    newState[3][3][0] = circle4B(newState[0][3][0],
                                 newState[1][3][0],
                                 newState[5][0][3],
                                 newState[3][3][0])

    newState[0][3][1], \
    newState[1][3][1], \
    newState[5][0][2], \
    newState[3][3][1] = circle4B(newState[0][3][1],
                                 newState[1][3][1],
                                 newState[5][0][2],
                                 newState[3][3][1])

    newState[0][3][2], \
    newState[1][3][2], \
    newState[5][0][1], \
    newState[3][3][2] = circle4B(newState[0][3][2],
                                 newState[1][3][2],
                                 newState[5][0][1],
                                 newState[3][3][2])

    newState[0][3][3], \
    newState[1][3][3], \
    newState[5][0][0], \
    newState[3][3][3] = circle4B(newState[0][3][3],
                                 newState[1][3][3],
                                 newState[5][0][0],
                                 newState[3][3][3])

    newState[2][0][0], \
    newState[2][0][3], \
    newState[2][3][3], \
    newState[2][3][0] = circle4F(newState[2][0][0],
                                 newState[2][0][3],
                                 newState[2][3][3],
                                 newState[2][3][0])
    newState[2][0][1], \
    newState[2][1][3], \
    newState[2][3][2], \
    newState[2][2][0] = circle4F(newState[2][0][1],
                                 newState[2][1][3],
                                 newState[2][3][2],
                                 newState[2][2][0])

    newState[2][0][2], \
    newState[2][2][3], \
    newState[2][3][1], \
    newState[2][1][0] = circle4F(newState[2][0][2],
                                 newState[2][2][3],
                                 newState[2][3][1],
                                 newState[2][1][0])

    newState[2][1][1], \
    newState[2][1][2], \
    newState[2][2][2], \
    newState[2][2][1] = circle4F(newState[2][1][1],
                                 newState[2][1][2],
                                 newState[2][2][2],
                                 newState[2][2][1])

    newState[4][0][0], \
    newState[4][0][3], \
    newState[4][3][3], \
    newState[4][3][0] = circle4B(newState[4][0][0],
                                 newState[4][0][3],
                                 newState[4][3][3],
                                 newState[4][3][0])
    newState[4][0][1], \
    newState[4][1][3], \
    newState[4][3][2], \
    newState[4][2][0] = circle4B(newState[4][0][1],
                                 newState[4][1][3],
                                 newState[4][3][2],
                                 newState[4][2][0])

    newState[4][0][2], \
    newState[4][2][3], \
    newState[4][3][1], \
    newState[4][1][0] = circle4B(newState[4][0][2],
                                 newState[4][2][3],
                                 newState[4][3][1],
                                 newState[4][1][0])

    newState[4][1][1], \
    newState[4][1][2], \
    newState[4][2][2], \
    newState[4][2][1] = circle4B(newState[4][1][1],
                                 newState[4][1][2],
                                 newState[4][2][2],
                                 newState[4][2][1])
    return newState


# for line in FlipBackward(test):
#     for line1 in line:
#         print(line1)

def FlipRight(state):
    newState = deepcopy(state)
    newState[1][0][0], \
    newState[2][3][0], \
    newState[3][3][3], \
    newState[4][0][3] = circle4F(newState[1][0][0],
                                 newState[2][3][0],
                                 newState[3][3][3],
                                 newState[4][0][3])
    newState[1][0][1], \
    newState[2][2][0], \
    newState[3][3][2], \
    newState[4][1][3] = circle4F(newState[1][0][1],
                                 newState[2][2][0],
                                 newState[3][3][2],
                                 newState[4][1][3])
    newState[1][0][2], \
    newState[2][1][0], \
    newState[3][3][1], \
    newState[4][2][3] = circle4F(newState[1][0][2],
                                 newState[2][1][0],
                                 newState[3][3][1],
                                 newState[4][2][3])

    newState[1][0][3], \
    newState[2][0][0], \
    newState[3][3][0], \
    newState[4][3][3] = circle4F(newState[1][0][3],
                                 newState[2][0][0],
                                 newState[3][3][0],
                                 newState[4][3][3])
    newState[1][1][0], \
    newState[2][3][1], \
    newState[3][2][3], \
    newState[4][0][2] = circle4F(newState[1][1][0],
                                 newState[2][3][1],
                                 newState[3][2][3],
                                 newState[4][0][2])
    newState[1][1][1], \
    newState[2][2][1], \
    newState[3][2][2], \
    newState[4][1][2] = circle4F(newState[1][1][1],
                                 newState[2][2][1],
                                 newState[3][2][2],
                                 newState[4][1][2])
    newState[1][1][2], \
    newState[2][1][1], \
    newState[3][2][1], \
    newState[4][2][2] = circle4F(newState[1][1][2],
                                 newState[2][1][1],
                                 newState[3][2][1],
                                 newState[4][2][2])

    newState[1][1][3], \
    newState[2][0][1], \
    newState[3][2][0], \
    newState[4][3][2] = circle4F(newState[1][1][3],
                                 newState[2][0][1],
                                 newState[3][2][0],
                                 newState[4][3][2])

    newState[1][2][0], \
    newState[2][3][2], \
    newState[3][1][3], \
    newState[4][0][1] = circle4F(newState[1][2][0],
                                 newState[2][3][2],
                                 newState[3][1][3],
                                 newState[4][0][1])
    newState[1][2][1], \
    newState[2][2][2], \
    newState[3][1][2], \
    newState[4][1][1] = circle4F(newState[1][2][1],
                                 newState[2][2][2],
                                 newState[3][1][2],
                                 newState[4][1][1])
    newState[1][2][2], \
    newState[2][1][2], \
    newState[3][1][1], \
    newState[4][2][1] = circle4F(newState[1][2][2],
                                 newState[2][1][2],
                                 newState[3][1][1],
                                 newState[4][2][1])

    newState[1][2][3], \
    newState[2][0][2], \
    newState[3][1][0], \
    newState[4][3][1] = circle4F(newState[1][2][3],
                                 newState[2][0][2],
                                 newState[3][1][0],
                                 newState[4][3][1])

    newState[1][3][0], \
    newState[2][3][3], \
    newState[3][0][3], \
    newState[4][0][0] = circle4F(newState[1][3][0],
                                 newState[2][3][3],
                                 newState[3][0][3],
                                 newState[4][0][0])

    newState[1][3][1], \
    newState[2][2][3], \
    newState[3][0][2], \
    newState[4][1][0] = circle4F(newState[1][3][1],
                                 newState[2][2][3],
                                 newState[3][0][2],
                                 newState[4][1][0])
    newState[1][3][2], \
    newState[2][1][3], \
    newState[3][0][1], \
    newState[4][2][0] = circle4F(newState[1][3][2],
                                 newState[2][1][3],
                                 newState[3][0][1],
                                 newState[4][2][0])

    newState[1][3][3], \
    newState[2][0][3], \
    newState[3][0][0], \
    newState[4][3][0] = circle4F(newState[1][3][3],
                                 newState[2][0][3],
                                 newState[3][0][0],
                                 newState[4][3][0])

    newState[0][0][0], \
    newState[0][0][3], \
    newState[0][3][3], \
    newState[0][3][0] = circle4B(newState[0][0][0],
                                 newState[0][0][3],
                                 newState[0][3][3],
                                 newState[0][3][0])
    newState[0][0][1], \
    newState[0][1][3], \
    newState[0][3][2], \
    newState[0][2][0] = circle4B(newState[0][0][1],
                                 newState[0][1][3],
                                 newState[0][3][2],
                                 newState[0][2][0])

    newState[0][0][2], \
    newState[0][2][3], \
    newState[0][3][1], \
    newState[0][1][0] = circle4B(newState[0][0][2],
                                 newState[0][2][3],
                                 newState[0][3][1],
                                 newState[0][1][0])

    newState[0][1][1], \
    newState[0][1][2], \
    newState[0][2][2], \
    newState[0][2][1] = circle4B(newState[0][1][1],
                                 newState[0][1][2],
                                 newState[0][2][2],
                                 newState[0][2][1])

    newState[5][0][0], \
    newState[5][0][3], \
    newState[5][3][3], \
    newState[5][3][0] = circle4F(newState[5][0][0],
                                 newState[5][0][3],
                                 newState[5][3][3],
                                 newState[5][3][0])
    newState[5][0][1], \
    newState[5][1][3], \
    newState[5][3][2], \
    newState[5][2][0] = circle4F(newState[5][0][1],
                                 newState[5][1][3],
                                 newState[5][3][2],
                                 newState[5][2][0])

    newState[5][0][2], \
    newState[5][2][3], \
    newState[5][3][1], \
    newState[5][1][0] = circle4F(newState[5][0][2],
                                 newState[5][2][3],
                                 newState[5][3][1],
                                 newState[5][1][0])

    newState[5][1][1], \
    newState[5][1][2], \
    newState[5][2][2], \
    newState[5][2][1] = circle4F(newState[5][1][1],
                                 newState[5][1][2],
                                 newState[5][2][2],
                                 newState[5][2][1])

    return newState


# for line in FlipRight(test):
#     for line1 in line:
#         print(line1)

def FlipLeft(state):
    newState = deepcopy(state)
    newState[1][0][0], \
    newState[2][3][0], \
    newState[3][3][3], \
    newState[4][0][3] = circle4B(newState[1][0][0],
                                 newState[2][3][0],
                                 newState[3][3][3],
                                 newState[4][0][3])
    newState[1][0][1], \
    newState[2][2][0], \
    newState[3][3][2], \
    newState[4][1][3] = circle4B(newState[1][0][1],
                                 newState[2][2][0],
                                 newState[3][3][2],
                                 newState[4][1][3])
    newState[1][0][2], \
    newState[2][1][0], \
    newState[3][3][1], \
    newState[4][2][3] = circle4B(newState[1][0][2],
                                 newState[2][1][0],
                                 newState[3][3][1],
                                 newState[4][2][3])

    newState[1][0][3], \
    newState[2][0][0], \
    newState[3][3][0], \
    newState[4][3][3] = circle4B(newState[1][0][3],
                                 newState[2][0][0],
                                 newState[3][3][0],
                                 newState[4][3][3])
    newState[1][1][0], \
    newState[2][3][1], \
    newState[3][2][3], \
    newState[4][0][2] = circle4B(newState[1][1][0],
                                 newState[2][3][1],
                                 newState[3][2][3],
                                 newState[4][0][2])
    newState[1][1][1], \
    newState[2][2][1], \
    newState[3][2][2], \
    newState[4][1][2] = circle4B(newState[1][1][1],
                                 newState[2][2][1],
                                 newState[3][2][2],
                                 newState[4][1][2])
    newState[1][1][2], \
    newState[2][1][1], \
    newState[3][2][1], \
    newState[4][2][2] = circle4B(newState[1][1][2],
                                 newState[2][1][1],
                                 newState[3][2][1],
                                 newState[4][2][2])

    newState[1][1][3], \
    newState[2][0][1], \
    newState[3][2][0], \
    newState[4][3][2] = circle4B(newState[1][1][3],
                                 newState[2][0][1],
                                 newState[3][2][0],
                                 newState[4][3][2])

    newState[1][2][0], \
    newState[2][3][2], \
    newState[3][1][3], \
    newState[4][0][1] = circle4B(newState[1][2][0],
                                 newState[2][3][2],
                                 newState[3][1][3],
                                 newState[4][0][1])
    newState[1][2][1], \
    newState[2][2][2], \
    newState[3][1][2], \
    newState[4][1][1] = circle4B(newState[1][2][1],
                                 newState[2][2][2],
                                 newState[3][1][2],
                                 newState[4][1][1])
    newState[1][2][2], \
    newState[2][1][2], \
    newState[3][1][1], \
    newState[4][2][1] = circle4B(newState[1][2][2],
                                 newState[2][1][2],
                                 newState[3][1][1],
                                 newState[4][2][1])

    newState[1][2][3], \
    newState[2][0][2], \
    newState[3][1][0], \
    newState[4][3][1] = circle4B(newState[1][2][3],
                                 newState[2][0][2],
                                 newState[3][1][0],
                                 newState[4][3][1])

    newState[1][3][0], \
    newState[2][3][3], \
    newState[3][0][3], \
    newState[4][0][0] = circle4B(newState[1][3][0],
                                 newState[2][3][3],
                                 newState[3][0][3],
                                 newState[4][0][0])

    newState[1][3][1], \
    newState[2][2][3], \
    newState[3][0][2], \
    newState[4][1][0] = circle4B(newState[1][3][1],
                                 newState[2][2][3],
                                 newState[3][0][2],
                                 newState[4][1][0])
    newState[1][3][2], \
    newState[2][1][3], \
    newState[3][0][1], \
    newState[4][2][0] = circle4B(newState[1][3][2],
                                 newState[2][1][3],
                                 newState[3][0][1],
                                 newState[4][2][0])

    newState[1][3][3], \
    newState[2][0][3], \
    newState[3][0][0], \
    newState[4][3][0] = circle4B(newState[1][3][3],
                                 newState[2][0][3],
                                 newState[3][0][0],
                                 newState[4][3][0])

    newState[0][0][0], \
    newState[0][0][3], \
    newState[0][3][3], \
    newState[0][3][0] = circle4F(newState[0][0][0],
                                 newState[0][0][3],
                                 newState[0][3][3],
                                 newState[0][3][0])
    newState[0][0][1], \
    newState[0][1][3], \
    newState[0][3][2], \
    newState[0][2][0] = circle4F(newState[0][0][1],
                                 newState[0][1][3],
                                 newState[0][3][2],
                                 newState[0][2][0])

    newState[0][0][2], \
    newState[0][2][3], \
    newState[0][3][1], \
    newState[0][1][0] = circle4F(newState[0][0][2],
                                 newState[0][2][3],
                                 newState[0][3][1],
                                 newState[0][1][0])

    newState[0][1][1], \
    newState[0][1][2], \
    newState[0][2][2], \
    newState[0][2][1] = circle4F(newState[0][1][1],
                                 newState[0][1][2],
                                 newState[0][2][2],
                                 newState[0][2][1])

    newState[5][0][0], \
    newState[5][0][3], \
    newState[5][3][3], \
    newState[5][3][0] = circle4B(newState[5][0][0],
                                 newState[5][0][3],
                                 newState[5][3][3],
                                 newState[5][3][0])
    newState[5][0][1], \
    newState[5][1][3], \
    newState[5][3][2], \
    newState[5][2][0] = circle4B(newState[5][0][1],
                                 newState[5][1][3],
                                 newState[5][3][2],
                                 newState[5][2][0])

    newState[5][0][2], \
    newState[5][2][3], \
    newState[5][3][1], \
    newState[5][1][0] = circle4B(newState[5][0][2],
                                 newState[5][2][3],
                                 newState[5][3][1],
                                 newState[5][1][0])

    newState[5][1][1], \
    newState[5][1][2], \
    newState[5][2][2], \
    newState[5][2][1] = circle4B(newState[5][1][1],
                                 newState[5][1][2],
                                 newState[5][2][2],
                                 newState[5][2][1])

    return newState


# for line in FlipLeft(test):
#     for line1 in line:
#         print(line1)
