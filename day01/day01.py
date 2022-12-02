#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 07:56:39 2022

@author: AJPfleger

https://adventofcode.com/2022/day/1
"""

file = open('day01input.txt', 'r')
Lines = file.readlines()

calPerElf = [0]
elfCounter = 0
for i in range(len(Lines)):
    if Lines[i] != '\n':
        calItem = int(Lines[i])
        calPerElf[-1] += calItem
    else:
        calPerElf.append(0)

calPerElf.sort(reverse=True)
print(f'Elf with the most calories carries {calPerElf[0]} calories.')

topCals = 3
calSum = 0
for i in range(topCals):
    calSum += calPerElf[i]

print(f'The {topCals} elves with the most calories carry together {calSum} calories.')