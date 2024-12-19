#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
--- Day 6: Guard Gallivant ---
https://adventofcode.com/2024/day/06

@author: AJPfleger
https://github.com/AJPfleger
"""


from pathlib import Path


def parse_input(filename):
    path = Path(__file__).with_name(filename)
    file = path.open("r")
    lines = file.readlines()

    paradox = set()
    for y, line in enumerate(lines):
        # if line.strip() == "":
        #     break

        for x, c in enumerate(line.strip()):
            if c == ".":
                continue

            position = (x, y)

            if c == "#":
                paradox.add(position)
            else:
                guard = [(x, y), c]

    return paradox, guard, (x, y)


def get_direction(c):
    if c == ">":
        return (1, 0)
    elif c == "v":
        return (0, 1)
    elif c == "<":
        return (-1, 0)
    elif c == "^":
        return (0, -1)
    else:
        assert False, f"Illegal movement '{c}'"


def get_new_position(position, direction):
    return tuple(sum(x) for x in zip(position, get_direction(direction)))


def simulate(paradox, original_guard, limits, visited, visit_dir=False):
    guard = original_guard.copy()

    if visit_dir:
        visited.add(tuple(guard))
    else:
        visited.add(guard[0])
    while True:
        update_guard(guard, paradox)

        if outside(guard, limits):
            return False
        elif tuple(guard) in visited:
            return True

        if visit_dir:
            visited.add(tuple(guard))
        else:
            visited.add(guard[0])


def update_guard(guard, paradox):
    pos, dir = guard

    new_pos = get_new_position(pos, dir)

    if new_pos in paradox:
        guard[1] = rotate(dir)
    else:
        guard[0] = new_pos


def rotate(dir):
    all_dir = [">", "v", "<", "^"]
    idx = all_dir.index(dir)
    return all_dir[(idx + 1) % len(all_dir)]


def outside(guard, limits):
    pos = guard[0]
    inside = True
    for p, l in zip(pos, limits):
        inside &= 0 <= p < l

    return not inside


def obstruct(paradox, guard, limits, visited):
    visited.remove(guard[0])
    count_paradox = 0
    for new_paradox in visited:
        paradox.add(new_paradox)
        visited_temp = set()
        if simulate(paradox, guard, limits, visited_temp, visit_dir=True):
            count_paradox += 1

        paradox.remove(new_paradox)

    return count_paradox


print("\n--- Day 6: Guard Gallivant ---")

filename = "testinput.txt"

paradox, guard, limits = parse_input(filename)

print("\n--- Part 1 ---")
visited = set()
simulate(paradox, guard, limits, visited)

print(len(visited))


print("\n--- Part 2 ---")
count_paradox = obstruct(paradox, guard, limits, visited)
print(count_paradox)
