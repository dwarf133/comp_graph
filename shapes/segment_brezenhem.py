from helpful import sign


def segment_brezenhem(x1, y1, x2, y2):
    x = x1
    y = y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = sign(x2 - x1)
    sy = sign(y2 - y1)
    swap = False
    if dy > dx:
        dx, dy = dy, dx
        swap = True
    output = []
    e = 2 * dy - dx
    for i in range(0, dx):
        output.append((x, y))
        if e >= 0:
            if swap:
                x += sx
            else:
                y += sy
            e -= 2 * dx
        if swap:
            y += sy
        else:
            x += sx
        e += 2 * dy
    return output
