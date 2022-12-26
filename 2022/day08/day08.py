#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
--- Day 8: Treetop Tree House ---
https://adventofcode.com/2022/day/8

Created on Thu Dec  8 07:05:00 2022

@author: AJPfleger
https://github.com/AJPfleger
"""

from pathlib import Path


def generate_forest(filename):
    path = Path(__file__).with_name(filename)
    file = path.open("r")
    lines = file.readlines()

    forest = []
    for l in lines:
        row = [int(i) for i in l.strip()]
        forest.append(row)

    return forest


def get_visible(forest):
    n_rows = len(forest)
    n_cols = len(forest[0])

    visible = 0
    for r in range(n_rows):
        for c in range(n_cols):
            if is_visible(forest, r, c):
                visible += 1

    return visible


def is_visible(forest, r, c):
    row = forest[r]
    col = [ri[c] for ri in forest]

    row_left = row[:c + 1]
    row_right = row[c:]
    row_right.reverse()
    col_top = col[:r + 1]
    col_bottom = col[r:]
    col_bottom.reverse()

    directions = [row_left, row_right, col_top, col_bottom]

    visible = False
    for d in directions:
        if d.index(max(d)) == len(d) - 1:
            visible = True
            break

    return visible


def get_max_score(forest):
    n_rows = len(forest)
    n_cols = len(forest[0])

    max_score = 0
    for r in range(n_rows):
        for c in range(n_cols):
            views = unblocked_view(forest, r, c)
            score = get_score(views)

            if score > max_score:
                max_score = score

    return max_score


def unblocked_view(forest, r, c):
    n_rows = len(forest)
    n_cols = len(forest[0])
    h = forest[r][c]

    views = []
    v = 0

    # top
    for v in reversed(range(r)):
        if h <= forest[v][c]:
            break
    views.append(abs(v - r))

    # bottom
    for v in range(r + 1, n_rows):
        if h <= forest[v][c]:
            break
    views.append(abs(v - r))

    # left
    for v in reversed(range(c)):
        if h <= forest[r][v]:
            break
    views.append(abs(v - c))

    # right
    for v in range(c + 1, n_cols):
        if h <= forest[r][v]:
            break
    views.append(abs(v - c))

    return views


def get_score(views):
    s = 1
    for v in views:
        s *= v
    return s


print("\n--- Day 8: Treetop Tree House ---")

filename = "input.txt"
forest = generate_forest(filename)

print("\n--- Part 1 ---")
visible = get_visible(forest)
print(f"Number of visible trees = {visible}")

print("\n--- Part 2 ---")
max_score = get_max_score(forest)
print(f"Max Score = {max_score}\n")
