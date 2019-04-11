from random import randint
import asyncio
import curses


async def timeout(pause):
    for _ in range(pause):
        await asyncio.sleep(0)


async def blink(canvas, row, column, star):
    while True:
        for _ in range(5, randint(0, 20)):
            await asyncio.sleep(0)

        canvas.addstr(row, column, star, curses.A_DIM)
        await timeout(20)

        canvas.addstr(row, column, star)
        await timeout(3)

        canvas.addstr(row, column, star, curses.A_BOLD)
        await timeout(5)

        canvas.addstr(row, column, star)
        await timeout(3)
