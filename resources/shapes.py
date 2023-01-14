import pygame as pg
import random as rand


def box(x_pos, y_pos):
    return pg.Rect((x_pos * 26 + 78, y_pos * 26), (25, 25))


class BlockI:
    def __init__(self):
        self.rects = [box(0, 0), box(1, 0), box(2, 0), box(3, 0)]
        self.color = (0, 0, 240)

    def rotate(self):
        pass


class BlockJ:
    def __init__(self):
        self.rects = [box(0, 0), box(1, 0), box(2, 0), box(2, 1)]
        self.color = (0, 0, 240)

    def rotate(self):
        pass


class BlockL:
    def __init__(self):
        self.rects = [box(0, 0), box(1, 0), box(2, 0), box(0, 1)]
        self.color = (240, 160, 0)


class BlockO:
    def __init__(self):
        self.rects = [box(0, 0), box(1, 0), box(0, 1), box(1, 1)]
        self.color = (240, 240, 0)

    def rotate(self):
        pass


class BlockS:
    def __init__(self):
        self.rects = [box(1, 0), box(2, 0), box(0, 1), box(1, 1)]
        self.color = (0, 240, 0)


class BlockT:
    def __init__(self):
        self.rects = [box(1, 0), box(0, 1), box(1, 1), box(2, 1)]
        self.color = (160, 0, 240)

    def rotate(self):
        pass


class BlockZ:
    def __init__(self):
        self.rects = [box(0, 0), box(1, 0), box(1, 1), box(2, 1)]
        self.color = (240, 0, 0)

    def rotate(self):
        pass


def random_shape():
    match rand.randrange(7):
        case 0:
            return BlockI()
        case 1:
            return BlockJ()
        case 2:
            return BlockL()
        case 3:
            return BlockO()
        case 4:
            return BlockS()
        case 5:
            return BlockT()
        case 6:
            return BlockZ()
