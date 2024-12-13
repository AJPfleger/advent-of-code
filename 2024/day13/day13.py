#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
--- Day 13: Claw Contraption ---
https://adventofcode.com/2024/day/13

@author: AJPfleger
https://github.com/AJPfleger
"""

import re

from pathlib import Path


def parse_input(filename):
    path = Path(__file__).with_name(filename)
    file = path.open("r")
    lines = file.readlines()

    machines = []
    temp_machines = []
    for line in lines:
        re_match = re.findall(r".*: X.(\d+), Y.(\d+)", line)

        if re_match == []:
            machines.append(temp_machines)
            temp_machines = []
        else:
            sub_info = [int(x) for x in re_match[0]]
            temp_machines.append(sub_info)

    return machines


def get_cost(machine, push_limit=True, conversion=False):
    cost_a = 3
    cost_b = 1

    xa, ya = machine[0]
    xb, yb = machine[1]
    X, Y = machine[2]

    # We need to solve the equation system:
    # [ xa  xb ]   [ a ]   [ X ]
    # [ ya  yb ] * [ b ] = [ Y ]

    if conversion:
        offset = 10000000000000
        X += offset
        Y += offset

    det = xa * yb - xb * ya
    assert det != 0, "system is not solvable"

    a = (yb * X - xb * Y) / det
    b = (-ya * X + xa * Y) / det

    for val in [a, b]:
        if not validate(val, push_limit):
            return 0

    return int(a) * cost_a + int(b) * cost_b


def validate(val, push_limit):
    valid = val <= 100 if push_limit else True
    valid = valid and val.is_integer()
    valid = valid and 0 <= val
    return valid


print("\n--- Day 13: Claw Contraption ---")

filename = "input.txt"

machines = parse_input(filename)

print("\n--- Part 1 ---")
total_cost = 0
for machine in machines:
    total_cost += get_cost(machine)

print(total_cost)

print("\n--- Part 1 ---")
total_cost = 0
for machine in machines:
    total_cost += get_cost(machine, push_limit=False, conversion=True)

print(total_cost)
