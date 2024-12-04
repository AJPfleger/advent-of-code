#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
--- Day 1: Historian Hysteria ---
https://adventofcode.com/2024/day/1

@author: AJPfleger
https://github.com/AJPfleger
"""

from pathlib import Path


def parse_input(filename):
    path = Path(__file__).with_name(filename)
    file = path.open("r")
    lines = file.readlines()

    list_1 = []
    list_2 = []
    for line in lines:
        [a, b] = line.split()
        list_1.append(int(a))
        list_2.append(int(b))

    return list_1, list_2


print("\n--- Day 1: Historian Hysteria ---")

filename = "testinput.txt"

[list_1, list_2] = parse_input(filename)

list_1.sort()
list_2.sort()

print("\n--- Part 1 ---")
res_part_1 = sum([abs(a - b) for a, b in zip(list_1, list_2)])
print(res_part_1)

print("\n--- Part 2 ---")
res_part_2 = sum([x * list_2.count(x) for x in list_1])
print(res_part_2)
