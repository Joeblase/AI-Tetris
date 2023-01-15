import pygame as pg

import game

pg.init()

pg.display.set_caption('Tetris AI')
pg.display.set_icon(pg.image.load('data/icon.png'))
display = pg.display.set_mode((480, 640), 0, 32)

clock = pg.time.Clock()

fonts = []
for num in range(1, 51):
    fonts.append(pg.font.Font('data/joystix.ttf', num))

if __name__ == "__main__":
    game.run()
