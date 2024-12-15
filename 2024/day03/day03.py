#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
--- Day 3: Mull It Over ---
https://adventofcode.com/2024/day/03

@author: AJPfleger
https://github.com/AJPfleger
"""

import re

from pathlib import Path


def parse_input(filename, skip_do=True):
    path = Path(__file__).with_name(filename)
    file = path.open("r")
    lines = file.readlines()

    mul = []
    do_it = True
    for line in lines:
        re_match = re.findall(r"(mul\(\d+,\d+\)|do\(\)|don\'t\(\))", line)

        for match in re_match:
            if match == "do()":
                do_it = True
            elif match == "don't()":
                do_it = False
            elif skip_do or do_it:
                re_match_ints = re.findall(r"mul\((\d+),(\d+)\)", match)
                mul.append([int(x) for x in re_match_ints[0]])

    return mul


def sum_mul(mul):
    return sum([a * b for a, b in mul])


print("\n--- Day 3: Mull It Over ---")

filename = "input.txt"

print("\n--- Part 1 ---")
mul = parse_input(filename)
print(sum_mul(mul))

print("\n--- Part 2 ---")
mul = parse_input(filename, skip_do=False)
print(sum_mul(mul))
