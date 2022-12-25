#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 06:55:59 2022

@author: AJPfleger

https://adventofcode.com/2022/day/15
"""


def parseLine(Line):
    pl = []
    s = ''
    
    for c in Line:
        if c == ',' or c == ':' or c == '\n' or c == '=':
            if s[-1].isnumeric(): # last element to detect also negative numbers
                pl.append(eval(s))
                s = ''
            else:
                s = ''
        else:
            s += c

    return pl

def getMeasurments(Lines):
    meas = []
    for line in Lines:
        pl = parseLine(line)
        meas.append(pl)

    return meas

def manhattenDist(pair):
    return abs(pair[0] - pair[2]) + abs(pair[1] - pair[3])

# too slow for part 2
def generateCovBeac(meas, targetRow = 2000000):
    covered = {}
    beacons = {}
    
    for m in meas:
        xS,yS,xB,yB = m
        
        if yB == targetRow:
            beacons.update({xB: 'B'})
        
        d = manhattenDist(m)
        dRow = abs(targetRow - yS)
        if dRow > d:
            continue
        
        r = d - dRow
        for x in range(xS-r,xS+r+1):
            covered.update({x: '#'})
    
    return covered, beacons

def searchBeacon(meas, xMax, yMax):

    for y in range(yMax+1):
        c = []
        for m in meas:
            xS,yS,xB,yB = m
            
            d = manhattenDist(m)
            dRow = abs(y - yS)
            if dRow > d:
                continue
            
            r = d - dRow
            a = max(xS-r,0)
            if a>xMax:
                continue
            b = min(xS+r,xMax)
            c.append([a,b])
            
        c.sort()

        while len(c)>1:
            i = 0
            if c[i][1] < c[i+1][0]:
                break
            if c[i][0] <= c[i+1][1]:
                c[i][1] = max(c[i][1],c[i+1][1])
                c.pop(i+1)
                
        if len(c)>1:
            x = c[0][1]+1
            print(f'x = {x},y = {y}')
            print(f'tuning frequency = {x*4000000 + y}')
            return


file = open('input.txt', 'r')
Lines = file.readlines()
meas = getMeasurments(Lines)


print('\n*** Part 1 ***\n')
covered, beacons = generateCovBeac(meas, 2000000)
sumCovered = len(covered) - len(beacons)
print(f'positions without beacon = {sumCovered}')


print('\n\n*** Part 2 ***\n')
xMax = 4000000
yMax = xMax

# # too slow for the real input (~100 days of computing)
# for y in range(yMax+1):
#     covered, beacons = generateCovBeac(meas, y)
#     for x in range(xMax+1):
#         if not covered.get(x):
#             print(f'x = {x}, y = {y}')

searchBeacon(meas,xMax,yMax)
