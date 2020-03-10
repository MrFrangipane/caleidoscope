import pygame
from caleidoscope import draw
from caleidoscope import patterns
from caleidoscope.clock import Clock
from caleidoscope.ps4_controller import PS4Controller


SCREEN_SIZE = 1024, 1280
pygame.font.init()
FONT = pygame.font.SysFont('consolas', 16)

pygame.init()

background = pygame.image.load('image.gif')

screen = pygame.display.set_mode(SCREEN_SIZE)
clock = Clock()
gamepad = PS4Controller(0)
gamepad.MOTION_THRESHOLD = 0.01
stripes = patterns.Stripes()

show_debug = False

is_running = True
while is_running:
    clock.step()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            show_debug = not show_debug

        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            is_running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.display.set_mode(SCREEN_SIZE)

        gamepad.process_event(event)

    gamepad.compute_values()

    # DRAW
    screen.fill((0, 0, 0))
    stripes.draw(screen, gamepad, clock.time)

    if show_debug:
        lines = (
            "LEFT",
            "t: {}".format(gamepad.trigger_left.value),
            "x: {}".format(gamepad.joystick_left.x.value),
            "y: {}".format(gamepad.joystick_left.y.value),
            "a: {}".format(gamepad.joystick_left.angle)
        )
        for i, line in enumerate(lines):
            text = FONT.render(
                line,
                True,
                (150, 150, 150)
            )
            screen.blit(text, (100, 500 + i * 24))

    pygame.display.flip()
