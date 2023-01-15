from main import font


def text(text_):
    return font.render(text_, False, (255, 255, 255))


def remove_full_rows(game):
    full_rows = []
    for row, pieces in enumerate(game.pieces_per_row):
        if pieces == 10:  # check if any row has 10 pieces
            full_rows.append(row)
    for row in full_rows:
        game.lines += 1
        if game.lines % 10 == 0:
            game.level += 1
        for piece in game.dropped_pieces:
            for rect in reversed(piece.rects):
                if rect.top == row * 26:
                    piece.rects.remove(rect)
        game.pieces_per_row.pop(row)
        game.pieces_per_row.insert(0, 0)
        full_rows.pop(0)
        for piece in game.dropped_pieces:
            for rect in piece.rects:
                if rect.top < row*26:
                    rect.top += 26


def rect_check(rect, dropped_pieces):  # returns true if a rect collides with any dropped pieces
    for dropped_piece in dropped_pieces:
        for dropped_rect in dropped_piece.rects:
            if rect.colliderect(dropped_rect):
                return True
    return False


def moveable(new_rects, dropped_pieces):
    for rect in new_rects:
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
        game.dropped_pieces.append(game.piece)
        for rect in game.piece.rects:
            game.pieces_per_row[rect.top//26] += 1
        game.piece = None
        game.drop_pause = 5
    game.frame_counter = 0


def move_sideways(game, direction):
    new_rects = []
    match direction:
        case 'right':
            move_offset = 26
        case 'left':
            move_offset = -26
    if game.piece.rects is not None:
        for rect in game.piece.rects:
            new_rects.append(rect.move(move_offset, 0))
        if moveable(new_rects, game.dropped_pieces):
            game.piece.rects = new_rects.copy()
