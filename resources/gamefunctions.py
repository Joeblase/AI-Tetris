from main import font
import resources.shapes as shp


def text(text_):
    return font.render(text_, False, (255, 255, 255))


def moveable_check(piece, dropped_pieces):
    moved_rects = []  # created to check for collision
    for rect in piece.rects:
        if rect.top == 494:
            return False
        moved_rects.append(rect.move(0, 26))
    for piece_rect in piece.rects:
        for dropped_piece in dropped_pieces:
            for dropped_rect in dropped_piece.rects:
                if piece_rect.colliderect(dropped_rect):
                    return False
    return True


def move(game):
    new_rects = []
    if moveable_check(game.controlled_piece, game.dropped_pieces):  # move piece down if moveable
        for rect in game.controlled_piece.rects:
            new_rects.append(rect.move(0, 26))
        game.controlled_piece.rects = new_rects.copy()
    else:  # change piece to dropped state
        game.dropped_pieces.append(game.controlled_piece)
        game.controlled_piece = shp.random_shape()
    game.frame_counter = 0

def move_sideways(piece, direction):
    new_rects = []
    match direction:
        case 'right':
            for rect in piece.rects:
                new_rects.append(rect.move(26, 0))
        case 'left':
            for rect in piece.rects:
                new_rects.append(rect.move(-26, 0))
    piece.rects = new_rects.copy()
