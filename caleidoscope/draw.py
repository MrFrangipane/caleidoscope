import math
import pygame


def _transform(x, y, position, angle):
    x_ = position[0] + math.cos(angle) * x - math.sin(angle) * y
    y_ = position[1] + math.sin(angle) * x - math.cos(angle) * y
    return x_, y_


def thick_line(surface, center, angle, thickness, color):
    x1, y1 = -2000, thickness / 2
    x2, y2 = 2000, thickness / 2
    x3, y3 = -2000, -thickness / 2
    x4, y4 = 2000, -thickness / 2

    x1, y1 = _transform(x1, y1, center, angle)
    x2, y2 = _transform(x2, y2, center, angle)
    x3, y3 = _transform(x3, y3, center, angle)
    x4, y4 = _transform(x4, y4, center, angle)

    pygame.draw.polygon(surface, color, [(x1, y1), (x2, y2), (x4, y4), (x3, y3)])
