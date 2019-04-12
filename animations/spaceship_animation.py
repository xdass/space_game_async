from collections import namedtuple
from curses_tools import draw_frame, read_controls, get_frame_size
import asyncio


GameField = namedtuple("GameField", "x1 y1 x2 y2")
SpaceShip = namedtuple("SpaceShip", "x1 y1 x2 y2")


async def animate_spaceship(canvas, frames):
    max_row, max_col = canvas.getmaxyx()
    frame_max_row, frame_max_col = get_frame_size(frames[0])
    row = max_row - (frame_max_row + 1)
    col = max_col // 2
    while True:
        dy, dx, space = read_controls(canvas)
        new_col = col + dx
        new_row = row + dy
        if 0 < new_col < (max_col - frame_max_col):
            col += dx
        if 0 < new_row < (max_row - frame_max_row):
            row += dy

        for frame in frames:
            draw_frame(canvas, row, col, frame)
            await asyncio.sleep(0)
            draw_frame(canvas, row, col, frame, negative=True)
