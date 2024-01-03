#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: AJPfleger

https://adventofcode.com/2023/day/12
"""

from functools import lru_cache


def parse_file(filename):
    file = open(filename, "r")
    lines = file.readlines()
    allSprings = []
    allBroken = []
    for l in lines:
        springsStr, broken = parse_line(l)
        allSprings.append(springsStr)
        allBroken.append(broken)

    return allSprings, allBroken


def parse_line(line):
    springsStr, brokenStr = line.strip().split(" ")
    bss = brokenStr.split(",")
    broken = ()
    for b in bss:
        broken += (int(b),)

    return springsStr, broken


@lru_cache(maxsize=None)
def countpossibilities(springsStr, broken):
    B = broken[0]

    C = 0
    if len(broken) > 1:
        while len(springsStr) >= sum(broken) + len(broken) - 1:
            if "." not in springsStr[0:B] and springsStr[B] != "#":
                C = C + countpossibilities(springsStr[B + 1 :], broken[1:])

            if springsStr[0] == "#":
                break

            springsStr = springsStr[1:]
    else:
        nss = len(springsStr)
        for p in range(nss - B + 1):
            if "." not in springsStr[0:B] and "#" not in springsStr[B:]:
                C = C + 1

            if springsStr[0] == "#":
                break

            springsStr = springsStr[1:]

    return C


filename = "input.txt"

allSprings, allBroken = parse_file(filename)


print("\n*** Part 1 ***")

C = 0
for s in range(len(allSprings)):
    C2 = countpossibilities(allSprings[s], allBroken[s])
    C += C2
    print(f"string {s+1}: {C2}")

print(f"resultPart1 = {C}")


print("\n*** Part 2 ***")

broken = allBroken[0][:]

springs = allSprings[0]
for _ in range(5 - 1):
    springs += "?"
    springs += allSprings[0]

print(springs)


C = 0
for s in range(len(allSprings)):
    broken = allBroken[s][:] * 5
    springs = allSprings[s]
    for _ in range(5 - 1):
        springs += "?"
        springs += allSprings[s]
    C2 = countpossibilities(springs, broken)
    C += C2
    print(f"string {s+1}: {C2}")

print(f"resultPart2 = {C}")
