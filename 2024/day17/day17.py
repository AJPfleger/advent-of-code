#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
--- Day 17: Chronospatial Computer ---
https://adventofcode.com/2024/day/17

@author: AJPfleger
https://github.com/AJPfleger
"""

import re

from pathlib import Path


def parse_input(filename):
    path = Path(__file__).with_name(filename)
    file = path.open("r")
    lines = file.readlines()

    register = []
    for line in lines:
        re_match = re.findall(r".*: (\d+)", line)

        if re_match == []:
            break

        register.append(int(re_match[0]))

    program_line = lines[4].strip()[9:]
    program = [int(x) for x in program_line.split(",")]

    return register, program


def get_combo(register, operand):
    assert operand != 7, "reserverd operand in combo"
    assert 0 <= operand < 7, "operand in combo must be 3 bit"
    combo = [0, 1, 2, 3] + register
    return combo[operand]


def do_instruction(register, program, position, out):
    instruction = program[position]
    combo_operand = program[position + 1]
    combo = get_combo(register, combo_operand)

    position += 2

    match instruction:
        case 0:  # adv
            register[0] //= 2**combo  # maybe math.trunc()
            # print(register)
        case 1:  # bxl
            register[1] ^= combo_operand
        case 2:  # bst
            register[1] = combo % 8
        case 3:  # jnz
            if register[0] != 0:
                position = combo_operand
        case 4:  # bxc
            register[1] ^= register[2]
        case 5:  # out
            out.append(combo % 8)
        case 6:  # bdv
            register[1] = register[0] // (2**combo)
        case 7:  # cdv
            register[2] = register[0] // (2**combo)

    return position


print("\n--- Day 17: Chronospatial Computer ---")

filename = "input.txt"

register, program = parse_input(filename)

print(register)
print(program)
position = 0
max_position = len(program)

print("\n--- Part 1 ---")
out = []
for _ in range(100):
    # print(position)
    position = do_instruction(register, program, position, out)
    if position >= max_position:
        break

print(f"out: {out}")
