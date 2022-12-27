#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
--- Day 9: Rope Bridge ---
https://adventofcode.com/2022/day/9

Created on Fri Dec  9 07:15:30 2022

@author: AJPfleger
https://github.com/AJPfleger
"""

from pathlib import Path


def get_series_of_motions(filename):
    path = Path(__file__).with_name(filename)
    file = path.open("r")
    lines = file.readlines()

    som = []
    for l in lines:
        direction = l[0]
        steps = int(l[2:-1])
        som.append([direction, steps])

    return som


def simulate_rope(series_of_motions, knots=2):
    rope = [[0, 0] for _ in range(knots)]
    visited = {str(rope[-1]): ""}

    for direction, steps in series_of_motions:
        for _ in range(steps):
            rope[0] = move_H(rope[0], direction)
            for k in range(knots - 1):
                rope[k + 1] = move_T(rope[k], rope[k + 1])
            visited.update({str(rope[-1]): ""})

    return len(visited)


def move_H(H, direction):
    if direction == "R":
        H[1] += 1
    elif direction == "L":
        H[1] -= 1
    elif direction == "U":
        H[0] += 1
    elif direction == "D":
        H[0] -= 1

    return H


def move_T(H, T):
    if not_touching(H, T):
        for i in range(len(H)):
            delta = H[i] - T[i]
            if delta != 0:
                T[i] += int(delta / abs(delta))

    return T


def not_touching(H, T):
    cond = False
    if abs(H[0] - T[0]) > 1 or abs(H[1] - T[1]) > 1:
        cond = True

    return cond


print("\n--- Day 9: Rope Bridge ---")

filename = "input.txt"
series_of_motions = get_series_of_motions(filename)

print("\n--- Part 1 ---")
visited = simulate_rope(series_of_motions)
print(f"Visited positions = {visited}")

print("\n--- Part 2 ---")
visited = simulate_rope(series_of_motions, 10)
print(f"Visited positions = {visited}\n")
