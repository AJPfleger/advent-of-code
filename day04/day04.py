#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 08:34:02 2022

@author: AJPfleger

https://adventofcode.com/2022/day/4
"""

def lineToRanges(L):
    
    r = ()
    s = ''
    for l in range(len(L)):
        if L[l].isnumeric():
            s += L[l]
        else:
            r += (int(s),)
            s = ''

    return (range(r[0],r[1]+1),range(r[2],r[3]+1))

def includingRange(r):
    
    for i in range(2):
        if r[(i+1)%2][0] in r[i] and r[(i+1)%2][-1] in r[i]:
            return True
    
    return False

def overlappingRange(r):
    
    for i in range(2):
        if r[(i+1)%2][0] in r[i] or r[(i+1)%2][-1] in r[i]:
            return True
    
    return False


file = open('input.txt', 'r')
Lines = file.readlines()

totalIncludes = 0 
for i in range(len(Lines)):
    r = lineToRanges(Lines[i])
    if includingRange(r):
        totalIncludes += 1
    
print(f'Part1 - Number of includes = {totalIncludes}')

totalOverlaps = 0 
for i in range(len(Lines)):
    r = lineToRanges(Lines[i])
    if overlappingRange(r):
        totalOverlaps += 1
    
print(f'Part2 - Number of overlaps = {totalOverlaps}')