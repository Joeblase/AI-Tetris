import sys

import pygame as pg
import pygame.locals as pgl

import resources.gamefunctions as gf
import resources.pieces as p
from resources.levels import fpg

pg.init()
pg.display.set_caption('Tetris AI')
pg.display.set_icon(pg.image.load('data/icon.png'))
display = pg.display.set_mode((480, 640), 0, 32)

clock = pg.time.Clock()
fonts = []
for num in range(1, 51):
    fonts.append(pg.font.Font('data/joystix.ttf', num))


class GameBox:  # object containing separate surface where game occurs
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


class Game:  # class for storing game variables so they can be passed and modified by game functions
    def __init__(self):
        self.state = 'playing'

        self.lines = 0
        self.level = 1
        self.score = 0

        self.drop_counter = 0
        self.drop_pause_counter = 0
        self.removal_counter = 0
        self.shift_counter = 0

        self.drop_type = 'normal'

        self.dropped_pieces = []
        self.shifted_dropped_pieces = []
        self.removal_pieces = []  # pieces to be removed

        self.removal_rows = 0

        self.last_piece = None
        self.piece = p.starting_piece()
        self.next_piece = p.random_piece(self)

        self.pieces_per_row = [0 for _ in range(20)]


def run():
    game_box = GameBox()
    game = Game()
    r_key, l_shift_key = False, False

    background = pg.image.load('data/background.png')

    while True:

        clock.tick(60)

        display.blit(background, (0, 0))
        game_box.surface.fill((0, 0, 0))

        gf.draw_piece(display, game.next_piece, (290, 585))
        display.blit(gf.text('next', 18), (295, 598))

        display.blit(gf.text('score', 30), (316, 180))
        display.blit(gf.text(str(game.score).zfill(5), 30), (316, 210))

        display.blit(gf.text('lines', 30), (316, 250))
        display.blit(gf.text(str(game.lines).zfill(5), 30), (316, 280))
        display.blit(gf.text('level', 30), (316, 320))
        display.blit(gf.text(str(game.level).zfill(5), 30), (316, 350))

        for event in pg.event.get():
            if event.type == pgl.QUIT or event.type == pgl.WINDOWCLOSE:
                pg.quit()
                sys.exit()
            if event.type == pgl.KEYDOWN:
                if event.key == pgl.K_r:
                    r_key = True
                if event.key == pgl.K_LSHIFT:
                    l_shift_key = True
            if event.type == pgl.KEYUP:
                if event.key == pgl.K_r:
                    r_key = False
                if event.key == pgl.K_LSHIFT:
                    l_shift_key = False
            if game.state == 'playing':
                if event.type == pgl.KEYDOWN:
                    if event.key == pgl.K_LEFT or event.key == pgl.K_a:
                        gf.move_sideways(game, 'left')
                    if event.key == pgl.K_RIGHT or event.key == pgl.K_d:
                        gf.move_sideways(game, 'right')
                    if event.key == pgl.K_UP or event.key == pgl.K_w:
                        if game.piece is not None:
                            game.piece.rotate(game.dropped_pieces)
                    if event.key == pgl.K_DOWN or event.key == pgl.K_s:
                        game.drop_type = 'soft'
                if event.type == pgl.KEYUP:
                    if event.key == pgl.K_DOWN or event.key == pgl.K_s:
                        game.drop_type = 'normal'

        if r_key and l_shift_key:
            run()

        if game.state == 'playing':
            if game.drop_pause_counter == 0:
                if not game.piece:
                    game.piece = game.next_piece
                    game.next_piece = p.random_piece(game)
                    game.drop_type = 'normal'
                    if not gf.moveable(game.next_piece.rects, game.dropped_pieces):
                        game.state = 'lost'
                if game.drop_type == 'normal':
                    if game.drop_counter >= fpg[game.level]:
                        gf.move_down(game)
                if game.drop_type == 'soft':
                    if game.drop_counter >= 2:
                        gf.move_down(game)
                game.drop_counter += 1

            if game.drop_pause_counter > 0:
                game.drop_pause_counter -= 1

            gf.remove_pieces(game)
            gf.shift_pieces(game)

        # draw pieces to game box
        for piece in game.dropped_pieces:
            gf.draw_piece(game_box.surface, piece)
        for piece in game.removal_pieces:
            gf.draw_piece(game_box.surface, piece)
        gf.draw_piece(game_box.surface, game.piece)

        game_box.draw_game_box()

        if game.state == 'lost':
            display.blit(gf.text('you lost!', 26), (55, 300))
            display.blit(gf.text('shift + r to restart', 10), (60, 330))

        pg.display.update()


if __name__ == "__main__":
    run()
