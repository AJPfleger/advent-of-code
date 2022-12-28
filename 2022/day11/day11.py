#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
--- Day 11: Monkey in the Middle ---
https://adventofcode.com/2022/day/11

Created on Sun Dec 11 08:05:00 2022

@author: AJPfleger
https://github.com/AJPfleger
"""

from pathlib import Path


class Monkey:
    def __init__(self, start_item, monkey_properties):
        self.start_item = start_item
        self.div = []
        self.mods = []
        for mp in monkey_properties:
            self.div.append(mp[2])
            self.mods.append(start_item % mp[2])

    def update_modulos(self):
        for d in range(len(self.div)):
            self.mods[d] = self.mods[d] % self.div[d]

    def __mod__(self, integer):
        return self.mods[self.div.index(integer)]

    def __add__(self, integer):
        for d in range(len(self.div)):
            self.mods[d] += integer
        self.update_modulos()
        return self

    def __mul__(self, integer):
        if isinstance(integer, self.__class__):
            for d in range(len(self.div)):
                self.mods[d] *= self.mods[d]
        else:
            for d in range(len(self.div)):
                self.mods[d] *= integer
        self.update_modulos()
        return self


def get_input(filename):
    path = Path(__file__).with_name(filename)
    file = path.open("r")
    lines = file.readlines()

    monkeys_start = []
    properties = []
    for m in range(0, len(lines), 7):
        starting_items, prop = parse_monkey(lines[m:m + 6])
        monkeys_start.append(starting_items)
        properties.append(prop)

    return monkeys_start, properties


def parse_monkey(lines6):
    offset = len("Starting items: ")
    starting_items = lines6[1].strip()[offset:].split(", ")
    for i in range(len(starting_items)):
        starting_items[i] = int(starting_items[i])

    offset = len("Operation: new = old ")
    op_mode = lines6[2].strip()[offset]
    op_value = lines6[2].strip()[offset + 2:]  # "old" or integer

    offset = len("Test: divisible by ")
    test_value = int(lines6[3].strip()[offset:])

    offset = len("If true: throw to monkey ")
    true_target = int(lines6[4].strip()[offset:])

    offset = len("If false: throw to monkey ")
    false_target = int(lines6[5].strip()[offset:])

    return starting_items, [op_mode, op_value, test_value, true_target, false_target]


def run_round(monkeys_start, monkey_properties, rounds=20, get_bored=True):
    if get_bored:
        monkeys = monkeys_start
    else:
        monkeys = [[] for _ in range(len(monkeys_start))]

        for m in range(len(monkeys_start)):
            for i in range(len(monkeys_start[m])):
                monkeys[m].append(Monkey(monkeys_start[m][i], monkey_properties))

    inspections = [0 for _ in range(len(monkeys_start))]

    for _ in range(rounds):
        for m in range(len(monkeys_start)):
            for _ in range(len(monkeys[m])):
                inspections[m] += 1
                item = monkeys[m].pop()
                item = inspect(item, m, monkey_properties)
                if get_bored:
                    item = item // 3
                aim = get_aim(item, m, monkey_properties)
                monkeys[aim].append(item)

    return inspections


def inspect(item, monkey, monkey_properties):
    op_mode, op_value_str, _, _, _ = monkey_properties[monkey]

    op_value = int(op_value_str) if op_value_str.isnumeric() else item
    if op_mode == "+":
        item += op_value
    elif op_mode == "*":
        item *= op_value
    else:
        print(f"ERROR inspect(): unknown op_mode [{op_mode}]")

    return item


def get_aim(item, monkey, monkey_properties):
    _, _, test_value, true_target, false_target = monkey_properties[monkey]
    aim = true_target if (item % test_value == 0) else false_target

    return aim


def level(inspections):
    inspections.sort(reverse=True)
    level_of_monkey_business = inspections[0] * inspections[1]
    print(f"Level of the monkey business = {level_of_monkey_business}")

    return level_of_monkey_business


print("\n--- Day 11: Monkey in the Middle ---")

filename = "input.txt"

print("\n--- Part 1 ---")
monkeys_start, monkey_properties = get_input(filename)
inspections = run_round(monkeys_start, monkey_properties, 20, True)
level(inspections)

print("\n--- Part 2 ---")
monkeys_start, monkey_properties = get_input(filename)
inspections = run_round(monkeys_start, monkey_properties, 10000, False)
level(inspections)

print("")  # new line at end of output
