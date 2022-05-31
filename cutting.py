from math import fabs as abs
from PIL import Image, ImageDraw
from drawing.canvas import canvas, shape
from shapes.rectangle import rectangle
from shapes.segment_brezenhem import segment_brezenhem

WIDTH = 81
HEIGHT = 81

def math_round(number):
    if number - int(number) > 0.5:
        return int(number + 1)
    else: return int(number)


def sign(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0


def to_normal_view(x, y):
    return x + WIDTH // 2, -1 * (y - HEIGHT // 2)


def wright_axes():
    dda(-1 * WIDTH // 2, 0, WIDTH // 2 + 1, 0, 'red')
    dda(0, -1 * HEIGHT // 2, 0, HEIGHT // 2 + 1, 'red')


x1, y1, x2, y2 = -3, -8, 25, 18
img = Image.new('RGB', (HEIGHT, WIDTH), 'white')
idDraw = ImageDraw.Draw(img)


def dda(x1, y1, x2, y2, color = 'black'):
    if abs(x2-x1) >= abs(y2-y1):
        length = abs(x2-x1)
    else:
        length = abs(y2-y1)
    length = int(length)
    dx = (x2 - x1) / length
    dy = (y2 - y1) / length
    x = x1 + 0.5 * sign(dx)
    y = y1 + 0.5 * sign(dy)
    for i in range(0, length):
        idDraw.point(to_normal_view(math_round(x), math_round(y)), fill=color)
        #print(math_round(x), math_round(y))
        #print(x, y)
        x += dx
        y += dy


def now_cutting(rectX1: int, rectY1: int, rectX2: int, rectY2: int, cutting: list) -> list:
    output = []
    for pixel in cutting:
        if rectX1 <= pixel[0] <= rectX2 and rectY1 <= pixel[1] <= rectY2:
            output.append(pixel)
    return output


def get_code(param, rect):
    pass


def is_visible(bar, rect):
    pass


def log_prod(code1, code2):
    p = 0
    for i in range(4):
        p += code1[i] & code2[i]

    return p


def is_visible(bar, rect):
    """Видимость - 0 = невидимый
                   1 = видимый
                   2 = частично видимый"""
    # вычисление кодов концевых точек отрезка
    s1 = sum(get_code(bar[0], rect))
    s2 = sum(get_code(bar[1], rect))

    # предположим, что отрезок частично видим
    vis = 2

    # проверка полной видимости отрезка
    if not s1 and not s2:
        vis = 1
    else:
        # проверка тривиальной невидимости отрезка
        l = log_prod(get_code(bar[0], rect), get_code(bar[1], rect))
        if l != 0:
            vis = 0

    return vis


def cohen_sutherland(bar, rect, win):
    # инициализация флага
    flag = 1  # общего положения
    t = 1

    # проверка вертикальности и горизонтальности отрезка
    if bar[1][0] - bar[0][0] == 0:
        flag = -1  # вертикальный отрезок
    else:
        # вычисление наклона
        t = (bar[1][1] - bar[0][1]) / (bar[1][0] - bar[0][0])
        if t == 0:
            flag = 0  # горизонтальный

    # для каждой стороны окна
    for i in range(4):
        vis = is_visible(bar, rect)
        if vis == 1:
            win.scene.addLine(bar[0][0], bar[0][1], bar[1][0], bar[1][1], win.pen)
            return
        elif not vis:
            return

        # проверка пересечения отрезка и стороны окна
        code1 = get_code(bar[0], rect)
        code2 = get_code(bar[1], rect)

        if code1[i] == code2[i]:
            continue

        # проверка нахождения Р1 вне окна; если Р1 внутри окна, то Р2 и Р1 поменять местами
        if not code1[i]:
            bar[0], bar[1] = bar[1], bar[0]

        # поиск пересечений отрезка со сторонами окна
        # контроль вертикальности отрезка
        if flag != -1:
            if i < 2:
                bar[0][1] = t * (rect[i] - bar[0][0]) + bar[0][1]
                bar[0][0] = rect[i]
                continue
            else:
                bar[0][0] = (1 / t) * (rect[i] - bar[0][1]) + bar[0][0]

        bar[0][1] = rect[i]
    win.scene.addLine(bar[0][0], bar[0][1], bar[1][0], bar[1][1], win.pen)

c = canvas()
rX1 = -3
rY1 = -8
rX2 = 25
rY2 = 18

lines = [segment_brezenhem(10, 3, 30, 40),
            segment_brezenhem(-5, 20, 20, -23),
            segment_brezenhem(10, 0, 18, 5),
            segment_brezenhem(6, 6, 2, 30)]

for line in lines:
    c.addObject(shape(line, "Black"))
    c.addObject(shape(now_cutting(rX1, rY1, rX2, rY2, line), "Red"))

c.addObject(shape(rectangle(rX1, rY1, rX2, rY2), "Blue"))
c.saveToFile("cutting.png")

