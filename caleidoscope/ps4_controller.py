import math
import collections
import pygame


class FilteredValue:

    def __init__(self, value, size=30):
        self._size = float(size)
        self._values = collections.deque([value] * size, maxlen=size)
        self.value = value
        self.value_instantaneous = value

    def compute_value(self):
        self._values.append(self.value_instantaneous)
        self.value = sum(self._values) / self._size

    def __repr__(self):
        return "<FilteredValue({})>".format(self.value)


class FilteredPos:
    def __init__(self):
        self.x = FilteredValue(0)
        self.y = FilteredValue(0)
        self.angle = 0

    def compute_values(self):
        self.x.compute_value()
        self.y.compute_value()
        self.angle = math.atan2(self.y.value, self.x.value)

    def __repr__(self):
        return "<Pos(x={}, y={}, a={})>".format(
            self.x.value,
            self.y.value,
            self.angle
        )


class PS4Controller:
    MOTION_THRESHOLD = 0.1

    def __init__(self, index):
        self.joystick_left = FilteredPos()
        self.joystick_right = FilteredPos()
        self.trigger_left = FilteredValue(0)
        self.trigger_right = FilteredValue(0)

        self._pg_gamepad = pygame.joystick.Joystick(index)
        self._pg_gamepad.init()

    def compute_values(self):
        self.joystick_left.compute_values()
        self.joystick_right.compute_values()
        self.trigger_left.compute_value()
        self.trigger_right.compute_value()

    def process_event(self, event):
        if event.type == pygame.JOYAXISMOTION and abs(event.value) > self.MOTION_THRESHOLD:

            if event.axis == 0:
                self.joystick_left.x.value_instantaneous = event.value

            if event.axis == 1:
                self.joystick_left.y.value_instantaneous = event.value

            if event.axis == 2:
                self.joystick_right.x.value_instantaneous = event.value

            if event.axis == 3:
                self.joystick_right.y.value_instantaneous = event.value

            if event.axis == 4:
                self.trigger_right.value_instantaneous = max(0.0, (event.value + 1.0) / 2.0)

            if event.axis == 5:
                self.trigger_left.value_instantaneous = max(0.0 , (event.value + 1.0) / 2.0)
