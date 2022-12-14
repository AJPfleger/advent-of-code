#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 06:44:07 2022

@author: AJPfleger

https://adventofcode.com/2022/day/14
"""


def parseLine(Line):
    pl = []
    s = ''
    
    for c in Line:
        if c == ' ' or c == '\n':
            if s == '->':
                s = ''
            else:
                pl.append(eval(s))
                s = ''
        else:
            s += c
            
    return pl

def linesToList(Lines):
    lst = []
    
    for L in Lines:
        lst.append(parseLine(L))
    
    return lst

def createCave(Lines, mode = 'simple'):
    lst = linesToList(Lines)
    maxDepth = 300
    maxWidth = 1001
    
    cave = [ [ '.' for _ in range(maxWidth)] for _ in range(maxDepth) ]
    
    for line in lst:
        for i in range(len(line)-1):
            w0 = line[i][0]
            w1 = line[i+1][0]
            d0 = line[i][1]
            d1 = line[i+1][1]
        
            if w0 == w1:
                w = w0
                if d0>d1:
                    d0,d1 = d1,d0
                for d in range(d0,d1+1):
                    cave[d][w] = '#'
            else:
                d = d0
                if w0>w1:
                    w0,w1 = w1,w0
                for w in range(w0,w1+1):
                    cave[d][w] = '#'
    cave[0][500] = '+'
    
    # remove empty lines at the bottom
    foundRock = False
    while not foundRock:
        if '#' in cave[-1]:
            foundRock = True
        else:
            cave.pop()
    
    if mode == 'simple':
        cave = popSide(cave,'left')
        cave = popSide(cave,'right')

    elif mode == 'groundfloor':
        cave = expandCave(cave)
        while len(cave[0]) > 2*len(cave)+1 :
            for d in range(len(cave)):
                cave[d].pop(0)
                cave[d].pop(-1)
    else:
        print(f'ERROR unknown mode {mode}')
        
    return cave

def popSide(cave,side):
    sideIndex = 0 if (side == 'left') else -1
    foundRock = False
    while not foundRock:
        for d in range(len(cave)):
            if cave[d][sideIndex] == '#':
                foundRock = True
                break
        if not foundRock:
            for d in range(len(cave)):
                cave[d].pop(sideIndex)
    
    return cave

def expandCave(cave):
    maxW = len(cave[0])
    
    cave.append([ '.' for _ in range(maxW)])
    cave.append([ '#' for _ in range(maxW)])
    
    return cave
    
def flowSand(cave):
    startW = cave[0].index('+')
    maxD = len(cave)
    maxW = len(cave[0])
    
    units = 0
    noOverflow = True
    while noOverflow:
        w = startW
        if cave[0][startW] == 'O':
            return units

        for d in range(1,maxD):
            if cave[d][w] == '.':
                continue
            elif w == 0:
                noOverflow = False
                break
            elif cave[d][w-1] == '.':
                w -= 1
            elif w == maxW-1:
                noOverflow = False
                break
            elif cave[d][w+1] == '.':
                w += 1
            elif d == 0:
                noOverflow = False
                break
            else:
                cave[d-1][w] = 'O'
                units += 1
                break
    
    return units


file = open('input.txt', 'r')
Lines = file.readlines()


print('\n*** Part 1 ***\n')
cave = createCave(Lines)
units = flowSand(cave)
print(f'max units = {units}')


print('\n\n*** Part 2 ***\n')
cave = createCave(Lines,'groundfloor')
units = flowSand(cave)
print(f'max units = {units}')
