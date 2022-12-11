#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 08:05:00 2022

@author: AJPfleger

https://adventofcode.com/2022/day/11

Manually translated the input-file into functions.
Maybe I add a proper readout in the future.
"""

def inspect(item, monkey):
    if monkey == 0:
        item *= 5
    elif monkey == 1:
        item *= item
    elif monkey == 2:
        item *= 7
    elif monkey == 3:
        item += 1
    elif monkey == 4:
        item += 3
    elif monkey == 5:
        item += 5
    elif monkey == 6:
        item += 8
    elif monkey == 7:
        item += 2
    else:
        print(f'ERROR - inspect({item},{monkey}) - monkey not found')
        
    return item

def bored(item):
    return int(item/3)

def throwTo(item, monkey):
    if monkey == 0:
        aim = 3 if (item%11  == 0) else 4
    elif monkey == 1:
        aim = 6 if (item%2  == 0) else 7
    elif monkey == 2:
        aim = 1 if (item%5  == 0) else 5
    elif monkey == 3:
        aim = 2 if (item%17  == 0) else 5
    elif monkey == 4:
        aim = 2 if (item%19  == 0) else 3
    elif monkey == 5:
        aim = 1 if (item%7  == 0) else 6
    elif monkey == 6:
        aim = 0 if (item%3  == 0) else 7
    elif monkey == 7:
        aim = 4 if (item%13  == 0) else 0
    else:
        print(f'ERROR - throwTo({item},{monkey}) - monkey not found')
        
    return aim

class monkeyClass:
    
    def __init__(self, startItem = 0, div = [i for i in range(1,20)]):
        self.startItem = startItem
        self.div = div
        self.mods = []
        for d in range(len(div)):
            self.mods.append(startItem%div[d])
    
    def updateMods(self):
        for d in range(len(self.div)):
            self.mods[d] = (self.mods[d]%self.div[d])
    
    def __mod__(self,integer):
        return self.mods[integer-1]
    
    def __add__(self,integer):
        for d in range(len(self.div)):
            self.mods[d] += integer
        self.updateMods()
        return self
    
    def __mul__(self,integer):
        if isinstance(integer, self.__class__):
            for d in range(len(self.div)):
                self.mods[d] *= self.mods[d]
        else:
            for d in range(len(self.div)):
                self.mods[d] *= integer
        self.updateMods()
        return self

def level(inspections):
    inspections.sort(reverse=True)
    print(f'Level of the monkey business = {inspections[0]*inspections[1]}')
    return


monkeysStart = [
    [92, 73, 86, 83, 65, 51, 55, 93],
    [99, 67, 62, 61, 59, 98],
    [81, 89, 56, 61, 99],
    [97, 74, 68],
    [78, 73],
    [50],
    [95, 88, 53, 75],
    [50, 77, 98, 85, 94, 56, 89]
    ]


print('\n*** Part 1 ***\n')

monkeys = monkeysStart.copy()

inspections = [ 0 for _ in range(len(monkeysStart))]

for r in range(20):
    for m in range(len(monkeysStart)):
        for i in range(len(monkeys[m])):
            inspections[m] += 1
            item = monkeys[m].pop()
            item = inspect(item,m)
            item = bored(item)
            aim = throwTo(item, m)
            monkeys[aim].append(item)
            
level(inspections)


print('\n*** Part 2 ***\n')

monkeysStart = [
    [92, 73, 86, 83, 65, 51, 55, 93],
    [99, 67, 62, 61, 59, 98],
    [81, 89, 56, 61, 99],
    [97, 74, 68],
    [78, 73],
    [50],
    [95, 88, 53, 75],
    [50, 77, 98, 85, 94, 56, 89]
    ]

monkeys = [ [] for _ in range(len(monkeysStart))]

for m in range(len(monkeysStart)):
    for i in range(len(monkeysStart[m])):
        monkeys[m].append(monkeyClass(monkeysStart[m][i]))

inspections = [ 0 for _ in range(len(monkeysStart))]

for r in range(10000):
    
    for m in range(len(monkeysStart)):
        for i in range(len(monkeys[m])):
            inspections[m] += 1
            item = monkeys[m].pop()
            item = inspect(item,m)
            #item = bored(item)
            aim = throwTo(item, m)
            monkeys[aim].append(item)
            
level(inspections)
