#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
--- Day 4: Ceres Search ---
https://adventofcode.com/2024/day/4

@author: AJPfleger
https://github.com/AJPfleger
"""

import re

from pathlib import Path


def parse_input(filename):
    path = Path(__file__).with_name(filename)
    file = path.open("r")
    lines = file.readlines()

    parsed_lines = []
    for line in lines:
        parsed_lines.append(line.strip())

    return parsed_lines


def count_in_string(string):
    fwd = len(re.findall("XMAS", string))
    bwd = len(re.findall("SAMX", string))
    return fwd + bwd


def count_in_block(block):
    return sum([count_in_string(line) for line in block])


def rotate_45_degrees(block):
    n_row = len(block)
    n_col = len(block[0])

    block_tmp = [""] * (n_row + n_col - 1)

    for r, row in enumerate(block):
        for c in range(len(row)):
            block_tmp[c + r] += row[c]

    return block_tmp


def rotate_90_degrees(block):
    block_tmp = [""] * len(block[0])

    for row in block:
        for c in range(len(row)):
            block_tmp[c] = row[c] + block_tmp[c]

    return block_tmp


def check_in_cross(sub_block):
    if sub_block[1][1] is not "A":
        return False

    string = sub_block[0][0]
    string += sub_block[0][2]
    string += sub_block[2][2]
    string += sub_block[2][0]
    string += sub_block[0][0]

    return bool(re.match(r".*MM.*", string)) and bool(re.match(r".*SS.*", string))


def count_all_sub_blocks(block):
    n_row = len(block)
    n_col = len(block[0])

    sub_block = [""] * 3
    count = 0
    for r in range(n_row - 2):
        for c in range(n_col - 2):
            for i in range(3):
                sub_block[i] = block[r + i][c : c + 3]
            count += check_in_cross(sub_block)

    return count


print("\n--- Day 4: Ceres Search ---")

filename = "testinput.txt"

print("\n--- Part 1 ---")
block = parse_input(filename)
block_90 = rotate_90_degrees(block)

count = 0
count += count_in_block(block)
count += count_in_block(rotate_45_degrees(block))
count += count_in_block(block_90)
count += count_in_block(rotate_45_degrees(block_90))

print(count)


print("\n--- Part 2 ---")

print(count_all_sub_blocks(block))
