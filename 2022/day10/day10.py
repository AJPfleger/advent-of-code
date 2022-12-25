#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 05:50:49 2022

@author: AJPfleger

https://adventofcode.com/2022/day/10
"""

def parseLine(Line):
    
    if Line[0:4] == "noop": # noop => addx 0
        return {"cmd":"noop"}
    else:
        return {"cmd":"addx","x":int(Line[5:-1])}

def createRegister(Lines):
    register = [1]
    
    for l in range(len(Lines)):
        cmd = parseLine(Lines[l])
        register.append(register[-1])
        
        if cmd['cmd'] == "addx":
            register.append(register[-1]+cmd['x'])
    
    return register

def investigateCycles(register, cycles):
    sumSigCyc = 0

    for c in cycles:
        sumSigCyc += c*register[c-1]
    
    print(f'The sum of the signal strengths is {sumSigCyc}.')
    
    return

def display(register, hRes = 40, vRes = 6):

    res = hRes * vRes
    disp = [ "." for _ in range(res) ]

    for p in range(res):
        if abs(register[p]-(p%hRes)) <= 1:
            disp[p] = "#"

    for i in range(vRes):
        print("".join(disp[hRes*i:hRes*(i+1)]))
    
    return


file = open('input.txt', 'r')
Lines = file.readlines()

print('\n*** Part 1 ***\n')
register = createRegister(Lines)
cycles = [20, 60, 100, 140, 180, 220]
investigateCycles(register, cycles)

print('\n*** Part 2 ***\n')
display(register)