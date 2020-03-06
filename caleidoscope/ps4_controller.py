import pygame
import collections


class FilteredValue:

    def __init__(self, value, size=10):
        self._size = float(size)
        self._values = collections.deque([value] * size, maxlen=size)
        self.value = value

    def _update(self):
        self.value = sum(self._values) / self._size

    def push_left(self):
        self._values.append(self._values[-1])
        self._update()

    def set(self, value):
        self._values.append(value)
        self._update()

    def __repr__(self):
        return "<FilteredValue({})>".format(self.value)


class FilteredPos:
    def __init__(self):
        self.x = FilteredValue(0)
        self.y = FilteredValue(0)

    def __repr__(self):
        return "<Pos(x={}, y={})>".format(self.x, self.y)



class PS4Controller:
    MOTION_THRESHOLD = 0.1


    def __init__(self, index):
        self.joystick_left = FilteredPos()
        self.joystick_right = FilteredPos()
        self.trigger_left = FilteredValue(0)
        self.trigger_right = FilteredValue(0)

        self._pg_gamepad = pygame.joystick.Joystick(index)
        self._pg_gamepad.init()

    def process(self, event):
        if event.type == pygame.JOYAXISMOTION and abs(event.value) > self.MOTION_THRESHOLD:
            # LEFT JOY X
            if event.axis == 0:
                self.joystick_left.x.set(event.value)
            else:
                self.joystick_left.x.push_left()

            # LEFT JOY Y
            if event.axis == 1:
                self.joystick_left.y.set(event.value)
            else:
                self.joystick_left.y.push_left()

            # RIGHT JOY X
            if event.axis == 2:
                self.joystick_right.x.set(event.value)
            else:
                self.joystick_right.x.push_left()

            # RIGHT JOY Y
            if event.axis == 3:
                self.joystick_right.y.set(event.value)
            else:
                self.joystick_right.y.push_left()

            # RIGHT TRIGGER
            if event.axis == 4:
                self.trigger_right.set((event.value + 1.0) / 2.0)
            else:
                self.trigger_right.push_left()

            # LEFT TRIGGER
            if event.axis == 5:
                self.trigger_left.set((event.value + 1.0) / 2.0)
            else:
                self.trigger_left.push_left()
