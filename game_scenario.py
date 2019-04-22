from helpers.tools import sleep
from animations.fill_orbit import fill_orbit_with_garbage
from curses_tools import draw_frame, get_frame_size
from helpers.tools import load_frames
from globalvars import coroutines, year
import time

PHRASES = {
    # Только на английском, Repl.it ломается на кириллице
    1957: "First Sputnik",
    1961: "Gagarin flew!",
    1969: "Armstrong got on the moon!",
    1971: "First orbital space station Salute-1",
    1981: "Flight of the Shuttle Columbia",
    1998: 'ISS start building',
    2011: 'Messenger launch to Mercury',
    2020: "Take the plasma gun! Shoot the garbage!",
}


async def show_gameover(canvas):
    max_row, max_col = canvas.getmaxyx()
    gameover_frame = load_frames("gameover")
    frame_max_row, frame_max_col = get_frame_size(gameover_frame[0])
    row = max_row // 2 - (frame_max_row // 2)
    col = max_col // 2 - (frame_max_col // 2)
    while True:
        draw_frame(canvas, row, col, gameover_frame[0])
        await sleep(1)
        draw_frame(canvas, row, col, gameover_frame[0])


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


async def game(canvas):
    global year
    info_row, info_col = canvas.getmaxyx()
    info_canvas = canvas.derwin(info_row-3, info_col - 40)
    year["year"] = 1957
    while True:
        start = int(time.time())
        delay = get_garbage_delay_tics(year["year"])
        if delay:
            await sleep(delay)
            await fill_orbit_with_garbage(canvas)
        else:
            await sleep(15)
        phrase = PHRASES.get(year["year"], '')
        coroutines.append(show_game_info(info_canvas, phrase, year["year"]))
        if int(time.time()) - start >= 1:
            year["year"] += 1


async def show_game_info(info_canvas, phrase, year):
    info_row, info_col = info_canvas.getmaxyx()
    while True:
        info_canvas.addstr(0, info_col - 6, f"{year}")
        info_canvas.addstr(1, info_col - len(phrase) - 1, f"{phrase}")
        info_canvas.refresh()
        await sleep(1)
