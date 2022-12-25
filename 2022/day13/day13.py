#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 07:59:26 2022

@author: AJPfleger

https://adventofcode.com/2022/day/13
"""


def generatePairs(Lines):
    pairs = []
    p = []
    for l in range(len(Lines)):
        line = Lines[l]
        if line == "\n":
            pairs.append(p)
            p = []
        else:
            p.append(eval(line))
            
    pairs.append(p)
    
    return pairs

def generateList(Lines,divider):
    p = divider
    for l in range(len(Lines)):
        line = Lines[l]
        if line != "\n":
            p.append(eval(line))
    
    return p

def convertToList(a):
    if isinstance(a,int):
        a = [a]
    return a

def matchType(a,b):
    a = convertToList(a)
    b = convertToList(b)
    aLen = len(a)
    bLen = len(b)
    for i in range(min(aLen,bLen)):
        if not isinstance(a[i],type(b[i])):
            a[i] = convertToList(a[i])
            b[i] = convertToList(b[i])
    return a,b

def checkPair(p):
    a,b = matchType(p[0],p[1])
    
    try:
        if a < b:
            return 1
        elif a == b:
            return 0
        else:
            return -1
    except:
        aLen = len(a)
        bLen = len(b)
        for i in range(min(aLen,bLen)):
            if checkPair([a[i],b[i]]) == 1:
                return 1
            elif checkPair([a[i],b[i]]) == -1:
                return -1
            else: # == 0
                continue
        return 0

def sortList(packets):
    sortCond = True
    while sortCond:
        sortCond = False
        
        for i in range(len(packets)-1):
            cond = checkPair([packets[i],packets[i+1]])
            if cond == -1:
                sortCond = True
                packets[i], packets[i+1] = packets[i+1], packets[i]
        
    return packets

def getIndexSum(pairs):
    indexSum = 0
    for p in range(len(pairs)):
        cond = checkPair(pairs[p])
        if cond == 1:
            indexSum += p+1
    return indexSum
    

file = open('input.txt', 'r')
Lines = file.readlines()


print('\n*** Part 1 ***')
pairs = generatePairs(Lines)
indexSum = getIndexSum(pairs)

print(f'Sum of indeces of correct pairs =  {indexSum}')


print('\n*** Part 2 ***')
divider = [[[2]],[[6]]]
packets = generateList(Lines, divider)
packets = sortList(packets)

decoderkey = (packets.index([[[[2]]]])+1)*(packets.index([[[[6]]]])+1)

print(f'Decoder key =  {decoderkey}')