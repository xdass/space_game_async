from globalvars import obstacles
from obstacles import show_obstacles
from curses_tools import draw_frame, get_frame_size
import asyncio


async def fly_garbage(canvas, obstacle, garbage_frame, speed=0.5):
    """Animate garbage, flying from top to bottom. Сolumn position will stay same, as specified on start."""
    rows_number, columns_number = canvas.getmaxyx()

    # obstacle.column = max(obstacle.column, 0)
    # obstacle.column = min(obstacle.column, columns_number - 1)
    obstacle.row = 1
    while obstacle.row < rows_number:
        draw_frame(canvas, obstacle.row, obstacle.column, garbage_frame)
        await asyncio.sleep(0)
        draw_frame(canvas, obstacle.row, obstacle.column, garbage_frame, negative=True)
        obstacle.row += speed
