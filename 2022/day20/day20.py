#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 09:36:38 2022

@author: AJPfleger

https://adventofcode.com/2022/day/20
"""


def getSequence(filename, key=1):
    file = open(filename, "r")
    Lines = file.readlines()

    sequence = []
    for i in range(len(Lines)):
        sequence.append({"val": eval(Lines[i]) * key, "opos": i})

    return sequence


def sequenceToList(sequence):
    l = []
    for d in sequence:
        l.append(d["val"])

    return l


def mix(sequence, maxMix=1):
    period = len(sequence)

    for i in range(maxMix):
        print(f"mixing {i + 1}/{maxMix}")
        for opos in range(period):
            for i in range(period):
                d = sequence[i]
                if d["opos"] == opos:
                    v = d["val"]
                    sequence.pop(i)
                    pos = v + i

                    if pos < 0:
                        pos = (v + i) % (period - 1)
                    elif pos >= period:
                        pos = (v + i) % (period - 1)

                    sequence.insert(pos, d)

                    break

    return sequence


def getRes(sequence):
    period = len(sequence)

    for i in range(period):
        if sequence[i]["val"] == 0:
            i0 = i
            break

    i1k = (1000 + i0) % period
    i2k = (2000 + i0) % period
    i3k = (3000 + i0) % period

    res = sequence[i1k]["val"] + sequence[i2k]["val"] + sequence[i3k]["val"]

    return res


filename = "input.txt"

print("\n*** Part 1 ***\n")
sequence = getSequence(filename)
sequence = mix(sequence)
res = getRes(sequence)
print(f"\nSum of the three numbers = {res}\n")

print("\n*** Part 2 ***\n")
sequence = getSequence(filename, 811589153)
sequence = mix(sequence, 10)
res = getRes(sequence)
print(f"\nSum of the three numbers = {res}\n")
