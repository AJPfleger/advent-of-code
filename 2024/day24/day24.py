#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
--- Day 24: Crossed Wires ---
https://adventofcode.com/2024/day/24

@author: AJPfleger
https://github.com/AJPfleger
"""

import re
import operator

from pathlib import Path


def parse_input(filename):
    path = Path(__file__).with_name(filename)
    file = path.open("r")
    lines = file.readlines()

    wires = {}
    for line in lines:
        if line.strip() == "":
            break
        w, bit = re.findall(r"(...): (.)", line.strip())[0]
        wires[w] = int(bit)

    gates = []
    for line in lines[len(wires) + 1 :]:
        if line.strip() == "":
            break

        re_match = re.findall(r"(.*) (.*) (.*) -> (.*)", line.strip())[0]
        gates.append(list(re_match))

        # wires.append(int(val))
    return wires, gates


def simulate(wires, gates_original):
    gates = gates_original.copy()
    for _ in range(len(gates)):
        for i in reversed(range(len(gates))):
            w1, op, w2, w3 = gates[i]

            if w1 in wires and w2 in wires:
                wires[w3] = op_dict[op](wires[w1], wires[w2])
                gates.pop(i)

        if len(gates) == 0:
            break


def get_value(wires, w_type="z"):
    rev_string = [0] * 100
    for w, bit in wires.items():
        if w[0] == w_type:
            rev_string[int(w[1:])] = bit

    final_string = ""
    for b in reversed(rev_string):
        final_string += str(b)

    return int(final_string, 2)


print("\n--- Day 24: Crossed Wires ---")

filename = "testinput.txt"

wires_raw, gates = parse_input(filename)

op_dict = {"AND": operator.and_, "OR": operator.or_, "XOR": operator.xor}

print("\n--- Part 1 ---")

wires = wires_raw.copy()
simulate(wires, gates)

z = get_value(wires, "z")

print(z)


print("\n--- Part 2 ---")

x = get_value(wires, "x")
y = get_value(wires, "y")


# Just brute-forcing is not an option since there are too many options:
# (220 binomial 8) ways to choose faulty wires.
# (8 binomial 2) * (6 binomial 2) * (4 binomial 2) * (2 binomial 2) to choose
# from each 8-set.
# In total we get around 3e17 combinations
