import math
import colorsys
from . import draw


class Stripes:
    BASE_SPEED = 0.33
    ACCEL_FACTOR = 2
    PHASE_MODULO = 2000.0
    SURFACE_SIZE = 1500
    SCREEN = 1280, 1024  # Do better
    MIN_LINE_COUNT = 1
    MAX_LINE_COUNT = 10

    def __init__(self):
        self.last_time = 0
        self.time = 0
        self.phase = 0

    def compute_phase(self, gamepad, time):
        self.time = time
        self.phase += (self.time - self.last_time) * (self.BASE_SPEED + gamepad.trigger_left.value * self.ACCEL_FACTOR)
        self.last_time = time

    def draw(self, surface, gamepad, time):
        self.compute_phase(gamepad, time)

        phase = ((self.phase % self.PHASE_MODULO) / self.PHASE_MODULO)
        line_count = int(self.MIN_LINE_COUNT + (gamepad.trigger_right.value * (self.MAX_LINE_COUNT - self.MIN_LINE_COUNT)))
        phases = [
            ((phase + float(offset) / line_count) % 1.0) - 0.5
            for offset in range(line_count)
        ]

        for i, phase_ in enumerate(phases):
            center = (
                self.SCREEN[1] / 2 + phase_ * self.SURFACE_SIZE * math.cos(gamepad.joystick_left.angle),
                self.SCREEN[0] / 2 + phase_ * self.SURFACE_SIZE * math.sin(gamepad.joystick_left.angle)
            )

            draw.thick_line(
                surface,
                center,
                self.SURFACE_SIZE,
                gamepad.joystick_left.angle,
                [int(c * 255) for c in colorsys.hsv_to_rgb(float(i) / len(phases), 1.0, 1.0)]
            )

