#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
--- Day 22: Monkey Market ---
https://adventofcode.com/2024/day/22

@author: AJPfleger
https://github.com/AJPfleger
"""


from pathlib import Path


def parse_input(filename):
    path = Path(__file__).with_name(filename)
    file = path.open("r")
    lines = file.readlines()

    secrets = []
    for line in lines:
        val = line.strip()
        if val == "":
            break
        secrets.append(int(val))
    return secrets


def evolve(val):
    val = prune(mix(val, val << 6))
    val = prune(mix(val, val >> 5))
    val = prune(mix(val, val << 11))

    return val


def mix(a, b):
    return a ^ b


def prune(val):
    return val % 16777216


def get_price(val):
    return val % 10


print("\n--- Day 22: Monkey Market ---")

filename = "testinput.txt"

secrets = parse_input(filename)

print("\n--- Part 1 ---")

assert mix(42, 15) == 37, "'mix' is broken"
assert prune(100000000) == 16113920, "'prune' is broken"

final_sum = 0
all_chains = []
for s in secrets:
    chain = [get_price(s)]
    for _ in range(2000):
        s = evolve(s)
        chain.append(get_price(s))
    final_sum += s
    all_chains.append(chain)

print(final_sum)


print("\n--- Part 2 ---")

all_sequences = {}

for chain in all_chains:
    price_list = {}
    diff_chain = [n_1 - n_0 for n_0, n_1 in zip(chain[:-1], chain[1:])]

    while len(diff_chain) >= 4:
        seq = tuple(diff_chain[-4:])
        price_list[seq] = chain[-1]

        diff_chain.pop()
        chain.pop()

    for seq, price in price_list.items():
        all_sequences[seq] = all_sequences.get(seq, 0) + price

print(max(all_sequences.values()))
