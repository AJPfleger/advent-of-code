#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
--- Day 25: Code Chronicle ---
https://adventofcode.com/2024/day/25

@author: AJPfleger
https://github.com/AJPfleger
"""


from pathlib import Path


def parse_input(filename):
    path = Path(__file__).with_name(filename)
    file = path.open("r")
    lines = file.readlines()

    keys = []
    locks = []
    kind = "x"
    # pattern = []
    for line in lines:
        line = line.strip()
        if line == "":
            assert kind != "x", "wrong type"

            pattern.append(sum(pattern))
            if kind == "k":
                keys.append(pattern)
            else:
                locks.append(pattern)

            kind = "x"
            continue

        if kind == "x":
            kind = "k" if "#" in line else "l"
            pattern = [-1] * len(line)

        for i, c in enumerate(line):
            if c == "#":
                pattern[i] += 1

    return keys, locks


print("\n--- Day 25: Code Chronicle ---")

filename = "testinput.txt"

keys, locks = parse_input(filename)

print("\n--- Part 1 ---")

fits = len(keys) * len(locks)
for l in locks:
    for k in keys:
        for i in reversed(range(len(k))):
            if i == 5:
                if l[i] + k[i] > 25:
                    fits -= 1
                    break
            elif l[i] + k[i] > 5:
                fits -= 1
                break


print(fits)
