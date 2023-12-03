#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 07:38:10 2022

@author: AJPfleger

https://adventofcode.com/2022/day/17
"""


def printCave(cave, lines=10):

    D = len(cave)
    if lines > D:
        print(f"WARNING - printcave: lines={lines} set to {D}")
        lines = D

    for l in range(D - 1, D - 1 - lines, -1):
        print("".join(cave[l]))
    return


def generateRock(rock, W, offset=2):

    assert 3 + offset <= W and "cave not wide enough"

    R = []
    for _ in range(4):  # highest rock has for lines
        R.append(["." for _ in range(W)])

    if rock == "-":
        for i in range(4):
            R[0][i + offset] = "@"

    elif rock == "+":
        R[0][1 + offset] = "@"
        for i in range(3):
            R[1][i + offset] = "@"
        R[2][1 + offset] = "@"

    elif rock == "L":
        for i in range(3):
            R[0][i + offset] = "@"
        R[1][2 + offset] = "@"
        R[2][2 + offset] = "@"

    elif rock == "I":
        for i in range(4):
            R[i][offset] = "@"

    elif rock == "o":
        R[0][offset] = "@"
        R[0][offset + 1] = "@"
        R[1][offset] = "@"
        R[1][offset + 1] = "@"

    else:
        print(f"ERROR - rock shape [{rock}] not found")

    while "@" not in R[-1]:
        R.pop()

    return R


def addNewRock(cave, rock, offset=2):
    W = len(cave[0])
    space = ["." for _ in range(W)]
    for _ in range(3):
        cave.append(space.copy())

    newRock = generateRock(rock, W, offset)
    for l in newRock:
        cave.append(l)

    return cave


def moveSide(cave, side):

    if not pushSpace(cave, side):
        return cave

    H = len(cave)
    W = len(cave[0])

    if side == ">":
        for ci in reversed(range(0, W - 1)):
            for ri in range(H):
                if cave[ri][ci] == "@":
                    cave[ri][ci] = "."
                    cave[ri][ci + 1] = "@"
    elif side == "<":
        for ci in range(1, W):
            for ri in range(H):
                if cave[ri][ci] == "@":
                    cave[ri][ci] = "."
                    cave[ri][ci - 1] = "@"
    else:
        print(f"WARNING - moveSide: unknown command [{side}]")

    return cave


def pushSpace(cave, side):
    H = len(cave)
    W = len(cave[0])

    if side == ">":
        for ri in range(H):
            if cave[ri][W - 1] == "@":
                return False
        for ci in reversed(range(0, W - 1)):
            for ri in range(H):
                if cave[ri][ci] == "@" and cave[ri][ci + 1] == "#":
                    return False
    elif side == "<":
        for ri in range(H):
            if cave[ri][0] == "@":
                return False
        for ci in range(1, W):
            for ri in range(H):
                if cave[ri][ci] == "@" and cave[ri][ci - 1] == "#":
                    return False
    else:
        print(f"WARNING - pushSpace: unknown command [{side}]")

    return True


def checkFallSpace(cave):
    H = len(cave)
    W = len(cave[0])

    for ci in range(0, W):
        for ri in range(1, H):
            if cave[ri][ci] == "@" and cave[ri - 1][ci] == "#":
                return False

    return True


def fall(cave):
    H = len(cave)
    W = len(cave[0])

    for ci in range(0, W):
        for ri in range(1, H):
            if cave[ri][ci] == "@":
                cave[ri][ci] = "."
                cave[ri - 1][ci] = "@"

    return cave


def propagateRock(cave, rock, jets, jetsIter):
    # W = len(cave[0])
    cave = addNewRock(cave, rock)

    fallSpace = True
    while fallSpace:
        # printCave(cave,999)
        side = jets[jetsIter % len(jets)]
        jetsIter += 1
        cave = moveSide(cave, side)

        fallSpace = checkFallSpace(cave)
        if fallSpace:
            cave = fall(cave)

    # only look at the lines of the rock and the line below ?
    for h in range(len(cave)):
        cave[h] = converToSolid(cave[h])

    while "#" not in cave[-1]:
        cave.pop()

    return cave, jetsIter


def converToSolid(line):
    for p in range(len(line)):
        if line[p] == "@":
            line[p] = "#"

    return line


filename = "testinput.txt"
if filename == "testinput.txt":
    print("##### WARNING - TEST INPUT #####")

file = open(filename, "r")
Lines = file.readlines()
jets = Lines[0].strip()

W = 7
cave = []
cave.append(["#" for _ in range(W)])
rocks = ["-", "+", "L", "I", "o"]


print("\n*** Part 1 ***\n")
maxRocks = 2022 * 100
jetsIter = 0

import time

st = time.time()
for r in range(maxRocks):
    rock = rocks[r % len(rocks)]

    cave, jetsIter = propagateRock(cave, rock, jets, jetsIter)

    if jetsIter % len(jets) == 0:
        break

et = time.time()
elapsed_time = et - st
print("Execution time:", elapsed_time, "seconds")

tower = len(cave) - 1

print(f"Height of the tower = {tower}")


print("\n\n*** Part 2 ***\n")
maxRocks = 1000000000000
print("unsolved :(")
