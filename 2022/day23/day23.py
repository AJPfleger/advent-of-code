#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 06:13:00 2022

@author: AJPfleger

https://adventofcode.com/2022/day/23
"""


def parse_file(filename):
    file = open(filename, "r")
    lines = file.readlines()

    grove = {}
    for ns in range(len(lines)):
        row = list(lines[ns])
        for ew in range(len(row)):
            if row[ew] == "#":
                grove.update({str([ns, ew]): ""})

    return grove


def find_limits(grove_dict):
    grove = []
    for g in list(grove_dict):
        grove.append(eval(g))

    grove.sort()
    min_ns = grove[0][0]
    max_ns = grove[-1][0]
    grove.sort(key=lambda x: x[1])
    min_ew = grove[0][1]
    max_ew = grove[-1][1]

    return [min_ns, max_ns, min_ew, max_ew]


def propagate(grove, max_moves=10):
    direction = ["e", "n", "s", "w"]

    moves = 0
    moved = True
    while moved and moves < max_moves:
        moved = False
        moves += 1
        direction.append(direction.pop(0))

        moveable = []
        suggestions = []
        for elf in grove:

            if no_neighbours(elf, grove):
                continue
            moved = True
            for d in direction:
                sug_pos = suggest_position(elf, grove, d)

                if len(sug_pos) > 0:
                    moveable.append(elf)
                    suggestions.append(sug_pos)
                    break

        for i in range(len(suggestions)):
            if suggestions.count(suggestions[i]) == 1:  # move all
                grove.pop(moveable[i])
                grove.update({suggestions[i]: ""})

    if moves == max_moves:
        print(f"WARNING propagate: max_moves reached")

    return grove, moves


def suggest_position(elf, grove, d):
    ns, ew = eval(elf)

    if d == "n":
        ns_opts = [-1] * 3
        ew_opts = [-1, 0, 1]
    elif d == "s":
        ns_opts = [1] * 3
        ew_opts = [-1, 0, 1]
    elif d == "w":
        ns_opts = [-1, 0, 1]
        ew_opts = [-1] * 3
    else:  # d == 'e':
        ns_opts = [-1, 0, 1]
        ew_opts = [1] * 3

    for dns in ns_opts:
        for dew in ew_opts:
            if str([ns + dns, ew + dew]) in grove:
                return ""

    return str([ns + ns_opts[1], ew + ew_opts[1]])


def no_neighbours(elf, grove):
    cond = True
    ns, ew = eval(elf)
    for dns in [-1, 0, 1]:
        for dew in [-1, 0, 1]:
            if dns == dew == 0:
                continue
            elif str([ns + dns, ew + dew]) in grove:
                cond = False
                break

    return cond


def get_vacant(grove):
    n_elves = len(grove)

    min_ns, max_ns, min_ew, max_ew = find_limits(grove)

    area = (max_ns - min_ns + 1) * (max_ew - min_ew + 1)

    return area - n_elves


def print_grove(grove):
    min_ns, max_ns, min_ew, max_ew = find_limits(grove)
    d_ns = max_ns - min_ns + 1
    d_ew = max_ew - min_ew + 1

    g = [["," for _ in range(d_ew)] for _ in range(d_ns)]

    for elf in list(grove):
        ns, ew = eval(elf)
        g[ns - min_ns][ew - min_ew] = "#"

    print("\ngrove:")

    for r in range(len(g)):
        print("".join(g[r]))

    return


filename = "input.txt"

print("\n*** Part 1 ***")
grove = parse_file(filename)
grove, _ = propagate(grove)
vacant = get_vacant(grove)
print(f"Vacant positions: {vacant}")

print("\n*** Part 2 ***")
grove = parse_file(filename)
grove, moves = propagate(grove, int(1e3))
print(f"Required moves: {moves}")
