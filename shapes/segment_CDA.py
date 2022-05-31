import math
from helpful import sign


# какие есть варианты округлить:
#   отбрасывание дробной части (или к нулю) - int()
#   округление вниз - math.floor()
#   округление вверх - math.ceil()
#   округление математическое - round()

def rounder(roundType, num):
    if roundType == "math":
        return round(num)
    elif roundType == "floor":
        return math.floor(num)
    elif roundType == "ceil":
        return math.ceil(num)
    else:
        return int(num)  # int


def segment_CDA(x1, y1, x2, y2, roundType="int"):
    length = max(abs(x2 - x1), abs(y2 - y1))
    dx = (x2 - x1) / length
    dy = (y2 - y1) / length
    x = x1 + 0.5 * sign(dx)
    y = y1 + 0.5 * sign(dy)
    output = []
    for i in range(0, length):
        output.append((rounder(roundType, x), rounder(roundType, y)))
        x += dx
        y += dy
    return output
