#!/bin/bash
cd "$(dirname "$0")" || exit

git reset --hard
git clean -f
rm DCIM/orig/*
