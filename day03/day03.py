#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 08:06:00 2022

@author: AJPfleger

https://adventofcode.com/2022/day/2
"""

def sanitizeLine(L):
    return L[0:-1]

def sanitizeLineGroup(LG):
    
    for l in range(len(LG)):
        LG[l] = sanitizeLine(LG[l])
    
    return LG

def matchLines(l1,l2):
    l12 = ''
    
    for i1 in l1:
        for i2 in l2:
            if i1 == i2:
                l12 += i1
    
    return l12

def priorityOfLine(L):
    halfLength = int(len(L)/2)
    item = matchLines(L[:halfLength], L[halfLength:])
    
    return convertItemToPriority(item[0])
    
def priorityOfGroup(LG):
    
    lHelp = LG[0]
    for l in range(1,len(LG)):
        lHelp = matchLines(lHelp,LG[l])

    return convertItemToPriority(lHelp[0])

def convertItemToPriority(item):
    priority = ord(item)-96
    
    if priority < 1:
        priority += 58
    
    return priority


file = open('input.txt', 'r')
Lines = file.readlines()

sumOfPriorities = 0 
for i in range(len(Lines)):
    line = sanitizeLine(Lines[i])
    sumOfPriorities += priorityOfLine(line)
    
print(f'Part1 - Sum of priorities = {sumOfPriorities}')

sumOfPriorities = 0 
for i in range(0,len(Lines),3):
    lineGroup = sanitizeLineGroup(Lines[i:i+3])
    sumOfPriorities += priorityOfGroup(lineGroup)
    
print(f'Part2 - Sum of priorities = {sumOfPriorities}')