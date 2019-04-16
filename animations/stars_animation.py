from random import randint
from helpers.tools import sleep
import curses


async def blink(canvas, row, column, star):
    while True:
        await sleep(randint(0, 20))

        canvas.addstr(row, column, star, curses.A_DIM)
        await sleep(20)

        canvas.addstr(row, column, star)
        await sleep(3)

        canvas.addstr(row, column, star, curses.A_BOLD)
        await sleep(5)

        canvas.addstr(row, column, star)
        await sleep(3)
