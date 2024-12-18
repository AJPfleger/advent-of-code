#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
--- Day 17: Chronospatial Computer ---
https://adventofcode.com/2024/day/17

@author: AJPfleger
https://github.com/AJPfleger
"""

import re
import random

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
            register[0] //= 2**combo
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


def run_program(register, program):
    position = 0
    max_position = len(program)

    out = []
    for _ in range(100000):
        position = do_instruction(register, program, position, out)
        if position >= max_position:
            break
    return out


def format_output(out):
    out_string = ""
    for x in out:
        out_string += str(x)
        out_string += ","
    return out_string[:-1]


# A reversed engineered version of the real input. We have some branching which
# we use by a classy random choice.
def random_walk():
    A = 0
    for p in reversed(program):
        # print(p)
        p6 = p ^ 6
        R_possible = []
        for R in range(8):
            A_try = A * 8 + R
            B = R ^ 1

            if p6 == B ^ ((A_try // (2**B)) % 8):
                R_possible.append(R)
        if R_possible == []:
            return
        R_rand = random.choice(R_possible)
        A = A * 8 + R_rand
    return A


print("\n--- Day 17: Chronospatial Computer ---")

filename = "input.txt"

print("\n--- Part 1 ---")

register, program = parse_input(filename)

out = run_program(register, program)

print(format_output(out))

print("\n--- Part 2---")
# Important to notice is, that all our programs end with (3, 0). And have no
# other (3, x) operations inside. This means, that we repeat the programs,
# until we reach the end with A = 0. This makes it possible, to unroll the
# programs from the end and do reverted operations. Since we are looking for
# the smallest integer A we have enough constraints to do it (hopefully).
# Worst case, we branch 8 times in each step.

A_rand = set()
for _ in range(10000):
    val = random_walk()
    if val:
        A_rand.add(val)

A = min(A_rand)

register, program = parse_input(filename)
register[0] = A
out = run_program(register, program)
if out == program:
    print(A)
else:
    print("couldn't find a valid value for A")
