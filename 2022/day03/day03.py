#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
--- Day 3: Rucksack Reorganization ---
https://adventofcode.com/2022/day/3

Created on Sat Dec  3 08:06:00 2022

@author: AJPfleger
https://github.com/AJPfleger
"""

from pathlib import Path


def parse_file(filename):
    path = Path(__file__).with_name(filename)
    file = path.open("r")
    raw_lines = file.readlines()

    lines = []
    for rl in raw_lines:
        lines.append(rl.strip())

    return lines


def match_lines(l1, l2):
    l12 = ""
    for i1 in l1:
        if i1 in l2:
            l12 += i1

    return l12


def priority_of_group(line_group):
    l_help = line_group[0]
    for l in line_group[1:]:
        l_help = match_lines(l_help, l)

    return item_to_priority(l_help[0])


def item_to_priority(item):
    priority = ord(item[0]) - 96

    if priority < 1:
        priority += 58

    return priority


def get_priorities(lines, group_size=1):
    sum_of_priorities = 0
    for i in range(0, len(lines), group_size):
        if group_size == 1:
            l = lines[i]
            half_length = int(len(l) / 2)
            line_group = [l[:half_length], l[half_length:]]
        else:
            line_group = lines[i: i + group_size]

        sum_of_priorities += priority_of_group(line_group)

    return sum_of_priorities


print("\n--- Day 3: Rucksack Reorganization ---")

filename = "input.txt"
lines = parse_file(filename)

print("\n--- Part 1 ---")
sum_of_priorities = get_priorities(lines, 1)
print(f"Sum of priorities = {sum_of_priorities}")

print("\n--- Part 2 ---")
sum_of_priorities = get_priorities(lines, 3)
print(f"Sum of priorities = {sum_of_priorities}\n")
