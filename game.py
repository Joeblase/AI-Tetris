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
        pg.draw.rect(display, (180, 180, 180), self .border)
        display.blit(self.surface, self.location)


class Game:
    def __init__(self):
        self.lines = 0
        self.level = 1

        self.drop_counter = 0
        self.drop_pause_counter = 0
        self.removal_counter = 0

        self.drop_type = 'normal'

        self.dropped_pieces = []
        self.shifted_dropped_pieces = []
        self.removal_pieces = []  # Pieces to be removed

        self.removal_rows = 0

        self.piece = p.starting_piece()

        self.pieces_per_row = [0 for _ in range(20)]


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
                    if game.piece is not None:
                        game.piece.rotate(game.dropped_pieces)
                if event.key == pgl.K_LSHIFT:
                    game.drop_type = 'hard'
                if event.key == pgl.K_DOWN or event.key == pgl.K_s:
                    game.drop_type = 'soft'
            if event.type == pgl.KEYUP:
                if event.key == pgl.K_DOWN or event.key == pgl.K_s:
                    game.drop_type = 'normal'

        if game.drop_pause_counter == 0:
            if not game.piece:
                game.piece = p.random_piece()
            match game.drop_type:
                case 'normal':
                    if game.drop_counter >= fpg[game.level]:
                        gf.move_down(game)
                case 'soft':
                    if game.drop_counter >= 2:
                        gf.move_down(game)
                case 'hard':
                    pass
            game.drop_counter += 1

        if game.drop_pause_counter > 0:
            game.drop_pause_counter -= 1

        gf.remove_pieces(game)

        if game.removal_pieces:
            if game.removal_counter % 3 == 0:
                for _ in range(game.removal_rows * 2):
                    game.removal_pieces.pop(len(game.removal_pieces)//2)
            if not game.removal_pieces:  # occurs when pieces are done removing
                game.lines += 1
                if game.lines % 10 == 0:
                    game.level += 1
                game.dropped_pieces = game.shifted_dropped_pieces.copy()
            game.removal_counter += 1

        # draw pieces to game box
        gf.draw_piece(game_box.surface, game.piece)
        for piece in game.dropped_pieces:
            gf.draw_piece(game_box.surface, piece)
        for piece in game.removal_pieces:
            gf.draw_piece(game_box.surface, piece)

        game_box.draw_game_box()

        pg.display.update()
