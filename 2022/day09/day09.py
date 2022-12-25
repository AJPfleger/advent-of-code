#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 07:15:30 2022

@author: AJPfleger

https://adventofcode.com/2022/day/9
"""


def parseLine(Line):
    direction = Line[0]
    steps = int(Line[2:-1])
    
    return [direction, steps]

def checkTouch(H,T):
    if abs(H[0]-T[0]) <= 1 and abs(H[1]-T[1]) <= 1:
        return True
    else:
        return False

def moveH(H, direction):
    
    if direction == 'R':
        H[1] += 1
    elif direction == 'L':
        H[1] -= 1
    elif direction == 'U':
        H[0] += 1
    elif direction == 'D':
        H[0] -= 1
    
    return H

def moveT(H,T):
    if not checkTouch(H,T):
        for i in range(len(H)):
            delta = H[i]-T[i]
            if delta != 0:
                T[i] += int(delta/abs(delta))

    return T

def simulateRope(Lines, knots = 2):

    R = [ [0,0] for _ in range(knots) ]
    visited = {str(R[-1]):''}
    
    for l in range(len(Lines)):
        direction, steps = parseLine(Lines[l])
        
        for _ in range(steps):
            R[0] = moveH(R[0], direction)
            for k in range(knots-1):
                R[k+1] = moveT(R[k],R[k+1])
            visited.update({str(R[-1]):''})
    
    return len(visited)
        

file = open('input.txt', 'r')
Lines = file.readlines()

print('\n*** Part 1 ***')
visited = simulateRope(Lines)    
print(f'Visited positions = {visited}')

print('\n*** Part 2 ***')
visited = simulateRope(Lines, 10)   
print(f'Visited positions = {visited}')
