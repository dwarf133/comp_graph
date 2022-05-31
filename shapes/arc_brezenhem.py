import math


def arc_brezenhem(x0, y0, r, angF, angS):
    if angF > angS:
        angF, angS = angS, angF
    angF *= math.pi / 180
    angS *= math.pi / 180
    x = int(r * math.cos(angS))
    y = int(r * math.sin(angS))
    delta = 2 * (1 - r)
    output = []
    while y >= int(r * math.sin(angF)):
        output.append((x + x0, y + y0))
        if delta < 0 and 2 * delta + 2 * y - 1 <= 0:
            x += 1
            delta += 2 * x - 1
        elif delta > 0 and 2 * delta - 2 * x - 1 > 0:
            y -= 1
            delta += 1 - 2 * y
        else:
            x += 1
            y -= 1
            delta += 2 * x - 2 * y + 2
    return output
