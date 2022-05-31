import math

from shapes.segment_brezenhem import segment_brezenhem
import numpy as np


class NGon:
    def __init__(self, dots):
        self.matr = np.empty((len(dots), 3))
        for i in range(len(dots)):
            self.matr[i][0] = dots[i][0]
            self.matr[i][1] = dots[i][1]
            self.matr[i][2] = 1

    def to_pixels(self):
        for i in range(len(self.matr)):
            self.matr[i][0] /= self.matr[i][2]
            self.matr[i][1] /= self.matr[i][2]
        matr = self.matr.astype(int)
        output = segment_brezenhem(
            matr[0][0],
            matr[0][1],
            matr[len(matr) - 1][0],
            matr[len(matr) - 1][1]
        )
        for i in range(len(matr) - 1):
            output.extend(segment_brezenhem(
                matr[i][0],
                matr[i][1],
                matr[i + 1][0],
                matr[i + 1][1]
            ))
        return output

    # вспомогательное преобразование (перемножает матрицы)
    def abstacrt_trans(self, matr):
        self.matr = np.matmul(self.matr, matr)

    # тождественное преобразование
    def identical(self):
        m = np.array([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])
        self.abstacrt_trans(m)

    # локальное масштабирование
    def local_scale(self, xn, yn):
        m = np.array([
            [xn, 0, 0],
            [0, yn, 0],
            [0, 0, 1]
        ])
        self.abstacrt_trans(m)

    # симметрию относительно OX
    def symmetry_x(self):
        m = np.array([
            [1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ])
        self.abstacrt_trans(m)

    # симметрию относительно OY
    def symmetry_y(self):
        m = np.array([
            [-1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])
        self.abstacrt_trans(m)

    # симметрия относительная начала координат
    def symmetry_o(self):
        m = np.array([
            [-1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ])
        self.abstacrt_trans(m)

    # сдвиг вдоль оси OX пропорционально координате y
    def shift_x(self, s):
        m = np.array([
            [1, 0, 0],
            [0, 1, 0],
            [s, 0, 1]
        ])
        self.abstacrt_trans(m)

    # сдвиг вдоль оси OY пропорционально координате x
    def shift_y(self, s):
        m = np.array([
            [1, 0, 0],
            [0, 1, 0],
            [0, s, 1]
        ])
        self.abstacrt_trans(m)

    # сдвиг вдоль обоих осей
    def shift(self, sx, sy):
        m = np.array([
            [1, 0, 0],
            [0, 1, 0],
            [sx, sy, 1]
        ])
        self.abstacrt_trans(m)

    # вращение
    def rotation(self, angle):
        angle *= math.pi / 180
        m = np.array([
            [math.cos(angle), math.sin(angle), 0],
            [-math.sin(angle), math.cos(angle), 0],
            [0, 0, 1]
        ])
        self.abstacrt_trans(m)

    # вращение вокруг точки
    def rotation_around(self, angle, m, n):
        self.shift(-m, -n)
        self.rotation(angle)
        self.shift(m, n)

    # отражение относительно y = x
    def symmetry_main_diag(self):
        m = np.array([
            [0, 1, 0],
            [1, 0, 0],
            [0, 0, 1]
        ])
        self.abstacrt_trans(m)

    # отражение относительно y = -x
    def symmetry_aux_diag(self):
        m = np.array([
            [0, -1, 0],
            [-1, 0, 0],
            [0, 0, 1]
        ])
        self.abstacrt_trans(m)

    # общее (пропорциональное) масштабирование
    def common_scale(self, n):
        m = np.array([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, n]
        ])
        self.abstacrt_trans(m)

    # симметрия относительно произвольной точки
    def symmetry_dot(self, m, n):
        self.shift(-m, -n)
        self.symmetry_o()
        self.shift(m, n)

    # проецирование в однородных координатах
    def projection(self, p, q, h):
        m = np.array([
            [1, 0, p],
            [0, 1, q],
            [0, 0, h]
        ])
        self.abstacrt_trans(m)


# 1.	+ тождественное преобразование,
# 2.	+ локальное масштабирование,
# 3.	+ симметрию относительно осей координат,
# 4.	+ симметрию относительно начала координат,
# 5.	+ сдвиг вдоль оси ОХ пропорционально координате у,
# 6.	+ сдвиг вдоль оси ОУ пропорционально координате х,
# 7.	+ поворот на заданный угол вокруг начала системы координат,
# 8.	+ симметрию относительно прямых у=х и у=-х,
# 9.	+ перемещение (параллельный перенос) на заданный вектор,
# 10.	+ проецирование в однородных координатах,
# 11.	+ общее масштабирование.

# С помощью простейших преобразований реализовать
# 1.	+ поворот относительно произвольной точки и
# 2.	+ симметрию относительно произвольной прямой.
