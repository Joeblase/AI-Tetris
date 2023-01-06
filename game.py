import pygame as pg
from pygame.locals import *
import sys

from main import clock, display


class GameBox:
    def __init__(self):
        self.size = (259, 509)
        self.surface = pg.Surface(self.size)
        self.surface.fill((0, 0, 0))
        self.location = (20, 100)
        self.border_size = 8
        self.border = pg.Rect((self.location[0] - self.border_size//2, self.location[1] - self.border_size//2),
                              (self.size[0] + self.border_size, self.size[1] + self.border_size))

    def draw_game_box(self):
        pg.draw.rect(display, (180, 180, 180), self.border)
        display.blit(self.surface, self.location)


class Piece:
    def __init__(self, shape):
        self.rects = shape[0]
        self.color = shape[1]


def run():

    background = pg.image.load('data/background.png')
    game_box = GameBox()

    while True:
        clock.tick(60)
        display.blit(background, (0, 0))

        for event in pg.event.get():
            if event.type == QUIT or event.type == WINDOWCLOSE:
                pg.quit()
                sys.exit()

        game_box.draw_game_box()

        pg.display.update()
