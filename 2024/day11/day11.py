#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
--- Day 11: Plutonian Pebbles ---
https://adventofcode.com/2024/day/11

@author: AJPfleger
https://github.com/AJPfleger
"""

import functools

# import math

from pathlib import Path


def parse_input(filename):
    path = Path(__file__).with_name(filename)
    file = path.open("r")
    line = file.readlines()[0]

    return [int(x) for x in line.split()]


@functools.lru_cache(maxsize=1000000)
def count_split(val, blinks):
    if blinks == 0:
        return 1
    elif val == 0:
        return count_split(1, blinks - 1)
    elif val == 1:
        return count_split(2024, blinks - 1)

    # n_digits = int(math.ceil(math.log10(val)))
    val_str = str(val)
    n_digits = len(val_str)
    if n_digits % 2 == 0:
        # print(f"even case with {n_digits} digits for {val}")
        # center = int(10 ** (n_digits / 2))
        # left = int(val / center)
        # right = int(val % center)

        # the weird string approach is encessary because we have a too long
        # number inside, that somehow messes up everything
        mid = int(n_digits / 2)
        left = int(val_str[:mid])
        right = int(val_str[mid:])
        return count_split(left, blinks - 1) + count_split(right, blinks - 1)
    else:
        return count_split(val * 2024, blinks - 1)


def simulate_stones(stones, blinks):
    n_stones = 0
    for val in stones:
        n_stones += count_split(val, blinks)

    return n_stones


print("\n--- Day 11: Plutonian Pebbles ---")

filename = "testinput.txt"

stones = parse_input(filename)

print("\n--- Part 1 ---")
blinks = 25
n_stones = simulate_stones(stones, blinks)
print(n_stones)

print("\n--- Part 2 ---")
blinks = 75
n_stones = simulate_stones(stones, blinks)
print(n_stones)
