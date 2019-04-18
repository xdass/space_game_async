from curses_tools import draw_frame
from animations.explosion import explode
import asyncio
from globalvars import obstacles, obstacles_in_last_collisions


async def fly_garbage(canvas, obstacle, garbage_frame, speed=0.5):
    """Animate garbage, flying from top to bottom. Сolumn position will stay same, as specified on start."""
    rows_number, columns_number = canvas.getmaxyx()

    obstacle.row = 1
    try:
        while obstacle.row < rows_number:
            if obstacle in obstacles_in_last_collisions:
                obstacles_in_last_collisions.remove(obstacle)
                await explode(canvas, obstacle.row, obstacle.column)
                return
            draw_frame(canvas, obstacle.row, obstacle.column, garbage_frame)
            await asyncio.sleep(0)
            draw_frame(canvas, obstacle.row, obstacle.column, garbage_frame, negative=True)
            obstacle.row += speed
    finally:
        obstacles.remove(obstacle)
