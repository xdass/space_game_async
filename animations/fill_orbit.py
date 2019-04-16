import os
from random import randint, choice
from animations.space_garbage import fly_garbage
from helpers.tools import sleep


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
    await sleep(randint(30, 100))
    while True:
        await fly_garbage(canvas, randint(2, max_col - 1), choice(garbage_frames))
