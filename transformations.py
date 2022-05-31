from shapes.arc_brezenhem import arc_brezenhem
from drawing.canvas import canvas, shape
from shapes.segment_CDA import segment_CDA
from shapes.segment_brezenhem import segment_brezenhem
from shapes.circle_brezenhem import circle_brezenhem
from shapes.rectangle import rectangle
from drawing.colours import getNextColour
from helpful import clearPNGs
from shapes.ngon import NGon

def test_identical(dots):
    c = canvas()

    triag = NGon(dots)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    triag.identical()
    c.addObject(shape(triag.to_pixels(), getNextColour()))
    c.saveToFile("identical.png")


def test_local_scaling(dots):
    c = canvas()

    triag = NGon(dots)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    triag.local_scale(2, 5)
    c.addObject(shape(triag.to_pixels(), getNextColour()))
    c.saveToFile("local_scale.png")


def test_symmetry(dots):
    c = canvas()

    triag = NGon(dots)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    triag.symmetry_x()
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    triag.symmetry_y()
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    triag.symmetry_o()
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    c.saveToFile("symmetry.png")


def test_shift(dots):
    c = canvas()

    triag = NGon(dots)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    triag.shift_x(60)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    triag.shift_y(120)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    triag.shift(-60, -60)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    c.saveToFile("shift.png")


def test_rotation(dots):
    c = canvas()

    triag = NGon(dots)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    triag.rotation(-90)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    dot = (100, -30)
    triag.rotation_around(-90, dot[0], dot[1])
    c.addObject(shape(triag.to_pixels(), getNextColour()))
    c.addObject(shape([dot], getNextColour()))

    c.saveToFile("rotation.png")


def test_symmetry_diag(dots):
    c = canvas()

    triag = NGon(dots)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    triag.symmetry_main_diag()
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    triag.symmetry_aux_diag()
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    c.saveToFile("symmetry_diag.png")


def test_common_scaling(dots):
    c = canvas()

    triag = NGon(dots)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    triag.common_scale(2)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    c.saveToFile("common_scale.png")


def test_symmetry_dot(dots):
    c = canvas()

    triag = NGon(dots)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    dot = (30, 40)
    triag.symmetry_dot(dot[0], dot[1])
    c.addObject(shape(triag.to_pixels(), getNextColour()))
    c.addObject(shape([dot], getNextColour()))

    c.saveToFile("symmetry_dot.png")


def test_projection(dots):
    c = canvas()

    triag = NGon(dots)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    triag.projection(1/50, 1/24, 3)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    c.saveToFile("projection.png")

def test_transformations():
    dots = [(10, 15), (40, 60), (90, 5)]
    test_identical(dots)
    test_local_scaling(dots)
    test_symmetry(dots)
    test_shift(dots)
    test_rotation(dots)
    test_symmetry_diag(dots)
    test_common_scaling(dots)
    test_symmetry_dot(dots)
    test_projection(dots)


test_transformations()