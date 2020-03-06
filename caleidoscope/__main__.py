import pygame
from caleidoscope import draw
from caleidoscope.ps4_controller import PS4Controller


SCREEN_SIZE = 1024, 1280
RECT_SIZE = 60, 60


pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)

gamepad = PS4Controller(0)
gamepad.MOTION_THRESHOLD = 0.01

is_running = True
while is_running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            is_running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.display.set_mode(SCREEN_SIZE)

        gamepad.process_event(event)

    gamepad.compute_values()

    x1 = ((gamepad.joystick_left.x.value / 2.0) + 0.5) * (SCREEN_SIZE[0] - RECT_SIZE[0])
    y1 = ((gamepad.joystick_left.y.value / 2.0) + 0.5) * (SCREEN_SIZE[1] - RECT_SIZE[1])

    x2 = ((gamepad.joystick_right.x.value / 2.0) + 0.5) * (SCREEN_SIZE[0] - RECT_SIZE[0])
    y2 = ((gamepad.joystick_right.y.value / 2.0) + 0.5) * (SCREEN_SIZE[1] - RECT_SIZE[1])

    center = x1, y1
    thickness = 50 + gamepad.trigger_left.value * 1280
    angle = gamepad.joystick_right.angle

    # DRAW
    screen.fill((0, 0, 0))

    draw.thick_line(
        surface=screen,
        center=(x2, y2),
        thickness= 50 + gamepad.trigger_right.value * 1280,
        angle=angle,
        color=(0, 255, 255)
    )

    draw.thick_line(
        surface=screen,
        center=center,
        thickness=thickness,
        angle=angle,
        color=(255, 255, 255)
    )

    pygame.display.flip()
