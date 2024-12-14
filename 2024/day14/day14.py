#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
--- Day 14: Restroom Redoubt ---
https://adventofcode.com/2024/day/14

@author: AJPfleger
https://github.com/AJPfleger
"""

import re
import copy
from pathlib import Path


def parse_input(filename):
    path = Path(__file__).with_name(filename)
    file = path.open("r")
    lines = file.readlines()

    robots = []
    for line in lines:
        if line.strip() == "":
            break
        re_match = re.findall(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line)

        robot = [int(x) for x in re_match[0]]
        robots.append(robot)

    return robots


def get_safety_factor(quadrants):
    safety_factor = 1
    for i in range(4):
        safety_factor *= quadrants.count(i)

    return safety_factor


def move_robots(robots, limits, time):
    for robot in robots:
        for i in range(2):
            robot[0 + i] += robot[2 + i] * time
            robot[0 + i] %= limits[i]


def count_quadrants(robots, limits):
    quadrants = []

    limits_half = [x // 2 for x in limits]
    for robot in robots:
        pos = []
        for i in range(2):
            pos.append(robot[i] - limits_half[i])

        if any(x == 0 for x in pos):
            continue

        quad = 0
        for i in range(2):
            quad += 2 ** i if pos[i] > 0 else 0

        quadrants.append(quad)

    return quadrants


def print_positions(robots, limits):

    empty_line = ["."] * limits[0]
    lines = []
    for _ in range(limits[1]):
        lines.append(copy.deepcopy(empty_line))

    for robot in robots:
        x, y = robot[:2]
        lines[y][x] = "*"

    for line in lines:
        print("".join(line))


print("\n--- Day 13: Claw Contraption ---")

filename = "testinput.txt"

robots = parse_input(filename)

if filename == "testinput.txt":
    limits = [11, 7]
else:
    limits = [101, 103]

print("\n--- Part 1 ---")
robots = parse_input(filename)
time = 100

move_robots(robots, limits, time)
quadrants = count_quadrants(robots, limits)
safety_factor = get_safety_factor(quadrants)

print(safety_factor)

print("\n--- Part 2 ---")
# I analysed the positions and noticed, that sometimes, the output gets denser.
# One time forming a horizontal stripe, one time a vertical stripe. The stripes
# occured in a periodicity of the limits with some offset. After finding the
# offsets, I guessed, that both stripes need to happen at the same time to form
# a pattern yielding the equation:
# offset_0 + limit_0 * t_p = offset_1 + limit_1 * t_p
# with the solution for the period
# t_p = (offset_1 - offset_0) / (limit_0 - limit_1)

# Code snippet to manually find the offsets
# robots = parse_input(filename)
# offset = 200
# move_robots(robots, limits, offset)
# for t in range(offset+limits[0],100000,limits[0]):
#     move_robots(robots, limits, limits[0])
#     print_positions(robots, limits)
#     print(f"Positions after {t} s.")
#     input("Press enter to continue")

offset = [200, 40]
t_p = (offset[1] - offset[0]) // (limits[0] - limits[1])
t = offset[0] + limits[0] * t_p
robots = parse_input(filename)
move_robots(robots, limits, t)
print_positions(robots, limits)

print(f"Easteregg after {t} s")
