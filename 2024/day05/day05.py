#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
--- Day 5: Print Queue ---
https://adventofcode.com/2024/day/05

@author: AJPfleger
https://github.com/AJPfleger
"""


from pathlib import Path


def parse_input(filename):
    path = Path(__file__).with_name(filename)
    file = path.open("r")
    lines = file.readlines()

    rules = set()
    for line in lines:
        l_s = line.strip()
        if l_s == "":
            break

        rules.add(l_s)

    updates = []
    for line in lines[len(rules) + 1 :]:
        l_s = line.strip()
        if l_s == "":
            break

        updates.append(l_s.split(","))

    return rules, updates


def generate_wrong_combinations(update):
    combinations = []

    for i in range(len(update) - 1):
        for j in range(i + 1, len(update)):
            c_str = update[j] + "|" + update[i]
            combinations.append(c_str)

    return combinations


def complying(combinations, rules):
    for c in combinations:
        if c in rules:
            return False

    return True


def get_middle(lst):
    return int(lst[len(lst) // 2])


def get_middle_sum(rules, updates, fix=False):
    middle_sum = 0
    for update in updates:
        combinations = generate_wrong_combinations(update)

        if complying(combinations, rules) and not fix:
            middle_sum += get_middle(update)

        if not complying(combinations, rules) and fix:
            fixed = fix_update(update, rules)

            middle_sum += get_middle(fixed)

    return middle_sum


def fix_update(update, rules):

    update_fixed = []
    for u in update:
        for pos in range(len(update_fixed) + 1):
            update_temp = insert(update_fixed, u, pos)
            # print(update_fixed)
            combo_temp = generate_wrong_combinations(update_temp)
            # print(combo_fixed)
            if complying(combo_temp, rules):
                update_fixed = update_temp.copy()
                break

    return update_fixed


def insert(lst, item, pos):
    return lst[:pos] + [item] + lst[pos:]


print("\n--- Day 5: Print Queue ---")

filename = "input.txt"

rules, updates = parse_input(filename)

print("\n--- Part 1 ---")
print(get_middle_sum(rules, updates))

print("\n--- Part 2---")
print(get_middle_sum(rules, updates, fix=True))
