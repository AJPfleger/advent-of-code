#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
--- Day 1: Calorie Counting ---
https://adventofcode.com/2022/day/1

Created on Thu Dec  1 07:56:39 2022

@author: AJPfleger
https://github.com/AJPfleger
"""

from pathlib import Path


def get_cal_per_elf(filename):
    path = Path(__file__).with_name(filename)
    file = path.open("r")
    lines = file.readlines()

    cal_per_elf = [0]
    for l in lines:
        if l != "\n":
            cal_per_elf[-1] += int(l)
        else:
            cal_per_elf.append(0)

    return cal_per_elf


def get_top_cals(cal_per_elf, top_n=1):
    cal_per_elf.sort(reverse=True)

    return sum(cal_per_elf[:top_n])


print("\n--- Day 1: Calorie Counting ---")

filename = "input.txt"
cal_per_elf = get_cal_per_elf(filename)

print("\n--- Part 1 ---")
print(f"Elf with the most calories carries {get_top_cals(cal_per_elf)} calories.")

print("\n--- Part 2 ---")
top_n = 3
print(f"The {top_n} elves with the most calories carry together {get_top_cals(cal_per_elf,top_n)} calories.\n")
