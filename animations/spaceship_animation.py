from curses_tools import draw_frame, read_controls, get_frame_size
from animations.fire_animation import fire
from helpers.physics import update_speed
from helpers.tools import load_frames
from globalvars import coroutines, obstacles
import asyncio


spaceship_frame = ""


async def show_gameover(canvas):
    max_row, max_col = canvas.getmaxyx()
    gameover_frame = load_frames("gameover")
    frame_max_row, frame_max_col = get_frame_size(gameover_frame[0])
    row = max_row // 2 - (frame_max_row // 2)
    col = max_col // 2 - (frame_max_col // 2)
    while True:
        draw_frame(canvas, row, col, gameover_frame[0])
        await asyncio.sleep(0)
        draw_frame(canvas, row, col, gameover_frame[0])


async def run_spaceship(canvas):
    # Положение корабля и отрисовка
    global spaceship_frame
    max_row, max_col = canvas.getmaxyx()

    frame_max_row, frame_max_col = get_frame_size(load_frames("rocket")[0])
    row = max_row - (frame_max_row + 1)
    col = max_col // 2
    row_speed = col_speed = 0

    while True:
        drow, dcol, space = read_controls(canvas)

        row_speed, col_speed = update_speed(row_speed, col_speed, drow, dcol)

        if 1 < col + col_speed < (max_col - frame_max_col):
            col += col_speed
        if 1 < row + row_speed < (max_row - frame_max_row):
            row += row_speed

        if space:
            coroutines.append(fire(canvas, row, col+2))

        for obstacle in obstacles:
            if obstacle.has_collision(row, col):
                coroutines.append(show_gameover(canvas))
                return

        draw_frame(canvas, row, col, spaceship_frame)
        old_frame = spaceship_frame
        await asyncio.sleep(0)
        draw_frame(canvas, row, col, old_frame, negative=True)


async def animate_spaceship():
    # Обновляет spaceship frame
    global spaceship_frame
    frames = load_frames("rocket")
    while True:
        spaceship_frame = frames[0]
        await asyncio.sleep(0)
        spaceship_frame = frames[1]
        await asyncio.sleep(0)