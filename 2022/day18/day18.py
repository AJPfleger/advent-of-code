#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 10:30:28 2022

@author: AJPfleger

https://adventofcode.com/2022/day/18
"""


def getCore(filename):
    if filename == 'testinput.txt':
        print('##### WARNING - TEST INPUT #####')
        
    file = open(filename, 'r')
    Lines = file.readlines()
    
    core = {}
    for l in Lines:
        c = str(list(eval(l)))
        core.update({c:''})

    return core

def getMinMax(core):
    
    minC = []
    maxC = []
    
    for a in core:
        minC.append(min(eval(a)))
        maxC.append(max(eval(a)))
    
    return [min(minC),max(maxC)]

def getSurface(core):
    nCoordinates = len(core)
    surface = nCoordinates * 3 * 2
    
    for a in core:
        x,y,z = eval(a)
        neighbours = (int(str([x-1,y,z]) in core) +
                      int(str([x+1,y,z]) in core) +
                      int(str([x,y-1,z]) in core) +
                      int(str([x,y+1,z]) in core) +
                      int(str([x,y,z-1]) in core) +
                      int(str([x,y,z+1]) in core) )
        surface -= neighbours
        
    return surface

def fillCore(core):
    minmax = getMinMax(core)
    air = {}
    # just corners. maybe whole surface of outer cube?
    for x in minmax:
        for y in minmax:
            for z in minmax:
                if str([x,y,z]) not in core:
                        air.update({str([x,y,z]):''})
                        
    
    for i in range(100): # add proper stop condition
        for x in range(minmax[0],minmax[1]+1):
            for y in range(minmax[0],minmax[1]+1):
                for z in range(minmax[0],minmax[1]+1):
                    if str([x,y,z]) not in core and str([x,y,z]) not in air:
                        if (str([x-1,y,z]) in air or
                            str([x+1,y,z]) in air or
                            str([x,y-1,z]) in air or
                            str([x,y+1,z]) in air or
                            str([x,y,z-1]) in air or
                            str([x,y,z+1]) in air ):
                                air.update({str([x,y,z]):''})
    
    for x in range(minmax[0],minmax[1]+1):
        for y in range(minmax[0],minmax[1]+1):
            for z in range(minmax[0],minmax[1]+1):
                if str([x,y,z]) not in air:
                    core.update({str([x,y,z]):''})
    
    return core


filename = 'input.txt'


print('\n*** Part 1 ***\n')
core = getCore(filename)
surface = getSurface(core)
print(f'Surface = {surface}')


print('\n\n*** Part 2 ***\n')
core = getCore(filename)
core = fillCore(core)
surface = getSurface(core)
print(f'Surface = {surface}')
