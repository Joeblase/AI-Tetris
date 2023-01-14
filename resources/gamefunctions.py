from main import font
import resources.pieces as p


def text(text_):
    return font.render(text_, False, (255, 255, 255))


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
    if moveable(new_rects, game.dropped_pieces):
        game.piece.rects = new_rects.copy()
    else:
        game.dropped_pieces.append(game.piece)
        game.piece = p.random_shape()
    game.frame_counter = 0


def move_sideways(game, direction):
    new_rects = []
    match direction:
        case 'right':
            move_offset = 26
        case 'left':
            move_offset = -26
    for rect in game.piece.rects:
        new_rects.append(rect.move(move_offset, 0))
    if moveable(new_rects, game.dropped_pieces):
        game.piece.rects = new_rects.copy()
