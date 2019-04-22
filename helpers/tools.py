import os
import asyncio


async def sleep(pause):
    for _ in range(pause):
        await asyncio.sleep(0)


def load_frames(sprites_folder):
    frames_dir = f"./sprites/{sprites_folder}"
    frames = list()
    for file in os.listdir(frames_dir):
        with open(os.path.join(frames_dir, file)) as fh:
            frame = fh.read()
            frames.append(frame)
    return frames