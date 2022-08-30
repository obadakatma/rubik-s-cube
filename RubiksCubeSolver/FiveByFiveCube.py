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
    [[Color.RED, Color.BLUE, Color.BLUE, Color.YELLOW, Color.GREEN],
     [Color.BLUE, Color.WHITE, Color.GREEN, Color.GREEN, Color.YELLOW],
     [Color.BLUE, Color.WHITE, Color.RED, Color.BLUE, Color.GREEN],
     [Color.RED, Color.WHITE, Color.BLUE, Color.BLUE, Color.YELLOW],
     [Color.WHITE, Color.WHITE, Color.ORANGE, Color.RED, Color.RED]],
    [[Color.WHITE, Color.WHITE, Color.WHITE, Color.ORANGE, Color.RED],
     [Color.WHITE, Color.GREEN, Color.RED, Color.WHITE, Color.BLUE],
     [Color.ORANGE, Color.ORANGE, Color.GREEN, Color.WHITE, Color.RED],
     [Color.ORANGE, Color.ORANGE, Color.BLUE, Color.BLUE, Color.RED],
     [Color.YELLOW, Color.YELLOW, Color.WHITE, Color.ORANGE, Color.ORANGE]],
    [[Color.ORANGE, Color.GREEN, Color.GREEN, Color.WHITE, Color.BLUE],
     [Color.YELLOW, Color.WHITE, Color.WHITE, Color.YELLOW, Color.RED],
     [Color.GREEN, Color.BLUE, Color.YELLOW, Color.ORANGE, Color.YELLOW],
     [Color.ORANGE, Color.BLUE, Color.YELLOW, Color.RED, Color.GREEN],
     [Color.ORANGE, Color.BLUE, Color.WHITE, Color.ORANGE, Color.RED]],
    [[Color.BLUE, Color.BLUE, Color.BLUE, Color.WHITE, Color.GREEN],
     [Color.GREEN, Color.GREEN, Color.YELLOW, Color.RED, Color.WHITE],
     [Color.ORANGE, Color.ORANGE, Color.BLUE, Color.YELLOW, Color.GREEN],
     [Color.YELLOW, Color.ORANGE, Color.GREEN, Color.YELLOW, Color.ORANGE],
     [Color.GREEN, Color.RED, Color.YELLOW, Color.BLUE, Color.ORANGE]],
    [[Color.WHITE, Color.GREEN, Color.BLUE, Color.ORANGE, Color.WHITE],
     [Color.GREEN, Color.GREEN, Color.ORANGE, Color.RED, Color.WHITE],
     [Color.YELLOW, Color.WHITE, Color.WHITE, Color.YELLOW, Color.YELLOW],
     [Color.GREEN, Color.YELLOW, Color.RED, Color.ORANGE, Color.ORANGE],
     [Color.YELLOW, Color.RED, Color.WHITE, Color.WHITE, Color.YELLOW]],
    [[Color.GREEN, Color.GREEN, Color.RED, Color.GREEN, Color.BLUE],
     [Color.BLUE, Color.ORANGE, Color.RED, Color.YELLOW, Color.RED],
     [Color.RED, Color.GREEN, Color.ORANGE, Color.GREEN, Color.RED],
     [Color.YELLOW, Color.RED, Color.RED, Color.BLUE, Color.BLUE],
     [Color.BLUE, Color.RED, Color.ORANGE, Color.YELLOW, Color.YELLOW]]
]


def circle4F(w, h, x, y, z, k):
    temp = w
    w = h
    h = x
    x = y
    y = z
    z = k
    k = temp
    return w, h, x, y, z, k


def circle4B(w, h, x, y, z, k):
    temp = k
    k = z
    z = y
    y = x
    x = h
    h = w
    w = temp
    return w, h, x, y, z, k

