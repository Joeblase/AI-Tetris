import copy

import pygame as pg

from main import font
import resources.pieces as p


def text(text_):
    return font.render(text_, False, (255, 255, 255))


def draw_piece(surface, piece):
    if piece:
        for rect in piece.rects:
            pg.draw.rect(surface, piece.color, rect)


def remove_pieces(game):
    full_rows = []
    for row, pieces in enumerate(game.pieces_per_row):
        if pieces == 10:  # check if any row has 10 pieces
            full_rows.append(row)

    if full_rows:
        game.removal_rows = len(full_rows)  # exists so the game knows how many rects to remove at a time
        for row in full_rows:  # shifts game.pieces_per_row
            game.pieces_per_row.pop(row)
            game.pieces_per_row.insert(0, 0)
        for row in full_rows:  # moves pieces to be removed from dropped_pieces to removal_pieces
            for piece in game.dropped_pieces:
                for rect in reversed(piece.rects):
                    if rect.top == row * 26:
                        game.removal_pieces.append(p.Piece([rect], piece.color, 0))
                        piece.rects.remove(rect)
            game.removal_pieces.sort(key=lambda piece_: piece_.rects[0].left)

        # creates a new list of dropped pieces, this is a deep copy because with a shallow copy (.copy()), changes
        # to shifted_dropped_pieces are reflected to dropped_pieces
        game.shifted_dropped_pieces = copy.deepcopy(game.dropped_pieces)
        for row in full_rows:  # shift all rects in the new list down above the row of removal
            for piece in game.shifted_dropped_pieces:
                for rect in reversed(piece.rects):
                    if rect.top < row * 26:
                        rect.top += 26


def rect_check(rect, dropped_pieces):  # returns true if a rect collides with any dropped pieces
    for dropped_piece in dropped_pieces:
        for dropped_rect in dropped_piece.rects:
            if rect.colliderect(dropped_rect):
                return True
    return False


def moveable(new_rects, dropped_pieces):  # returns true if no rect in new rects is out of bounds or is colliding with
    for rect in new_rects:                # a dropped piece
        if rect.top < 0 or rect.top >= 519:
            return False
        if rect.left < 0 or rect.left >= 259:
            return False
        if rect_check(rect, dropped_pieces):
            return False
    return True


def move_down(game):
    new_rects = []
    for rect in game.piece.rects:
        new_rects.append(rect.move(0, 26))
    if moveable(new_rects, game.dropped_pieces):  # Set current piece to moved piece
        game.piece.rects = new_rects.copy()
    else:  # Change current piece to dropped
        make_dropped(game)
    game.drop_counter = 0


def make_dropped(game):
    game.dropped_pieces.append(game.piece)
    for rect in game.piece.rects:
        game.pieces_per_row[rect.top // 26] += 1
    game.piece = None
    game.drop_pause_counter = 10


def move_sideways(game, direction):
    new_rects = []
    match direction:
        case 'right':
            move_offset = 26
        case 'left':
            move_offset = -26
    if game.piece is not None:
        for rect in game.piece.rects:
            new_rects.append(rect.move(move_offset, 0))
        if moveable(new_rects, game.dropped_pieces):
            game.piece.rects = new_rects.copy()
