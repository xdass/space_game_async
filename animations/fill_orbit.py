import os
from random import randint, choice
from animations.space_garbage import fly_garbage
from globalvars import obstacles
from obstacles import *
from helpers.tools import sleep
from curses_tools import get_frame_size


def load_garbage_frames():
    frames_dir = "./sprites/garbages/"
    frames = list()
    for file in os.listdir(frames_dir):
        with open(os.path.join(frames_dir, file)) as fh:
            frame = fh.read()
            frames.append(frame)
    return frames


async def fill_orbit_with_garbage(canvas):
    max_row, max_col = canvas.getmaxyx()
    garbage_frames = load_garbage_frames()
    # obstacles.extend([Obstacle(max_row, randint(2, max_col - 1)) for _ in range(0, 4)])
    await sleep(randint(10, 40))
    while True:
        # obstacles.append(Obstacle(max_row, randint(2, max_col - 1)))
        obstacle = Obstacle(max_row, randint(2, max_col - 1))
        frame = choice(garbage_frames)
        row_size, col_size = get_frame_size(frame)
        obstacle.rows_size = row_size
        obstacle.columns_size = col_size
        obstacles.append(obstacle)
        await fly_garbage(canvas, obstacle, frame)
