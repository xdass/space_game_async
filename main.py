import time
from random import randint, choice
from animations.stars_animation import blink
from animations.spaceship_animation import animate_spaceship, run_spaceship
from animations.fill_orbit import fill_orbit_with_garbage
import curses
from curses import curs_set
from curses_tools import draw_frame
from obstacles import show_obstacles
from globalvars import coroutines, obstacles


TIC_TIMEOUT = 0.1
STARS_AMOUNT = 120
# coroutines = list()


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

    row, col = get_window_size()
    coroutines.extend([blink(canvas, randint(1, row-2), randint(1, col-2), get_star()) for _ in range(STARS_AMOUNT)])
    coroutines.append(animate_spaceship())
    coroutines.append(run_spaceship(canvas))
    coroutines.append(show_obstacles(canvas, obstacles))
    coroutines.append(fill_orbit_with_garbage(canvas))

    while True:
        for coroutine in coroutines:
            try:
                coroutine.send(None)
                canvas.refresh()
            except StopIteration:
                coroutines.remove(coroutine)
        time.sleep(TIC_TIMEOUT)


def main():
    curses.update_lines_cols()
    curses.wrapper(draw)


if __name__ == '__main__':
    main()
