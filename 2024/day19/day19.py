#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
--- Day 19: Linen Layout ---
https://adventofcode.com/2024/day/19

@author: AJPfleger
https://github.com/AJPfleger
"""

import functools

from pathlib import Path


def parse_input(filename):
    path = Path(__file__).with_name(filename)
    file = path.open("r")
    lines = file.readlines()

    patterns = lines[0].strip().split(", ")

    designs = []
    for line in lines[2:]:
        designs.append(line.strip())

    if designs[-1] == "":
        designs.pop()

    return frozenset(patterns), designs


def reduce_patterns(patterns):
    """
    This is not relevant anymore but kept, since it was a cute function.
    We only want to keep a minimal set of patterns. The reduced pattern set is
    a orthonormal basis of all patterns.
    """

    p_set = set(patterns)
    p_set.add("")  # empty string to start with
    possible_lengths = set(len(p) for p in p_set)
    possible_lengths = sorted(possible_lengths)

    min_pat_set = set()

    for p in p_set:
        if len(p) == 1:
            min_pat_set.add(p)

    red_pat = set()
    for length in possible_lengths:
        p_set_it = p_set.copy()
        for p in p_set_it:
            if len(p) == length:
                red_pat.add(p)
                p_set.remove(p)

        all_set = all_combinations(red_pat)

        for a in all_set:
            p_set.discard(a)

    red_pat.remove("")
    return red_pat


def all_combinations(p_set):
    all_set = p_set.copy()

    for p in p_set:
        for q in p_set:
            all_set.add(p + q)
            all_set.add(q + p)

    return all_set


@functools.lru_cache(maxsize=1000000)
def reco_match(design, p_set, filter_possible):
    if design == "":
        return 1

    count = 0
    for p in p_set:
        if design.startswith(p):
            design_red = design.replace(p, "", 1)
            branches = reco_match(design_red, p_set, filter_possible)
            count += branches
            if filter_possible and branches > 0:
                break

    return count


def count_possible(patterns, designs, filter_possible=True):
    count = 0
    for d in designs:
        count += reco_match(d, patterns, filter_possible)

    return count


print("\n--- Day 19: Linen Layout ---")

filename = "input.txt"

patterns, designs = parse_input(filename)

print("\n--- Part 1 ---")

print(count_possible(patterns, designs))

print("\n--- Part 2 ---")

print(count_possible(patterns, designs, filter_possible=False))
