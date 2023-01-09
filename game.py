import sys

import pygame as pg
import pygame.locals as pgl

from main import clock, display
from resources.levels import fpg
import resources.gamefunctions as gf
import resources.shapes as shp


class GameBox:
    def __init__(self):
        self.size = (259, 509)
        self.surface = pg.Surface(self.size)
        self.surface.fill((0, 0, 0))
        self.location = (20, 100)
        self.border_size = 8
        self.border = pg.Rect((self.location[0] - self.border_size // 2, self.location[1] - self.border_size // 2),
                              (self.size[0] + self.border_size, self.size[1] + self.border_size))

    def draw_game_box(self):
        pg.draw.rect(display, (180, 180, 180), self.border)
        display.blit(self.surface, self.location)


def run():

    background = pg.image.load('data/background.png')
    game_box = GameBox()
    pieces = [shp.random_shape()]
    move_counter = 0
    level = 1

    while True:

        clock.tick(60)

        display.blit(background, (0, 0))
        game_box.surface.fill((0, 0, 0))

        for event in pg.event.get():
            if event.type == pgl.QUIT or event.type == pgl.WINDOWCLOSE:
                pg.quit()
                sys.exit()
            if event.type == pgl.KEYDOWN:
                if event.key == pgl.K_LEFT:
                    pass  # move left
                if event.key == pgl.K_RIGHT:
                    pass  # move right
                if event.key == pgl.K_UP or event.key == pgl.K_x:
                    pass  # rotate clockwise
                if event.key == pgl.K_RCTRL or event.key == pgl.K_LCTRL or event.key == pgl.K_z:
                    pass  # rotate counterclockwise
                if event.key == pgl.K_DOWN:
                    pass  # drop

        if move_counter == fpg[level]:
            gf.move_down(pieces[-1])
            move_counter = 0

        move_counter += 1

        for piece in pieces:
            for rect in piece.rects:
                pg.draw.rect(game_box.surface, piece.color, rect)

        game_box.draw_game_box()

        pg.display.update()
