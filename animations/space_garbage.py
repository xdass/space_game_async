from curses_tools import draw_frame
import asyncio
from globalvars import obstacles


async def fly_garbage(canvas, obstacle, garbage_frame, speed=0.5):
    """Animate garbage, flying from top to bottom. Сolumn position will stay same, as specified on start."""
    rows_number, columns_number = canvas.getmaxyx()

    obstacle.row = 1
    try:
        while obstacle.row < rows_number:
            draw_frame(canvas, obstacle.row, obstacle.column, garbage_frame)
            await asyncio.sleep(0)
            draw_frame(canvas, obstacle.row, obstacle.column, garbage_frame, negative=True)
            obstacle.row += speed
    finally:
        obstacles.remove(obstacle)
