from main import font
import resources.shapes as shp


def text(text_):
    return font.render(text_, False, (255, 255, 255))


def moveable_down(piece, dropped_pieces):
    moved_rects = []  # created to check for collision
    for rect in piece.rects:
        if rect.top == 494:
            return False
        moved_rects.append(rect.move(0, 26))
    for rect in moved_rects:
        for dropped_piece in dropped_pieces:
            for dropped_rect in dropped_piece.rects:
                if rect.colliderect(dropped_rect):
                    return False
    return True


def move(game):
    new_rects = []
    if moveable_down(game.piece, game.dropped_pieces):  # move piece down if moveable
        for rect in game.piece.rects:
            new_rects.append(rect.move(0, 26))
        game.piece.rects = new_rects.copy()
    else:  # change piece to dropped state
        game.dropped_pieces.append(game.piece)
        game.piece = shp.random_shape()
    game.frame_counter = 0


def moveable_sideways(piece, dropped_pieces, move_offset, wall_value):
    moved_rects = []
    for rect in piece.rects:
        if rect.left == wall_value:
            return False
        moved_rects.append(rect.move(move_offset, 0))
    for rect in moved_rects:
        for dropped_piece in dropped_pieces:
            for dropped_rect in dropped_piece.rects:
                if rect.colliderect(dropped_rect):
                    return False
    return True


def move_sideways(game, direction):
    new_rects = []
    match direction:
        case 'right':
            move_offset, wall_value = 26, 234  # move offset is the amount of pixels to move
        case 'left':
            move_offset, wall_value = -26, 0  # wall value is the location of a rect when touching the wall
    if moveable_sideways(game.piece, game.dropped_pieces, move_offset, wall_value):
        for rect in game.piece.rects:
            new_rects.append(rect.move(move_offset, 0))
            game.piece.rects = new_rects.copy()
