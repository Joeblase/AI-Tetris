import pygame as pg

import game

clock = pg.time.Clock()
pg.display.set_caption('Tetris')
display = pg.display.set_mode((480, 640), 0, 32)

pg.init()

if __name__ == "__main__":
    game.run()
