from curses_tools import draw_frame, read_controls, get_frame_size
from animations.fire_animation import fire
from game_scenario import show_gameover
from helpers.physics import update_speed
from helpers.tools import load_frames
from globalvars import coroutines, obstacles
import globalvars
import asyncio


spaceship_frame = ""


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
        border = 1
        row_speed, col_speed = update_speed(row_speed, col_speed, drow, dcol)

        if border < (col + col_speed) < (max_col - frame_max_col - border):
            col += col_speed
        if border < (row + row_speed) < (max_row - frame_max_row - border):
            row += row_speed

        if space and (globalvars.year >= 2020):
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
    frame_1, frame_2 = frames
    while True:
        spaceship_frame = frame_1
        await asyncio.sleep(0)
        spaceship_frame = frame_2
        await asyncio.sleep(0)