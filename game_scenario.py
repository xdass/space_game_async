from helpers.tools import sleep
from animations.space_garbage import fly_garbage
from curses_tools import draw_frame, get_frame_size
from helpers.tools import load_frames
from globalvars import coroutines
import globalvars
import time

PHRASES = {
    # Только на английском, Repl.it ломается на кириллице
    1957: "First Sputnik!",
    1961: "Gagarin flew!",
    1969: "Armstrong got on the moon!",
    1971: "First orbital space station Salute-1",
    1981: "Flight of the Shuttle Columbia",
    1998: 'ISS start building',
    2011: 'Messenger launch to Mercury',
    2020: "Take the plasma gun! Shoot the garbage!",
    2030: "You are still alive?!"
}


async def show_gameover(canvas):
    max_row, max_col = canvas.getmaxyx()
    frame = load_frames("gameover")
    frame_max_row, frame_max_col = get_frame_size(frame)
    row = max_row // 2 - (frame_max_row // 2)
    col = max_col // 2 - (frame_max_col // 2)
    while True:
        draw_frame(canvas, row, col, frame)
        await sleep(1)
        draw_frame(canvas, row, col, frame)


def get_garbage_delay_tics(year):
    if year < 1961:
        return None
    elif year < 1969:
        return 20
    elif year < 1981:
        return 14
    elif year < 1995:
        return 10
    elif year < 2010:
        return 8
    elif year < 2020:
        return 6
    else:
        return 2


async def start_gameplay(canvas):
    info_row, info_col = canvas.getmaxyx()
    info_canvas = canvas.derwin(info_row-3, info_col - 50)
    coroutines.append(show_game_info(info_canvas))
    while True:
        start = int(time.time())
        delay = get_garbage_delay_tics(globalvars.year)
        if delay:
            await sleep(delay)
            coroutines.append(fly_garbage(canvas))
        else:
            await sleep(15)
        if int(time.time()) - start >= 1:
            globalvars.year += 1


async def show_game_info(info_canvas):
    last_phrase = ""
    info_row, info_col = info_canvas.getmaxyx()
    while True:
        phrase = PHRASES.get(globalvars.year, "")
        draw_frame(info_canvas, 0, info_col-6, text=f"{globalvars.year}")
        draw_frame(info_canvas, 1, info_col - len(last_phrase) - 1, text=f"{last_phrase}", negative=True)
        draw_frame(info_canvas, 1, info_col - len(phrase) - 1, text=f"{phrase}")
        last_phrase = phrase
        await sleep(1)
        info_canvas.refresh()