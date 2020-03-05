import pygame


class Pos:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __repr__(self):
        return "<Pos(x={}, y={})>".format(self.x, self.y)


class PS4Controller:
    MOTION_THRESHOLD = 0.1


    def __init__(self, index):
        self.left_joystick = Pos()
        self.right_joystick = Pos()
        self.left_trigger = 0
        self.right_trigger = 0

        self._pg_gamepad = pygame.joystick.Joystick(index)
        self._pg_gamepad.init()

    def react(self, event):
        if event.type == pygame.JOYAXISMOTION and abs(event.value) > self.MOTION_THRESHOLD:
            if event.axis == 0:
                self.left_joystick.x = event.value

            elif event.axis == 1:
                self.left_joystick.y = event.value

            else:
                pass
                #print(event.axis, event.value)
