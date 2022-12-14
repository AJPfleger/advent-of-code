#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 07:16:39 2022

@author: AJPfleger

https://adventofcode.com/2022/day/21
"""


import re
import operator
import math


def getMonkeys(filename):

    file = open(filename, "r")
    Lines = file.readlines()

    monkeys = {}
    for l in Lines:
        m = re.match("(\w+): (.+)", l.strip())
        k, v = m.groups()

        monkeys.update({k: v})

    return monkeys


def parseMonkeyValue(v):
    m = re.match("(\w+) (\D) (\w+)", v.strip())
    ma, op, mb = m.groups()
    return ma, op, mb


def monkeyOp(monkeys, monk):

    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    v = monkeys[monk]
    if v.isnumeric():
        value = int(v)
    elif v == "nan":
        value = float("nan")
    else:
        ma, op, mb = parseMonkeyValue(v)

        value = operators.get(op)(monkeyOp(monkeys, ma), monkeyOp(monkeys, mb))

    return value


def invMonkeyOp(monkeys, monk):

    ma, _, mb = parseMonkeyValue(monkeys[monk])

    va = monkeyOp(monkeys, ma)
    vb = monkeyOp(monkeys, mb)
    humn = va if math.isnan(vb) else vb
    monk = mb if math.isnan(vb) else ma

    hNotFound = True
    while hNotFound:
        ma, op, mb = parseMonkeyValue(monkeys[monk])

        va = monkeyOp(monkeys, ma)
        vb = monkeyOp(monkeys, mb)
        vOp = va if math.isnan(vb) else vb
        monk = mb if math.isnan(vb) else ma

        if op == "+":
            humn -= vOp
        elif op == "-":
            if math.isnan(va):
                humn += vOp
            else:
                humn -= vOp
                humn *= -1
        elif op == "*":
            humn /= vOp
        else:
            if math.isnan(va):
                humn *= vOp
            else:
                humn /= vOp
                humn = 1 / humn

        if monk == "humn":
            hNotFound = False

    return humn


filename = "input.txt"
monkeys = getMonkeys(filename)


print("*** Part 1 ***")
root = int(monkeyOp(monkeys, "root"))
print(f"root = {root}")


print("\n*** Part 2 ***")
monkeys["humn"] = "nan"
humn = int(invMonkeyOp(monkeys, "root"))
print(f"humn = {humn}")
