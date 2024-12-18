#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
--- Day 18: RAM Run ---
https://adventofcode.com/2024/day/18

@author: AJPfleger
https://github.com/AJPfleger
"""


from pathlib import Path


def parse_input(filename):
    path = Path(__file__).with_name(filename)
    file = path.open("r")
    lines = file.readlines()

    walls = []
    for line in lines:
        coordinates = line.strip().split(",")
        if coordinates == [""]:
            break
        walls.append(tuple([int(x) for x in coordinates]))

    return walls


def get_candidates(current_position, grid_size):
    candidates = set()

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for c in current_position:
        for d in directions:
            cand = tuple([sum(x) for x in zip(c, d)])
            if valid_candidate(cand, grid_size):
                candidates.add(cand)

    return candidates


def valid_candidate(candidate, grid_size):
    for c in candidate:
        if not (0 <= c < grid_size):
            return False

    return True


def shortest_path(all_walls, cut_off, grid_size):
    walls = set(all_walls[:cut_off])
    current_position = {(0, 0)}
    visited = set()
    end_point = (grid_size - 1, grid_size - 1)
    for step in range(grid_size**2):
        candidates = get_candidates(current_position, grid_size)
        if end_point in candidates:
            break

        visited.update(current_position)
        current_position = set()

        for c in candidates:
            if c in visited or c in walls:
                continue

            current_position.add(c)

    return step + 1


print("\n--- Day 18: RAM Run ---")

filename = "testinput.txt"

if filename == "testinput.txt":
    grid_size = 7
    cut_off = 12
else:
    grid_size = 71
    cut_off = 1024

all_walls = parse_input(filename)

print("\n--- Part 1 ---")

steps = shortest_path(all_walls, cut_off, grid_size)
print(steps)

print("\n--- Part 2 ---")

blocking_piece = []
for w in range(1024, len(all_walls)):
    steps = shortest_path(all_walls, w + 1, grid_size)

    if steps == grid_size**2:
        blocking_piece = all_walls[w]
        break

print(blocking_piece)
