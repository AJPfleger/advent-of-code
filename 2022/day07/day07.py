#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
--- Day 7: No Space Left On Device ---
https://adventofcode.com/2022/day/7

Created on Wed Dec  7 06:46:46 2022

@author: AJPfleger
https://github.com/AJPfleger
"""

from pathlib import Path


def generate_filesystem(filename):
    path = Path(__file__).with_name(filename)
    file = path.open("r")
    lines = file.readlines()

    file_system = {}
    current_dir = []
    for l in lines:
        line = parse_line(l)
        if line["type"] == "cd":
            if line["target"] == "/":
                current_dir = []
            elif line["target"] == "..":
                current_dir.pop()
            else:
                current_dir.append([line["target"]])
        elif line["type"] == "dir":
            cur_d = file_system
            for cd in current_dir:
                cur_d = cur_d[cd[0]]
            cur_d.update({line["name"]: {}})
        elif line["type"] == "file":
            cur_d = file_system
            for cd in current_dir:
                cur_d = cur_d[cd[0]]
            cur_d.update({line["name"]: line["size"]})

    print("INFO Filesystem has been generated.")

    return file_system


def parse_line(line):
    if line[0:5] == "$ cd ":  # command
        return {"type": "cd", "target": line[5:-1]}

    elif line[0:4] == "dir ":  # directory
        return {"type": "dir", "name": line[4:-1]}

    elif line[0].isnumeric():  # file
        sep = line.index(" ")
        return {"type": "file", "name": line[sep + 1:-1], "size": int(line[0:sep]), }

    else:  # ls or error
        return {"type": "other"}


def sum_files(folder):
    size = 0
    for entry in folder:
        if type(folder[entry]) is dict:
            size += sum_files(folder[entry])
        else:
            size += folder[entry]

    return size


def get_size_of_folders(folder):
    folder_list = []
    for entry in folder:
        if type(folder[entry]) is dict:
            folder_list.append(sum_files(folder[entry]))
            sub_folders = get_size_of_folders(folder[entry])

            for sf in sub_folders:
                folder_list.append(sf)

    return folder_list


def get_total_size(file_system, cutoff_size):
    size_of_folders = get_size_of_folders(file_system)
    total_size = 0
    for s in size_of_folders:
        if s <= cutoff_size:
            total_size += s

    return total_size


def get_free_up_size(file_system, total_space, needed_unused):
    size_of_folders = get_size_of_folders(file_system)
    currently_used_space = sum_files(file_system)
    needed_free_up = currently_used_space - (total_space - needed_unused)

    free_up_size = currently_used_space
    for s in size_of_folders:
        if needed_free_up <= s < free_up_size:
            free_up_size = s

    return free_up_size, needed_free_up


print("\n--- Day 7: No Space Left On Device ---")

filename = "input.txt"
file_system = generate_filesystem(filename)

print("\n--- Part 1 ---")
cutoff_size = 100000  # <=
total_size = get_total_size(file_system, cutoff_size)
print(f"Sum of the total sizes of directories <= {cutoff_size}: {total_size}")

print("\n--- Part 2 ---")
total_space = 70000000
needed_unused = 30000000
free_up_size, needed_free_up = get_free_up_size(file_system, total_space, needed_unused)
print(f"Free {needed_free_up} by deleting: {free_up_size}\n")
