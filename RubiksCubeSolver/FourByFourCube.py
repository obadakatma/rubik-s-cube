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
    [[Color.BLUE, Color.GREEN, Color.WHITE, Color.ORANGE],
     [Color.YELLOW, Color.GREEN, Color.RED, Color.WHITE],
     [Color.ORANGE, Color.BLUE, Color.RED, Color.YELLOW],
     [Color.BLUE, Color.YELLOW, Color.GREEN, Color.WHITE]],
    [[Color.YELLOW, Color.ORANGE, Color.YELLOW, Color.YELLOW],
     [Color.BLUE, Color.RED, Color.YELLOW, Color.ORANGE],
     [Color.YELLOW, Color.WHITE, Color.ORANGE, Color.WHITE],
     [Color.YELLOW, Color.ORANGE, Color.BLUE, Color.WHITE]],
    [[Color.ORANGE, Color.RED, Color.GREEN, Color.ORANGE],
     [Color.ORANGE, Color.ORANGE, Color.YELLOW, Color.RED],
     [Color.YELLOW, Color.WHITE, Color.WHITE, Color.BLUE],
     [Color.BLUE, Color.ORANGE, Color.WHITE, Color.RED]],
    [[Color.YELLOW, Color.ORANGE, Color.RED, Color.RED],
     [Color.RED, Color.GREEN, Color.BLUE, Color.BLUE],
     [Color.YELLOW, Color.YELLOW, Color.GREEN, Color.RED],
     [Color.WHITE, Color.BLUE, Color.RED, Color.RED]],
    [[Color.GREEN, Color.GREEN, Color.WHITE, Color.RED],
     [Color.GREEN, Color.ORANGE, Color.BLUE, Color.BLUE],
     [Color.BLUE, Color.ORANGE, Color.YELLOW, Color.GREEN],
     [Color.BLUE, Color.ORANGE, Color.YELLOW, Color.GREEN]],
    [[Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN],
     [Color.RED, Color.BLUE, Color.GREEN, Color.WHITE],
     [Color.RED, Color.ORANGE, Color.RED, Color.BLUE],
     [Color.WHITE, Color.WHITE, Color.WHITE, Color.ORANGE]]
]


def circle4F(w, h, x, y, z):
    temp = w
    w = h
    h = x
    x = y
    y = z
    z = temp
    return w, h, x, y, z


def circle4B(w, h, x, y, z):
    temp = z
    z = y
    y = x
    x = h
    h = w
    w = temp
    return w, h, x, y, z
