#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
--- Day 9: Disk Fragmenter ---
https://adventofcode.com/2024/day/9

@author: AJPfleger
https://github.com/AJPfleger
"""

# import re

from pathlib import Path


def parse_input(filename):
    path = Path(__file__).with_name(filename)
    file = path.open("r")
    string = file.readlines()[0].strip()

    return string


def parse_string(string):
    disk = []

    for num in string:
        # print(f"{i}: {num}")
        disk.append(int(num))

    return disk


def truncate_disk(disk):
    while disk[-1] == 0:
        disk.pop()
        disk.pop()

    return disk


def check_rearranged(disk, space_full):
    disk_back_up = disk.copy()
    pos = 0
    check_sum = 0
    for [s, section] in enumerate(disk):
        if s % 2 == 0:
            for i in range(section):
                check_sum += pos * int(s / 2)
                pos += 1
                # print(f"{pos}:\t{check_sum}")
                if pos == space_full:
                    break
        else:
            # handle holes
            for i in range(section):
                check_sum += pos * int((len(disk_back_up) - 1) / 2)
                pos += 1
                disk_back_up[-1] -= 1
                disk_back_up = truncate_disk(disk_back_up)
                # print(f"{pos}:\t{check_sum}")
                if pos == space_full:
                    break
        if pos == space_full:
            return check_sum


print("\n--- Day 9: Disk Fragmenter ---")

filename = "testinput.txt"

print("\n--- Part 1 ---")
string = parse_input(filename)

disk = parse_string(string)
space_full = sum(disk[0::2])
# space_empty = sum(disk[1::2])
# space_total = space_full + space_empty
# print(f"{space_full} + {space_empty} = {space_total}")
#
check_sum = check_rearranged(disk, space_full)
print(check_sum)


print("\n--- Part 2 ---")
check_sum_defrag = check_defragment(disk, space_full)
print(check_sum_defrag)
