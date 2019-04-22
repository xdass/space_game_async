from random import randint, choice
from animations.space_garbage import fly_garbage
from globalvars import obstacles, coroutines
from obstacles import *
from helpers.tools import sleep, load_frames
from curses_tools import get_frame_size


async def fill_orbit_with_garbage(canvas):
    max_row, max_col = canvas.getmaxyx()
    garbage_frames = load_frames("garbages")
    frame = choice(garbage_frames)
    row_size, col_size = get_frame_size(frame)
    obstacle = Obstacle(max_row, randint(2 + col_size, max_col - 1) - col_size)
    obstacle.rows_size = row_size
    obstacle.columns_size = col_size
    obstacles.append(obstacle)
    coroutines.append(fly_garbage(canvas, obstacle, frame))
