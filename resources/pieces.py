import pygame as pg
import random
import resources.gamefunctions as gf


def box(x_pos, y_pos):
    return pg.Rect((x_pos * 26 + 78, y_pos * 26), (25, 25))


class BlockI:
    def __init__(self):
        self.rects = [box(0, 0), box(1, 0), box(2, 0), box(3, 0)]
        self.orientation = 1
        self.color = (0, 0, 240)

    def rotate(self, dropped_pieces):
        match self.orientation:
            case 1:
                new_rects = [self.rects[0].move((2*26, -2*26)),
                             self.rects[1].move((1*26, -1*26)),
                             self.rects[2],
                             self.rects[3].move((-1*26, 1*26))]
                if gf.moveable(new_rects, dropped_pieces):
                    self.rects = new_rects.copy()
                    self.orientation = 2
            case 2:
                new_rects = [self.rects[0].move((-2*26, 2*26)),
                             self.rects[1].move((-1*26, 1*26)),
                             self.rects[2],
                             self.rects[3].move((1*26, -1*26))]
                if gf.moveable(new_rects, dropped_pieces):
                    self.rects = new_rects.copy()
                    self.orientation = 1


class BlockJ:
    def __init__(self):
        self.rects = [box(0, 0), box(1, 0), box(2, 0), box(2, 1)]
        self.orientation = 1
        self.color = (0, 0, 240)

    def rotate(self, dropped_pieces):
        match self.orientation:
            case 1:
                new_rects = [self.rects[0].move((1*26, -1*26)),
                             self.rects[1],
                             self.rects[2].move((-1*26, 1*26)),
                             self.rects[3].move((-2*26, 0))]
                if gf.moveable(new_rects, dropped_pieces):
                    self.rects = new_rects.copy()
                    self.orientation = 2
            case 2:
                new_rects = [self.rects[0].move((1*26, 1*26)),
                             self.rects[1],
                             self.rects[2].move((-1*26, -1*26)),
                             self.rects[3].move((0, -2*26))]
                if gf.moveable(new_rects, dropped_pieces):
                    self.rects = new_rects.copy()
                    self.orientation = 3
            case 3:
                new_rects = [self.rects[0].move((-1*26, 1*26)),
                             self.rects[1],
                             self.rects[2].move((1*26, -1*26)),
                             self.rects[3].move((2*26, 0))]
                if gf.moveable(new_rects, dropped_pieces):
                    self.rects = new_rects.copy()
                    self.orientation = 4
            case 4:
                new_rects = [self.rects[0].move((-1*26, -1*26)),
                             self.rects[1],
                             self.rects[2].move((1*26, 1*26)),
                             self.rects[3].move((0, 2*26))]
                if gf.moveable(new_rects, dropped_pieces):
                    self.rects = new_rects.copy()
                    self.orientation = 1


class BlockL:
    def __init__(self):
        self.rects = [box(0, 0), box(1, 0), box(2, 0), box(0, 1)]
        self.orientation = 1
        self.color = (240, 160, 0)

    def rotate(self, dropped_pieces):
        match self.orientation:
            case 1:
                new_rects = [self.rects[0].move((1*26, -1*26)),
                             self.rects[1],
                             self.rects[2].move((-1*26, 1*26)),
                             self.rects[3].move((0, -2*26))]
                if gf.moveable(new_rects, dropped_pieces):
                    self.rects = new_rects.copy()
                    self.orientation = 2
            case 2:
                new_rects = [self.rects[0].move((1*26, 1*26)),
                             self.rects[1],
                             self.rects[2].move((-1*26, -1*26)),
                             self.rects[3].move((2*26, 0))]
                if gf.moveable(new_rects, dropped_pieces):
                    self.rects = new_rects.copy()
                    self.orientation = 3
            case 3:
                new_rects = [self.rects[0].move((-1*26, 26)),
                             self.rects[1],
                             self.rects[2].move((1*26, -1*26)),
                             self.rects[3].move((0, 2*26))]
                if gf.moveable(new_rects, dropped_pieces):
                    self.rects = new_rects.copy()
                    self.orientation = 4
            case 4:
                new_rects = [self.rects[0].move(-1*26, -26),
                             self.rects[1],
                             self.rects[2].move((1*26, 1*26)),
                             self.rects[3].move((-2*26, 0))]
                if gf.moveable(new_rects, dropped_pieces):
                    self.rects = new_rects.copy()
                    self.orientation = 1


class BlockO:
    def __init__(self):
        self.rects = [box(0, 0), box(1, 0), box(0, 1), box(1, 1)]
        self.orientation = 1
        self.color = (240, 240, 0)

    def rotate(self, droppped_pieces):
        pass


class BlockS:
    def __init__(self):
        self.rects = [box(1, 0), box(2, 0), box(0, 1), box(1, 1)]
        self.orientation = 1
        self.color = (0, 240, 0)

    def rotate(self, dropped_pieces):
        match self.orientation:
            case 1:
                new_rects = [self.rects[0],
                             self.rects[1].move((-1*26, 1*26)),
                             self.rects[2].move((0, -2*26)),
                             self.rects[3].move((-1*26, -1*26))]
                if gf.moveable(new_rects, dropped_pieces):
                    self.rects = new_rects.copy()
                    self.orientation = 2
            case 2:
                new_rects = [self.rects[0],
                             self.rects[1].move((1*26, -1*26)),
                             self.rects[2].move((0, 2*26)),
                             self.rects[3].move((1*26, 1*26))]
                if gf.moveable(new_rects, dropped_pieces):
                    self.rects = new_rects.copy()
                    self.orientation = 1


class BlockT:
    def __init__(self):
        self.rects = [box(0, 1), box(1, 1), box(2, 1), box(1, 0)]
        self.orientation = 1
        self.color = (160, 0, 240)

    def rotate(self, dropped_pieces):
        match self.orientation:
            case 1:
                new_rects = [self.rects[0].move((1*26, -1*26)),
                             self.rects[1],
                             self.rects[2].move((-1*26, 1*26)),
                             self.rects[3].move((1*26, 1*26))]
                if gf.moveable(new_rects, dropped_pieces):
                    self.rects = new_rects.copy()
                    self.orientation = 2
            case 2:
                new_rects = [self.rects[0].move((1*26, 1*26)),
                             self.rects[1],
                             self.rects[2].move((-1*26, -1*26)),
                             self.rects[3].move((-1*26, 1*26))]
                if gf.moveable(new_rects, dropped_pieces):
                    self.rects = new_rects.copy()
                    self.orientation = 3
            case 3:
                new_rects = [self.rects[0].move((-1*26, 1*26)),
                             self.rects[1],
                             self.rects[2].move((1*26, -1*26)),
                             self.rects[3].move((-1*26, -1*26))]
                if gf.moveable(new_rects, dropped_pieces):
                    self.rects = new_rects.copy()
                    self.orientation = 4
            case 4:
                new_rects = [self.rects[0].move((-1*26, -1*26)),
                             self.rects[1],
                             self.rects[2].move((1*26, 1*26)),
                             self.rects[3].move((1*26, -1*26))]
                if gf.moveable(new_rects, dropped_pieces):
                    self.rects = new_rects.copy()
                    self.orientation = 1


class BlockZ:
    def __init__(self):
        self.rects = [box(0, 0), box(1, 0), box(1, 1), box(2, 1)]
        self.orientation = 1
        self.color = (240, 0, 0)

    def rotate(self, dropped_pieces):
        match self.orientation:
            case 1:
                new_rects = [self.rects[0].move((1*26, -1*26)),
                             self.rects[1],
                             self.rects[2].move((-1*26, -1*26)),
                             self.rects[3].move((-2*26, 0))]
                if gf.moveable(new_rects, dropped_pieces):
                    self.rects = new_rects.copy()
                    self.orientation = 2
            case 2:
                new_rects = [self.rects[0].move((-1*26, 1*26)),
                             self.rects[1],
                             self.rects[2].move((1*26, 1*26)),
                             self.rects[3].move((2*26, 0))]
                if gf.moveable(new_rects, dropped_pieces):
                    self.rects = new_rects.copy()
                    self.orientation = 1


def random_shape():
    match random.randrange(7):
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
