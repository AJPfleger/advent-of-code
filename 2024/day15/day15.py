#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
--- Day 15: Warehouse Woes ---
https://adventofcode.com/2024/day/15

@author: AJPfleger
https://github.com/AJPfleger
"""


from pathlib import Path


def parse_input(filename):
    path = Path(__file__).with_name(filename)
    file = path.open("r")
    lines = file.readlines()

    ware_house = {}
    for y, line in enumerate(lines):
        if line.strip() == "":
            break

        for x, c in enumerate(line.strip()):
            if c == ".":
                continue

            position = (x, y)

            if c == "@":
                robot = position
            else:
                ware_house[position] = c

    moves = ""
    for line in lines[y:]:
        moves += line.strip()

    return ware_house, robot, moves


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
    return tuple(sum(x) for x in zip(position, direction))


def try_move(crate, ware_house, direction):
    new_position = get_new_position(crate, direction)

    if new_position in ware_house:
        if ware_house[new_position] == "#":
            return False
        elif not try_move(new_position, ware_house, direction):
            return False

    ware_house[new_position] = "O"
    ware_house.pop(crate)

    return True


def simulate(ware_house, robot, moves):
    for c in moves:
        direction = get_direction(c)

        proposed_robot = get_new_position(robot, direction)

        if proposed_robot not in ware_house:
            robot = proposed_robot
        elif ware_house[proposed_robot] == "#":
            continue
        elif try_move(proposed_robot, ware_house, direction):
            robot = proposed_robot


def get_gps_sum(ware_house):
    gps_sum = 0
    for position, thing in ware_house.items():
        if thing == "#":
            continue

        gps_sum += position[0]
        gps_sum += position[1] * 100

    return gps_sum


print("\n--- Day 15: Warehouse Woes ---")

filename = "testinput.txt"

print("\n--- Part 1 ---")
ware_house, robot, moves = parse_input(filename)
simulate(ware_house, robot, moves)
gps_sum = get_gps_sum(ware_house)
print(gps_sum)
