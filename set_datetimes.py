#!/usr/bin/env python3
import os
from pathlib import Path


def set_datetimes(datetimes_map: dict[str, int], folder: Path) -> None:
    for filename in datetimes_map:
        file = folder / filename
        os.utime(file, (datetimes_map[filename], datetimes_map[filename]))


if __name__ == '__main__':
    import json

    with open('datetimes.json', 'r') as f:
        set_datetimes(json.load(f), Path('DCIM/Camera'))
