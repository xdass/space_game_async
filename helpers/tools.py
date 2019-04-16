import asyncio


async def sleep(pause):
    for _ in range(pause):
        await asyncio.sleep(0)


def load_ship_frames():
    with open("./sprites/rocket_frame_1.txt") as fh:
        frame_1 = fh.read()

    with open("./sprites/rocket_frame_2.txt") as fh:
        frame_2 = fh.read()

    return frame_1, frame_2