import pygame as pg

import game

pg.init()

pg.display.set_caption('Tetris AI')
pg.display.set_icon(pg.image.load('data/icon.png'))
display = pg.display.set_mode((480, 640), 0, 32)

clock = pg.time.Clock()

font = pg.font.Font('data/joystix.ttf', 16)

if __name__ == "__main__":
    game.run()
