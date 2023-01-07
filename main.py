import pygame as pg

import game

pg.init()

clock = pg.time.Clock()
pg.display.set_caption('Tetris AI')
pg.display.set_icon(pg.image.load('data/icon.png'))
display = pg.display.set_mode((480, 640), 0, 32)
font = pg.font.Font('data/joystix.ttf', 16)

if __name__ == "__main__":
    game.run()
