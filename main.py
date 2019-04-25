from animations.stars_animation import blink
from animations.spaceship_animation import animate_spaceship, run_spaceship
from obstacles import show_obstacles
from globalvars import coroutines, obstacles
from game_scenario import start_gameplay
import time
from random import randint, choice
from curses import curs_set
import curses


TIC_TIMEOUT = 0.1
STARS_AMOUNT = 120
SHOW_OBSTACLES_BORDERS = False


def get_window_size():
    window_handle = curses.initscr()
    return window_handle.getmaxyx()


def draw(canvas):
    curs_set(False)
    canvas.nodelay(True)
    canvas.border()
    row, col = get_window_size()
    coroutines.extend([blink(canvas, randint(1, row - 2), randint(1, col - 2), choice("+*.:"))
                       for _ in range(STARS_AMOUNT)])
    coroutines.append(animate_spaceship())
    coroutines.append(start_gameplay(canvas))
    coroutines.append(run_spaceship(canvas))
    if SHOW_OBSTACLES_BORDERS:
        coroutines.append(show_obstacles(canvas, obstacles))

    while True:
        for coroutine in coroutines:
            try:
                coroutine.send(None)
            except StopIteration:
                coroutines.remove(coroutine)
        canvas.refresh()
        time.sleep(TIC_TIMEOUT)


def main():
    curses.update_lines_cols()
    curses.wrapper(draw)


if __name__ == '__main__':
    main()
