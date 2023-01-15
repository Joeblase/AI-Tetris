import pygame as pg
import random
import resources.gamefunctions as gf


def box(x_pos, y_pos):
    return pg.Rect((x_pos * 26 + 78, y_pos * 26), (25, 25))


class Piece:
    def __init__(self, rects, color, orientations):
        self.current_orientation = 1
        self.rects = rects
        self.color = color
        self.total_orientations = orientations

    def rotate(self, dropped_pieces):
        new_rects = self.get_rotations()
        if gf.moveable(new_rects, dropped_pieces):
            if self.current_orientation == self.total_orientations:
                self.current_orientation = 1
            else:
                self.current_orientation += 1
            self.rects = new_rects.copy()


class BlockI(Piece):
    def __init__(self):
        super().__init__([box(0, 0), box(1, 0), box(2, 0), box(3, 0)], (0, 240, 240), 2)

    def get_rotations(self):
        match self.current_orientation:
            case 1:
                return [self.rects[0].move((2*26, -2*26)),
                        self.rects[1].move((26, -26)),
                        self.rects[2],
                        self.rects[3].move((-26, 26))]
            case 2:
                return [self.rects[0].move((-2*26, 2*26)),
                        self.rects[1].move((-26, 26)),
                        self.rects[2],
                        self.rects[3].move((26, -26))]


class BlockJ(Piece):
    def __init__(self):
        super().__init__([box(0, 0), box(1, 0), box(2, 0), box(2, 1)], (0, 0, 240), 4)

    def get_rotations(self):
        match self.current_orientation:
            case 1:
                return [self.rects[0].move((26, -26)),
                        self.rects[1],
                        self.rects[2].move((-26, 26)),
                        self.rects[3].move((-2*26, 0))]
            case 2:
                return [self.rects[0].move((26, 26)),
                        self.rects[1],
                        self.rects[2].move((-26, -26)),
                        self.rects[3].move((0, -2*26))]
            case 3:
                return [self.rects[0].move((-26, 26)),
                        self.rects[1],
                        self.rects[2].move((26, -26)),
                        self.rects[3].move((2*26, 0))]
            case 4:
                return [self.rects[0].move((-26, -26)),
                        self.rects[1],
                        self.rects[2].move((26, 26)),
                        self.rects[3].move((0, 2*26))]


class BlockL(Piece):
    def __init__(self):
        super().__init__([box(0, 0), box(1, 0), box(2, 0), box(0, 1)], (240, 160, 0), 4)

    def get_rotations(self):
        match self.current_orientation:
            case 1:
                return [self.rects[0].move((26, -26)),
                        self.rects[1],
                        self.rects[2].move((-26, 26)),
                        self.rects[3].move((0, -2*26))]
            case 2:
                return [self.rects[0].move((26, 26)),
                        self.rects[1],
                        self.rects[2].move((-26, -26)),
                        self.rects[3].move((2*26, 0))]
            case 3:
                return [self.rects[0].move((-26, 26)),
                        self.rects[1],
                        self.rects[2].move((26, -26)),
                        self.rects[3].move((0, 2*26))]
            case 4:
                return [self.rects[0].move(-26, -26),
                        self.rects[1],
                        self.rects[2].move((26, 26)),
                        self.rects[3].move((-2*26, 0))]


class BlockO(Piece):
    def __init__(self):
        super().__init__([box(0, 0), box(1, 0), box(0, 1), box(1, 1)], (240, 240, 0), 0)

    def rotate(self, droppped_pieces):
        pass


class BlockS(Piece):
    def __init__(self):
        super().__init__([box(1, 0), box(2, 0), box(0, 1), box(1, 1)], (0, 240, 0), 2)

    def get_rotations(self):
        match self.current_orientation:
            case 1:
                return [self.rects[0],
                        self.rects[1].move((-26, 26)),
                        self.rects[2].move((0, -2*26)),
                        self.rects[3].move((-26, -26))]
            case 2:
                return [self.rects[0],
                        self.rects[1].move((26, -26)),
                        self.rects[2].move((0, 2*26)),
                        self.rects[3].move((26, 26))]


class BlockT(Piece):
    def __init__(self):
        super().__init__([box(0, 1), box(1, 1), box(2, 1), box(1, 0)], (160, 0, 240), 4)

    def get_rotations(self):
        match self.current_orientation:
            case 1:
                return [self.rects[0].move((26, -26)),
                        self.rects[1],
                        self.rects[2].move((-26, 26)),
                        self.rects[3].move((26, 26))]
            case 2:
                return [self.rects[0].move((26, 26)),
                        self.rects[1],
                        self.rects[2].move((-26, -26)),
                        self.rects[3].move((-26, 26))]
            case 3:
                return [self.rects[0].move((-26, 26)),
                        self.rects[1],
                        self.rects[2].move((26, -26)),
                        self.rects[3].move((-26, -26))]
            case 4:
                return [self.rects[0].move((-26, -26)),
                        self.rects[1],
                        self.rects[2].move((26, 26)),
                        self.rects[3].move((26, -26))]


class BlockZ(Piece):
    def __init__(self):
        super().__init__([box(0, 0), box(1, 0), box(1, 1), box(2, 1)], (240, 0, 0), 2)

    def get_rotations(self):
        match self.current_orientation:
            case 1:
                return [self.rects[0].move((26, -26)),
                        self.rects[1],
                        self.rects[2].move((-26, -26)),
                        self.rects[3].move((-2*26, 0))]
            case 2:
                return [self.rects[0].move((-26, 26)),
                        self.rects[1],
                        self.rects[2].move((26, 26)),
                        self.rects[3].move((2*26, 0))]


def random_piece(game):
    possible_pieces = [BlockI(), BlockJ(), BlockL(), BlockO(), BlockS(), BlockT(), BlockZ()]
    num = random.randrange(7)
    if num != game.last_piece:
        game.last_piece = num
        return possible_pieces[num]
    else:
        new_num = random.randrange(7)
        game.last_piece = new_num
        return possible_pieces[new_num]


def starting_piece():
    possible_pieces = [BlockI(), BlockJ(), BlockL(), BlockT()]
    return possible_pieces[random.randrange(4)]
