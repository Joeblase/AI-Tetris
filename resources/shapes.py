import pygame as pg
import random as rand


def box(x_pos, y_pos):
    return pg.Rect((x_pos * 26 + 78, y_pos * 26), (25, 25))


i_block = ([box(0, 0), box(1, 0), box(2, 0), box(3, 0)], (0, 240, 240))
j_block = ([box(0, 0), box(1, 0), box(2, 0), box(2, 1)], (0, 0, 240))
l_block = ([box(0, 0), box(1, 0), box(2, 0), box(0, 1)], (240, 160, 0))
o_block = ([box(0, 0), box(1, 0), box(0, 1), box(1, 1)], (240, 240, 0))
s_block = ([box(1, 0), box(2, 0), box(0, 1), box(1, 1)], (0, 240, 0))
t_block = ([box(1, 0), box(0, 1), box(1, 1), box(2, 1)], (160, 0, 240))
z_block = ([box(0, 0), box(1, 0), box(1, 1), box(2, 1)], (240, 0, 0))


def random_shape():
    match rand.randrange(7):
        case 0:
            return i_block
        case 1:
            return j_block
        case 2:
            return l_block
        case 3:
            return o_block
        case 4:
            return s_block
        case 5:
            return t_block
        case 6:
            return z_block
