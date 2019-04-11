from collections import namedtuple
from curses_tools import draw_frame, read_controls, get_frame_size
import asyncio


GameField = namedtuple("GameField", "x1 y1 x2 y2")
SpaceShip = namedtuple("SpaceShip", "x1 y1 x2 y2")


def is_ship_inside(field, sx1, sy1, sx2, sy2):

    left_corner = sx1 > field.x1 and sx1 < field.x2 and sy1 > field.y1 and sy1 < field.y2
    right_corner = sx2 > field.x1 and sx2 < field.x2 and sy2 > field.y1 and sy2 < field.y2
    return left_corner and right_corner


async def animate_spaceship(canvas, frames):
    max_row, max_col = canvas.getmaxyx()
    frame_max_row, frame_max_col = get_frame_size(frames[0])
    row = max_row - (frame_max_row + 1)
    col = max_col // 2
    game_field = GameField(x1=0, y1=0, x2=max_col, y2=max_row)
    while True:
        dy, dx, space = read_controls(canvas)
        row_border = row + frame_max_row
        col_border = col + frame_max_col
        prev_x = col
        prev_y = row
        if (0 < col + dx) < (max_col - frame_max_col):
            col += dx
        if (0 < row + dy) < (max_row - frame_max_row):
            row += dy
        # if not is_ship_inside(game_field, col, row, col + frame_max_col, row + frame_max_row):
        #     col = prev_x
        #     row = prev_y

        for frame in frames:
            draw_frame(canvas, row, col, frame)
            await asyncio.sleep(0)
            draw_frame(canvas, row, col, frame, negative=True)
