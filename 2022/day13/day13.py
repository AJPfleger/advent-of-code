#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
--- Day 13: Distress Signal ---
https://adventofcode.com/2022/day/13

Created on Tue Dec 13 07:59:26 2022

@author: AJPfleger
https://github.com/AJPfleger
"""

from pathlib import Path


def generate_pairs(lines):
    pairs = []
    for li in range(0, len(lines), 3):
        l0, l1 = lines[li:li + 2]
        pairs.append([eval(l0), eval(l1)])

    return pairs


def generate_list(lines, divider):
    packets = divider.copy()
    for l in lines:
        if l != "\n":
            packets.append(eval(l))

    return packets


def get_index_sum(pairs):
    index_sum = 0
    for p in range(len(pairs)):
        if check_pair(pairs[p]) == 1:
            index_sum += p + 1
    return index_sum


def check_pair(p):
    a, b = match_type(p[0], p[1])
    cond = 0
    try:
        if a < b:
            cond = 1
        elif a > b:
            cond = -1
    except:
        a_len = len(a)
        b_len = len(b)
        for i in range(min(a_len, b_len)):
            if check_pair([a[i], b[i]]) == 1:
                cond = 1
                break
            elif check_pair([a[i], b[i]]) == -1:
                cond = -1
                break

    return cond


def match_type(a, b):
    a = convert_to_list(a)
    b = convert_to_list(b)
    a_len = len(a)
    b_len = len(b)
    for i in range(min(a_len, b_len)):
        if not isinstance(a[i], type(b[i])):
            a[i] = convert_to_list(a[i])
            b[i] = convert_to_list(b[i])
    return a, b


def convert_to_list(a):
    if isinstance(a, int):
        a = [a]
    return a


def sort_list(packets):
    sort_cond = True
    while sort_cond:
        sort_cond = False
        for i in range(len(packets) - 1):
            if check_pair([packets[i], packets[i + 1]]) == -1:
                sort_cond = True
                packets[i], packets[i + 1] = packets[i + 1], packets[i]

    return packets


def reduce_packets(packets):
    for i in range(len(packets)):
        changed = True
        while changed:
            p = packets[i]
            try:
                if p == [p[0]]:
                    packets[i] = p[0]
                else:
                    changed = False
            except:
                changed = False

    return packets


print("\n--- Day 13: Distress Signal ---")

filename = "input.txt"
path = Path(__file__).with_name(filename)
file = path.open("r")
lines = file.readlines()

print("\n--- Part 1 ---")
pairs = generate_pairs(lines)
index_sum = get_index_sum(pairs)
print(f"Sum of indices of correct pairs =  {index_sum}")

print("\n--- Part 2 ---")
divider = [[[2]], [[6]]]
packets = generate_list(lines, divider)
packets = sort_list(packets)

packets = reduce_packets(packets)
divider = reduce_packets(divider)
decoder_key = (packets.index(divider[0]) + 1) * (packets.index(divider[1]) + 1)
print(f"Decoder key =  {decoder_key}\n")
