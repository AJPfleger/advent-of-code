#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
--- Day 5: Supply Stacks ---
https://adventofcode.com/2022/day/5

Created on Mon Dec  5 07:21:35 2022

@author: AJPfleger
https://github.com/AJPfleger
"""

from pathlib import Path
import re


def generate_storage(lines):
    sep = lines.index("\n")
    max_stacks = int(lines[sep - 1][-3])
    storage = [[] for _ in range(max_stacks)]

    for h in reversed(range(sep - 1)):
        for s in range(max_stacks):
            crate = lines[h][s * 4 + 1]
            if crate != " ":
                (storage[s]).append(crate)

    return storage


def move_crates(storage, instructions, crane="9000"):
    [n_max, start, end] = instructions
    order = -1
    for n in range(n_max):
        if crane == "9001":
            order = n - n_max
        storage[end - 1].append(storage[start - 1].pop(order))

    return storage


def simulate_instructions(storage, lines, crane="9000"):
    sep = lines.index("\n")

    for i in range(sep + 1, len(lines)):
        instructions = parse_move(lines[i])
        storage = move_crates(storage, instructions, crane)

    return storage


def parse_move(line):
    match = re.match("move (\d+) from (\d+) to (\d+)", line.strip())
    n_max, start, end = match.groups()

    return int(n_max), int(start), int(end)


def get_message(storage):
    message = ""
    for s in storage:
        message += s[-1]

    return message


print("\n--- Day 5: Supply Stacks ---")

filename = "input.txt"
path = Path(__file__).with_name(filename)
file = path.open("r")
lines = file.readlines()

print("\n--- Part 1 ---")
storage = generate_storage(lines)
storage = simulate_instructions(storage, lines, "9000")
message = get_message(storage)
print(f"Message = {message}")

print("\n--- Part 2 ---")
storage = generate_storage(lines)
storage = simulate_instructions(storage, lines, "9001")
message = get_message(storage)
print(f"Message = {message}\n")
