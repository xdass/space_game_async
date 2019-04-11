from animations.fire_animation import fire
from animations.stars_animation import blink
from animations.spaceship_animation import animate_spaceship
import time
from random import randint, choice
import curses
from curses import curs_set


TIC_TIMEOUT = 0.1
STARS_AMOUNT = 120


def get_window_size():
    window_handle = curses.initscr()
    return window_handle.getmaxyx()


def get_star():
    stars = "+*.:"
    return choice(stars)


def draw(canvas):
    curs_set(False)
    canvas.nodelay(True)
    canvas.border()

    ship_frames = load_ship_frames()
    row, col = get_window_size()
    coroutines = list()
    coroutines.append(animate_spaceship(canvas, ship_frames))
    coroutines.extend([blink(canvas, randint(1, row-2), randint(1, col-2), get_star()) for _ in range(STARS_AMOUNT)])
    
    while True:
        for coroutine in coroutines:
            try:
                coroutine.send(None)
                canvas.refresh()
            except StopIteration:
                coroutines.remove(coroutine)
        time.sleep(TIC_TIMEOUT)


def load_ship_frames():
    with open("./sprites/rocket_frame_1.txt") as fh:
        frame_1 = fh.read()

    with open("./sprites/rocket_frame_2.txt") as fh:
        frame_2 = fh.read()

    return frame_1, frame_2


def main():
    curses.update_lines_cols()
    curses.wrapper(draw)


if __name__ == '__main__':
    main()
