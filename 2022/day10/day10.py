#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
--- Day 10: Cathode-Ray Tube ---
https://adventofcode.com/2022/day/10

Created on Sat Dec 10 05:50:49 2022

@author: AJPfleger
https://github.com/AJPfleger
"""

from pathlib import Path


def get_commands(filename):
    path = Path(__file__).with_name(filename)
    file = path.open("r")
    lines = file.readlines()

    commands = []
    for l in lines:
        if l[0:4] == "noop":
            cmd = {"cmd": "noop"}
        else:
            cmd = {"cmd": "addx", "x": int(l[5:-1])}

        commands.append(cmd)

    return commands


def create_register(commands):
    register = [1]
    for cmd in commands:
        register.append(register[-1])

        if cmd["cmd"] == "addx":
            register.append(register[-1] + cmd["x"])

    return register


def investigate_cycles(register, cycles):
    sum_sig_cyc = 0
    for c in cycles:
        sum_sig_cyc += c * register[c - 1]

    return sum_sig_cyc


def display(register, h_res=40, v_res=6):
    full_res = h_res * v_res
    disp = ["." for _ in range(full_res)]

    for p in range(full_res):
        if abs(register[p] - (p % h_res)) <= 1:
            disp[p] = "#"

    for i in range(v_res):
        print("".join(disp[h_res * i: h_res * (i + 1)]))

    print("\n")

    return


print("\n--- Day 10: Cathode-Ray Tube ---")

filename = "input.txt"
commands = get_commands(filename)
register = create_register(commands)

print("\n--- Part 1 ---")
cycles = [i for i in range(20, 221, 40)]
sum_sig_cyc = investigate_cycles(register, cycles)
print(f"The sum of the signal strengths is {sum_sig_cyc}.")

print("\n--- Part 2 ---")
display(register)
