#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 07:21:35 2022

@author: AJPfleger

https://adventofcode.com/2022/day/5
"""

def findSeparationIndex(Lines):
    for l in range(len(Lines)):
        if Lines[l] == '\n':
            return l

def generateStorage(Lines):
    sep = findSeparationIndex(Lines)
    maxStacks = int(Lines[sep-1][-3])
    storage = [ [] for s in range(maxStacks) ]

    for h in range(sep-2,-1,-1):
        for s in range(maxStacks):
            crate = Lines[h][s*4+1]
            if crate != ' ':
                (storage[s]).append(crate)

    return storage

def moveCrates(storage, instructions, crane = "9000"):
    [N,start,end] = instructions
    order = -1
    for n in range(N):
        if crane == "9001":
            order = -N+n
        storage[end-1].append(storage[start-1].pop(order))

    return storage

def simulateInstructions(storage, Lines, crane = "9000"):
    sep = findSeparationIndex(Lines)

    for i in range(sep+1,len(Lines)):
        instructions = parseMove(Lines[i])
        storage = moveCrates(storage, instructions, crane)

    return storage

def parseMove(line):
    instructions = []
    s = ''
    for l in range(len(line)):
        if line[l].isnumeric():
            s += line[l]
        elif s.isnumeric():
            instructions.append(int(s))
            s = ''

    return instructions # [N,start,end]

def printMessage(storage):
    message = ''
    for s in range(len(storage)):
        message += storage[s][-1]
    print(f'Message = {message}')
    return


file = open('input.txt', 'r')
Lines = file.readlines()

print('*** Part 1 ***')
storage = generateStorage(Lines)
simulateInstructions(storage, Lines, "9000")
printMessage(storage)

print('\n*** Part 2 ***')
storage = generateStorage(Lines)
simulateInstructions(storage, Lines, "9001")
printMessage(storage)
