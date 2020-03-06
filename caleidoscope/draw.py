import math
import pygame
from pygame import gfxdraw


_THICKLINE_WIDTH = 20
_DEG2RAD = math.pi / 180.0


def _transform(x, y, position, angle):
    x_ = position[0] + math.cos(angle) * x - math.sin(angle) * y
    y_ = position[1] + math.sin(angle) * x + math.cos(angle) * y
    return x_, y_


def thick_line(surface, center, thickness, angle, color):
    x1, y1 = -_THICKLINE_WIDTH, thickness / 2
    x2, y2 = _THICKLINE_WIDTH, thickness / 2
    x3, y3 = -_THICKLINE_WIDTH, -thickness / 2
    x4, y4 = _THICKLINE_WIDTH, -thickness / 2

    x1, y1 = _transform(x1, y1, center, angle)
    x2, y2 = _transform(x2, y2, center, angle)
    x3, y3 = _transform(x3, y3, center, angle)
    x4, y4 = _transform(x4, y4, center, angle)

    gfxdraw.aapolygon(surface, [(x1, y1), (x2, y2), (x4, y4), (x3, y3)], color)
    pygame.draw.polygon(surface, color, [(x1, y1), (x2, y2), (x4, y4), (x3, y3)])
