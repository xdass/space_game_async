from curses_tools import get_frame_size
from animations.explosion import explode
from globalvars import obstacles, obstacles_in_last_collisions
from helpers.tools import load_frames
from random import randint, choice
from obstacles import *


async def fly_garbage(canvas,speed=0.5):
    """Animate garbage, flying from top to bottom. Сolumn position will stay same, as specified on start."""
    rows_number, columns_number = canvas.getmaxyx()
    garbage_frames = load_frames("garbages")
    frame = choice(garbage_frames)
    row_size, col_size = get_frame_size(frame)

    obstacle = Obstacle(rows_number, randint(2 + col_size, columns_number - 1) - col_size)
    obstacle.rows_size = row_size
    obstacle.columns_size = col_size
    obstacles.append(obstacle)
    obstacle.row = 1
    try:
        while obstacle.row < rows_number:
            if obstacle in obstacles_in_last_collisions:
                obstacles_in_last_collisions.remove(obstacle)
                await explode(canvas, obstacle.row, obstacle.column)
                return
            draw_frame(canvas, obstacle.row, obstacle.column, frame)
            await asyncio.sleep(0)
            draw_frame(canvas, obstacle.row, obstacle.column, frame, negative=True)
            obstacle.row += speed
    finally:
        obstacles.remove(obstacle)
