import pygame as pg
import random as rand


def box(x_pos, y_pos):
    return pg.Rect((x_pos * 26 + 78, y_pos * 26), (25, 25))


class I_Block:
    def __init__(self):
        self.rects = [box(0, 0), box(1, 0), box(2, 0), box(3, 0)]
        self.color = (0, 0, 240)

    def rotate(self):
        pass


class J_Block:
    def __init__(self):
        self.rects = [box(0, 0), box(1, 0), box(2, 0), box(2, 1)]
        self.color = (0, 0, 240)

    def rotate(self):
        pass


class L_Block:
    def __init__(self):
        self.rects = [box(0, 0), box(1, 0), box(2, 0), box(0, 1)]
        self.color = (240, 160, 0)


class O_Block:
    def __init__(self):
        self.rects = [box(0, 0), box(1, 0), box(0, 1), box(1, 1)]
        self.color = (240, 240, 0)

    def rotate(self):
        pass


class S_Block:
    def __init__(self):
        self.rects = [box(1, 0), box(2, 0), box(0, 1), box(1, 1)]
        self.color = (0, 240, 0)


class T_Block:
    def __init__(self):
        self.rects = [box(1, 0), box(0, 1), box(1, 1), box(2, 1)]
        self.color = (160, 0, 240)

    def rotate(self):
        pass


class Z_Block:
    def __init__(self):
        self.rects = [box(0, 0), box(1, 0), box(1, 1), box(2, 1)]
        self.color = (240, 0, 0)

    def rotate(self):
        pass


def random_shape():
    match rand.randrange(7):
        case 0:
            return I_Block()
        case 1:
            return J_Block()
        case 2:
            return L_Block()
        case 3:
            return O_Block()
        case 4:
            return S_Block()
        case 5:
            return T_Block()
        case 6:
            return Z_Block()
