#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
--- Day 4: Camp Cleanup ---
https://adventofcode.com/2022/day/4

Created on Sun Dec  4 08:34:02 2022

@author: AJPfleger
https://github.com/AJPfleger
"""

from pathlib import Path
import re


def get_range_pairs(filename):
    path = Path(__file__).with_name(filename)
    file = path.open("r")
    lines = file.readlines()

    range_pairs = []
    for l in lines:
        range_pairs.append(line_to_ranges(l))

    return range_pairs


def line_to_ranges(line):
    match = re.match("(\d+)-(\d+),(\d+)-(\d+)", line.strip())
    r00, r01, r10, r11 = match.groups()

    return range(int(r00), int(r01) + 1), range(int(r10), int(r11) + 1)


def count_intersects(range_pairs, mode="includes"):
    count = 0
    for rp in range_pairs:
        if intersect_ranges(rp, mode):
            count += 1

    return count


def intersect_ranges(rp, mode):
    intersect = False

    if mode == "includes":
        for i in range(2):
            if rp[(i + 1) % 2][0] in rp[i] and rp[(i + 1) % 2][-1] in rp[i]:
                intersect = True
                break

    elif mode == "overlaps":
        for i in range(2):
            if rp[(i + 1) % 2][0] in rp[i] or rp[(i + 1) % 2][-1] in rp[i]:
                intersect = True
                break
    else:
        print(f'WARNING intersect_ranges: unknown mode [{mode}]')

    return intersect


print("\n--- Day 4: Camp Cleanup ---")

filename = "input.txt"
range_pairs = get_range_pairs(filename)

print("\n--- Part 1 ---")
total_includes = count_intersects(range_pairs, "includes")
print(f"Number of includes = {total_includes}")

print("\n--- Part 2 ---")
total_overlaps = count_intersects(range_pairs, "overlaps")
print(f"Number of overlaps = {total_overlaps}\n")
