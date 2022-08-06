#!/bin/bash
cd "$(dirname "$0")" || exit

git reset --hard
git clean -f -d
rm DCIM/orig/* || true
python3 set_datetimes.py
