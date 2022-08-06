#!/usr/bin/env python3
import os

if __name__ == '__main__':
    import json

    with open('datetimes.json', 'r') as f:
        dates_map = json.load(f)
        for filename in dates_map:
            try:
                os.utime(filename, (dates_map[filename], dates_map[filename]))
            except FileNotFoundError:
                pass  # Not all files are necessary there when cleaning
