#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
--- Day 2: Red-Nosed Reports ---
https://adventofcode.com/2024/day/2

@author: AJPfleger
https://github.com/AJPfleger
"""

from pathlib import Path


def parse_input(filename):
    path = Path(__file__).with_name(filename)
    file = path.open("r")
    lines = file.readlines()

    parsed_lines = []
    for line in lines:
        parsed_line = [int(x) for x in line.split()]
        parsed_lines.append(parsed_line)

    return parsed_lines


def check_list(raw_list):
    diffs = [a - b for a, b in zip(raw_list[:-1], raw_list[1:])]

    min_diffs = min(diffs)
    max_diffs = max(diffs)

    return min_diffs * max_diffs > 0 and abs(min_diffs) <= 3 and abs(max_diffs) <= 3


def check_with_damping(raw_list):
    if check_list(raw_list):
        return True

    for i in range(len(raw_list)):
        reduced_list = raw_list.copy()
        reduced_list.pop(i)

        if check_list(reduced_list):
            return True

    return False


print("\n--- Day 2: Red-Nosed Reports ---")

filename = "testinput.txt"

parsed_lines = parse_input(filename)

print("\n--- Part 1 ---")
res_part_1 = sum([check_list(p) for p in parsed_lines])
print(res_part_1)

print("\n--- Part 2 ---")
res_part_2 = sum([check_with_damping(p) for p in parsed_lines])
print(res_part_2)
