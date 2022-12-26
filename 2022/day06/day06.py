#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
--- Day 6: Tuning Trouble ---
https://adventofcode.com/2022/day/6

Created on Tue Dec  6 07:29:37 2022

@author: AJPfleger
https://github.com/AJPfleger
"""

from pathlib import Path


def get_sequence(filename):
    path = Path(__file__).with_name(filename)
    file = path.open("r")
    lines = file.readlines()

    return lines[0].strip()


def find_marker(sequence, marker_length):
    marker = [sequence[0]] * marker_length

    for s in range(len(sequence)):
        marker[s % marker_length] = sequence[s]

        if len(set(marker)) == marker_length:
            return s + 1


print("\n--- Day 6: Tuning Trouble ---")

filename = "input.txt"
sequence = get_sequence(filename)

print("\n--- Part 1 ---")
chars = find_marker(sequence, 4)
print(f"Characters to process = {chars}")

print("\n--- Part 2 ---")
chars = find_marker(sequence, 14)
print(f"Characters to process = {chars}\n")
