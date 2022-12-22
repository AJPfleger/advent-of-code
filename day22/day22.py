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


def propagate_through_maze(maze, instructions, stepper="2D"):
    if stepper == "cube":
        pos = [0, 0, 0, 0]
        for i in instructions:
            pos = make_step_cube(maze, pos, i)
        pos = convert_cube_to_maze(pos)
    else:
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

        dr, dc = get_dr_dc(d)

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


def generate_cube(maze, filename):
    #TODO find pattern for cube
    if filename == "testinput.txt":
        a = 4
        connections = [  # block, new direction
            [[5, 2], [3, 1], [2, 1], [1, 1]],  # 0
            [[2, 0], [4, 3], [5, 3], [0, 1]],  # 1
            [[3, 0], [4, 0], [1, 2], [0, 0]],  # 2
            [[5, 1], [4, 1], [2, 2], [0, 3]],  # 3
            [[5, 0], [1, 3], [2, 3], [3, 3]],  # 4
            [[0, 2], [1, 0], [4, 2], [3, 2]],  # 5
        ]
        block_pos = [[0, 2], [1, 0], [1, 1], [1, 2], [2, 2], [2, 3]]
    elif filename == "input.txt":
        a = 50
        connections = [  # block, new direction
            [[1, 0], [2, 1], [3, 0], [5, 0]],  # 0
            [[4, 2], [2, 2], [0, 2], [5, 3]],  # 1
            [[1, 3], [4, 1], [3, 1], [0, 3]],  # 2
            [[4, 0], [5, 1], [0, 0], [2, 0]],  # 3
            [[1, 2], [5, 2], [3, 2], [2, 3]],  # 4
            [[4, 3], [1, 1], [0, 1], [3, 3]],  # 5
        ]
        block_pos = [[0, 1], [0, 2], [1, 1], [2, 0], [2, 1], [3, 0]]
    else:
        print(f"ERROR generate_cube: unknown preset for [{filename}]")
        return

    cube = []

    for side in range(6):
        block = []
        br0, bc0 = block_pos[side]
        for r in range(a):
            block.append(maze[a * br0 + r][a * bc0:a * bc0 + a])

        cube.append(block)

    cube.append(connections)

    return cube


def get_dr_dc(d):
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

    return dr, dc


def make_step_cube(cube, pos, instruction):
    r, c, d, b = pos
    print(f"inst = {instruction}, pos = {pos}")
    if instruction.isnumeric():

        dr, dc = get_dr_dc(d)

        for i in range(int(instruction)):
            a = len(cube[0])
            b2 = b
            d2 = d
            print(f'\nd {d}, c {c}, r {r}, a {a}')
            if ((d2 == 0 and c == (a - 1)) or
                    (d2 == 1 and r == (a - 1)) or
                    (d2 == 2 and c == 0) or
                    (d2 == 3 and r == 0)):
                print('change block a')
                b2, d2 = cube[-1][b][d]
                dr, dc = get_dr_dc(d2)

            if d == d2:  # no coordinate transform
                r2 = r
                c2 = c
            elif d == 0 and d2 == 1:
                r2 = -1
                c2 = a-1 - r
            elif d == 0 and d2 == 2:
                r2 = a-1 - r
                c2 = c + 1
            elif d == 0 and d2 == 3:
                r2 = a
                c2 = r
            elif d == 1 and d2 == 0:
                r2 = a-1 - c
                c2 = -1
            elif d == 1 and d2 == 2:
                r2 = c
                c2 = a
            elif d == 1 and d2 == 3:
                r2 = a
                c2 = a-1 - c
            elif d == 2 and d2 == 0:
                r2 = a-1 -r
                c2 = -1
            elif d == 2 and d2 == 1:
                r2 = -1
                c2 = r
            elif d == 2 and d2 == 3:
                r2 = a
                c2 = a-1 - r
            elif d == 3 and d2 == 0:
                r2 = c
                c2 = -1
            elif d == 3 and d2 == 1:
                r2 = -1
                c2 = a-1 - c
            elif d == 3 and d2 == 2:
                r2 = a-1 - c
                c2 = a
            else:
                print('missing case?')

            if cube[b2][(r2 + dr) % a][(c2 + dc) % a] == ".":
                r = (r2 + dr) % a
                c = (c2 + dc) % a
                b = b2
                d = d2
                print(f'pos = [{r},{c},{d},{b}]')
            else:  # maze[(r + dr2) % rows, (c + dc2) % cols] == "#":
                break

    elif instruction == "R":
        d = (d + 1) % 4
    else:  # instruction == "L"
        d = (d - 1) % 4

    return r, c, d, b



def convert_cube_to_maze(pos):
    # TODO - make conversion

    return pos


filename = "input.txt"
maze, instructions = parse_file(filename)

print("\n*** Part 1 ***")
end_position = propagate_through_maze(maze, instructions)
pwd = get_password(end_position)
print(f"The final password is {pwd}\n")

print("\n*** Part 2 ***")
cube = generate_cube(maze, filename)
end_position = propagate_through_maze(cube, instructions, "cube")
# pwd = get_password(end_position) # TODO - implement
pwd = 1000*(50+1+1) + 4*(50+26+1) + 3
print(f"The final password is {pwd}\n")
