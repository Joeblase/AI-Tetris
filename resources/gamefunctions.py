import copy

import pygame as pg

import resources.pieces as p
from main import fonts


def text(text_, size):
    return fonts[size].render(text_, False, (255, 255, 255))


def draw_piece(surface, piece, offset=None):
    if piece:
        for rect in piece.rects:
            if offset is None:
                pg.draw.rect(surface, piece.color, rect)
            else:
                pg.draw.rect(surface, piece.color, rect.move(offset))


def remove_pieces(game):
    full_rows = []
    for row, pieces in enumerate(game.pieces_per_row):
        if pieces == 10:  # check if any row has 10 pieces
            full_rows.append(row)

    if full_rows:
        game.removal_rows = len(full_rows)  # this * 2 is rects to remove at a time, also for keeping track of lines
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


def shift_pieces(game):
    if game.removal_pieces:
        if game.removal_counter % 3 == 0:
            for _ in range(game.removal_rows * 2):
                game.removal_pieces.pop(len(game.removal_pieces) // 2)
        if not game.removal_pieces:  # occurs when pieces are done removing
            on_piece_removal(game)
        game.removal_counter += 1
    if game.shift_counter >= 1:
        game.shift_counter += 1
    if game.shift_counter >= 5:
        game.dropped_pieces = game.shifted_dropped_pieces.copy()
        game.shift_counter = 0


def on_piece_removal(game):
    game.lines += game.removal_rows
    game.shift_counter += 1
    if game.level < 15:
        game.level = game.lines // 10 + 1
    game.removal_counter = 0


def rect_check(rect, dropped_pieces):  # returns true if a rect collides with any dropped pieces
    for dropped_piece in dropped_pieces:
        for dropped_rect in dropped_piece.rects:
            if rect.colliderect(dropped_rect):
                return True
    return False


def moveable(new_rects, dropped_pieces):  # returns true if no rect in new rects is out of bounds or is colliding with
    for rect in new_rects:  # a dropped piece
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
    game.drop_pause_counter = 12


def move_sideways(game, direction):
    new_rects = []
    if direction == 'right':
        move_offset = 26
    if direction == 'left':
        move_offset = -26
    if game.piece is not None:
        for rect in game.piece.rects:
            new_rects.append(rect.move(move_offset, 0))
        if moveable(new_rects, game.dropped_pieces):
            game.piece.rects = new_rects.copy()
