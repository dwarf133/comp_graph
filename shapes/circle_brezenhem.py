import math


def circle_brezenhem(x0, y0, r):
    x = 0
    y = r
    delta = 2 * (1 - r)
    output = []
    while y > int(r / math.sqrt(2)):
        output.extend(
            (i + x0, j + y0) for i, j in [(x, y), (y, x), (-x, y), (-y, x), (x, -y), (y, -x), (-x, -y), (-y, -x)])
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
