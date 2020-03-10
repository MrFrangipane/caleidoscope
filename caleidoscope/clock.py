import pygame


class Clock:

    def __init__(self):
        self.time = 0.0
        self._clock = pygame.time.Clock()

    def step(self):
        self.time += self._clock.get_time()
        self._clock.tick()
