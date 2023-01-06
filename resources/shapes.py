import pygame as pg


def box(x_pos, y_pos):
    return pg.Rect((x_pos * 26, y_pos * 26), (25, 25))


i_block = ((box(0, 0), box(1, 0), box(2, 0), box(3, 0)), (0, 240, 240))
j_block = ((box(0, 0), box(1, 0), box(2, 0), box(2, 1)), (0, 0, 240))
l_block = ((box(0, 0), box(1, 0), box(2, 0), box(0, 1)), (240, 160, 0))
o_block = ((box(0, 0), box(1, 0), box(0, 1), box(1, 1)), (240, 240, 0))
s_block = ((box(1, 0), box(2, 0), box(0, 1), box(1, 1)), (0, 240, 0))
t_block = ((box(1, 0), box(0, 1), box(1, 1), box(2, 1)), (160, 0, 240))
z_block = ((box(0, 0), box(1, 0), box(1, 1), box(2, 1)), (240, 0, 0))
