#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
--- Day 2: Rock Paper Scissors ---
https://adventofcode.com/2022/day/2

Created on Fri Dec  2 07:16:48 2022

@author: AJPfleger
https://github.com/AJPfleger
"""

from pathlib import Path


def play(lines, mode="normal"):

    total_score = 0
    for i in range(len(lines)):
        p1 = ord(lines[i][0]) - 65  # player1
        if mode == "normal":
            p2 = ord(lines[i][2]) - 88  # player2
            res = (p2 - p1 + 1) % 3
        elif mode == "inverse":
            res = ord(lines[i][2]) - 88  # expected result 0/1/2
            p2 = (p1 + res - 1) % 3
        else:
            p2 = 0
            res = 0
            print(f"ERROR play: unknow mode [{mode}]")

        total_score += (p2 + 1) + 3 * res

    return total_score


print("\n--- Day 2: Rock Paper Scissors ---")

filename = "input.txt"
path = Path(__file__).with_name(filename)
file = path.open("r")
lines = file.readlines()


print("\n--- Part 1 ---")
total_score = play(lines, "normal")
print(f"Expected Score = {total_score}")

print("\n--- Part 2 ---")
total_score = play(lines, "inverse")
print(f"Expected Score (Inverse) = {total_score}\n")
