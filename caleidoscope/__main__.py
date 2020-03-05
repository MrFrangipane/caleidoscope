import pygame
from caleidoscope.ps4_controller import PS4Controller

RECT_SIZE = 60, 60


pygame.init()

screen = pygame.display.set_mode((320, 240))

gamepad = PS4Controller(0)
gamepad.MOTION_THRESHOLD = 0.01

is_running = True
while is_running:
    for event in pygame.event.get():

        # QUIT
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            is_running = False

        # FULLSCREEN
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.display.set_mode((1280, 1024))

        # PS4
        gamepad.react(event)

        x = ((gamepad.left_joystick.x / 2.0) + 0.5) * (1280 - RECT_SIZE[0])
        y = ((gamepad.left_joystick.y / 2.0) + 0.5) * (1024 - RECT_SIZE[1])

        # DRAW
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x, y, RECT_SIZE[0], RECT_SIZE[1]))

    pygame.display.flip()
