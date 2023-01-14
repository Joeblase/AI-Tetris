import sys

import pygame as pg
import pygame.locals as pgl

from main import clock, display
from resources.levels import fpg
import resources.gamefunctions as gf
import resources.pieces as p


class GameBox:  # object with properties and surface for the box which the game occurs in
    def __init__(self):
        self.size = (259, 519)
        self.surface = pg.Surface(self.size)
        self.surface.fill((0, 0, 0))
        self.location = (20, 100)
        self.border_size = 8
        self.border = pg.Rect((self.location[0] - self.border_size // 2, self.location[1] - self.border_size // 2),
                              (self.size[0] + self.border_size, self.size[1] + self.border_size))

    def draw_game_box(self):
        pg.draw.rect(display, (180, 180, 180), self.border)
        display.blit(self.surface, self.location)


class Game:
    def __init__(self):
        self.level = 1
        self.drop_type = 'normal'
        self.piece = p.BlockI()  # p.random_shape()
        self.dropped_pieces = []
        self.frame_counter = 0


def run():

    game_box = GameBox()
    game = Game()

    background = pg.image.load('data/background.png')

    while True:

        clock.tick(60)

        display.blit(background, (0, 0))
        game_box.surface.fill((0, 0, 0))

        display.blit(gf.text('lines'), (300, 100))

        for event in pg.event.get():
            if event.type == pgl.QUIT or event.type == pgl.WINDOWCLOSE:
                pg.quit()
                sys.exit()
            if event.type == pgl.KEYDOWN:
                if event.key == pgl.K_LEFT or event.key == pgl.K_a:
                    gf.move_sideways(game, 'left')
                if event.key == pgl.K_RIGHT or event.key == pgl.K_d:
                    gf.move_sideways(game, 'right')
                if event.key == pgl.K_UP or event.key == pgl.K_w:
                    game.piece.rotate(game.dropped_pieces)
                if event.key == pgl.K_LSHIFT:
                    game.drop_type = 'hard'
                if event.key == pgl.K_DOWN or event.key == pgl.K_s:
                    game.drop_type = 'soft'
            if event.type == pgl.KEYUP:
                if event.key == pgl.K_DOWN or event.key == pgl.K_s:
                    game.drop_type = 'normal'

        match game.drop_type:
            case 'normal':
                if game.frame_counter >= fpg[game.level]:
                    gf.move_down(game)
            case 'soft':
                if game.frame_counter >= 2:
                    gf.move_down(game)
            case 'hard':
                pass
        game.frame_counter += 1

        for rect in game.piece.rects:
            pg.draw.rect(game_box.surface, game.piece.color, rect)

        for piece in game.dropped_pieces:
            for rect in piece.rects:
                pg.draw.rect(game_box.surface, piece.color, rect)

        game_box.draw_game_box()

        pg.display.update()
