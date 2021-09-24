import random
from pathlib import Path
from typing import List


def get_images(directory: Path) -> List[Path]:
    return [f for f in directory.iterdir()]


def get_spooky_number(start: int, end: int) -> int:
    return random.randint(start, end)
