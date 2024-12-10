#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
--- Day 10: Hoof It ---
https://adventofcode.com/2024/day/10

@author: AJPfleger
https://github.com/AJPfleger
"""

# import re
import copy

from pathlib import Path


def parse_input(filename):
    path = Path(__file__).with_name(filename)
    file = path.open("r")
    lines = file.readlines()

    raw_map = []
    for line in lines:
        row = [int(x) for x in line.strip()]
        if len(row) == 0:
            continue
        raw_map.append(row)

    return raw_map


def expand_map(raw_map):
    empty_line = [-2] * (len(raw_map[0]) + 2)
    large_map = []
    large_map.append(empty_line)

    for row in raw_map:
        tmp_row = [-2]
        [tmp_row.append(x) for x in row]
        tmp_row.append(-2)

        large_map.append(tmp_row)
    large_map.append(empty_line)

    return large_map


def print_map(example_map):
    for row in example_map:
        s = ""
        for pos in row:
            s += str(pos) if pos >= 0 else "."
        print(s)


def diff_one(a, b, sign=1):
    return a == b + sign


def clean_neighbours(my_map, sign=1):
    n_rows = len(my_map)
    n_cols = len(my_map[0])

    for c in range(1, n_cols - 1):
        for r in range(1, n_rows - 1):
            val = my_map[r][c]
            if not 0 < val <= 9:
                continue
            if (
                diff_one(val, my_map[r - 1][c], sign)
                or diff_one(val, my_map[r + 1][c], sign)
                or diff_one(val, my_map[r][c - 1], sign)
                or diff_one(val, my_map[r][c + 1], sign)
            ):
                continue

            my_map[r][c] = -2

    return my_map


def count_peaks(my_map):
    n_rows = len(my_map)
    n_cols = len(my_map[0])

    peak_count = 0
    print_map(my_map)
    for c in range(1, n_cols - 1):
        for r in range(1, n_rows - 1):
            val = my_map[r][c]
            # print(val)
            if val != 0:
                continue

            tmp_map = copy.deepcopy(my_map)
            tmp_map = overwrite_zeros(tmp_map)
            tmp_map[r][c] = 0

            for _ in range(100):
                tmp_map = clean_neighbours(tmp_map)

            # print_map(tmp_map)
            # print_map(my_map)

            peak_count += count_occurance(tmp_map, 9)
    return peak_count


def count_occurance(my_map, val=9):
    return sum([row.count(val) for row in my_map])


def overwrite_zeros(my_map):
    n_rows = len(my_map)
    n_cols = len(my_map[0])

    for c in range(1, n_cols - 1):
        for r in range(1, n_rows - 1):
            val = my_map[r][c]
            if val == 0:
                my_map[r][c] = -2

    return my_map


print("\n--- Day 10: Hoof It ---")

filename = "testinput.txt"

print("\n--- Part 1 ---")
raw_map = parse_input(filename)
print_map(raw_map)
updated_map = expand_map(raw_map)

# pre-clean
for _ in range(100):
    updated_map = clean_neighbours(updated_map)
    # print_map(updated_map)

sum_peaks = count_peaks(updated_map)
print(sum_peaks)
