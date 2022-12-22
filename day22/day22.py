#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 09:02:00 2022

@author: AJPfleger

https://adventofcode.com/2022/day/22
"""


def parse_file(filename):
    file = open(filename, "r")
    lines = file.readlines()

    maze = []
    for i in range(len(lines) - 2):
        row = list(lines[i][:-1])
        if i > 0:  # zero padding for shorter lines
            while len(row) < len(maze[0]):
                row.append(" ")
        maze.append(row)

    instructions_string = lines[-1].strip()

    s = ""
    instructions = []
    for i in range(len(instructions_string)):
        isi = instructions_string[i]

        if isi.isnumeric():
            s += isi
        else:
            instructions.append(s)
            s = ""
            instructions.append(isi)

    if s != "":
        instructions.append(s)

    return maze, instructions


def propagate_through_maze(maze, instructions):
    pos = get_start_position(maze)

    for i in instructions:
        pos = make_step(maze, pos, i)

    return pos


def get_start_position(maze):
    r = 0
    c = maze[r].index(".")
    d = 0  # '>'

    pos = [r, c, d]
    return pos


def make_step(maze, pos, instruction):
    r, c, d = pos
    print(f"inst = {instruction}, pos = {pos}")
    if instruction.isnumeric():
        print("implement instructions")

        if d == 0:
            dr = 0
            dc = 1
        elif d == 1:
            dr = 1
            dc = 0
        elif d == 2:
            dr = 0
            dc = -1
        else:  # d == 3:
            dr = -1
            dc = 0

        for i in range(int(instruction)):
            rows = len(maze)
            cols = len(maze[0])
            dr2 = dr
            dc2 = dc
            while maze[(r + dr2) % rows][(c + dc2) % cols] == " ":
                dr2 += dr
                dc2 += dc

            if maze[(r + dr2) % rows][(c + dc2) % cols] == ".":
                r = (r + dr2) % rows
                c = (c + dc2) % cols
            else:  # maze[(r + dr2) % rows, (c + dc2) % cols] == "#":
                break

    elif instruction == "R":
        d = (d + 1) % 4
    else:  # instruction == "L"
        d = (d - 1) % 4

    return r, c, d


def get_password(position):
    r, c, d = position
    r += 1
    c += 1

    pwd = 1000 * r + 4 * c + d

    return pwd


filename = "input.txt"

print("\n*** Part 1 ***")
maze, instructions = parse_file(filename)
end_position = propagate_through_maze(maze, instructions)
pwd = get_password(end_position)
print(f"The final password is {pwd}\n")
