#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 06:46:46 2022

@author: AJPfleger

https://adventofcode.com/2022/day/7
"""

def parseLine(line):
    
    if line[0:5] == '$ cd ': # command
        return {'type':'cd', 'target':line[5:-1]}
        
    elif line[0:4] == 'dir ': # directory
        return {'type':'dir', 'name':line[4:-1]}
    
    elif line[0].isnumeric(): # file
    
        for l in range(len(line)):
            if not line[l].isnumeric():
                return {'type':'file', 'name':line[l+1:-1], 'size':int(line[0:l])}
            
    else: # ls or error
        return {'type':'other'}

def sumFiles(folder):
    
    size = 0
    for entry in folder:
        if type(folder[entry]) is dict:
            size += sumFiles(folder[entry])
        else:
            size += folder[entry]

    return size

def sizeOfFolders(folder):
    
    folderList = []
    
    for entry in folder:
        if type(folder[entry]) is dict:
            folderList.append(sumFiles(folder[entry]))
            subFolders = sizeOfFolders(folder[entry])
            
            for i in range(len(subFolders)):
                folderList.append(subFolders[i])
    
    return folderList

def generateFilesystem(Lines):
    fileSystem = {}
    
    currentDir = []
    for i in range(len(Lines)):
        line = parseLine(Lines[i])
        if line['type'] == 'cd':
            if line['target'] == '/':
                currentDir = []
            elif line['target'] == '..':
                currentDir.pop()
            else:
                currentDir.append([line['target']])
        elif line['type'] == 'dir':
            curD = fileSystem
            for cd in currentDir:
                curD = curD[cd[0]]
            curD.update({line['name']:{}})
        elif line['type'] == 'file':
            curD = fileSystem
            for cd in currentDir:
                curD = curD[cd[0]]
            curD.update({line['name']:line['size']})

    print("Filesystem has been generated.")
    
    return fileSystem


file = open('input.txt', 'r')
Lines = file.readlines()

fileSystem = generateFilesystem(Lines)

cutoffSize = 100000 # <=

print('\n*** Part 1 ***')
s = sizeOfFolders(fileSystem)
totalsize = 0
for i in range(len(s)):
    if s[i] <= cutoffSize:
        totalsize += s[i]
        
print(f'Sum of the total sizes of directories < {cutoffSize}: {totalsize}')

print('\n*** Part 2 ***')
totalSpace = 70000000
neededUnused = 30000000
currentlyUsedSpace = sumFiles(fileSystem)
neededFreeUp = currentlyUsedSpace - (totalSpace - neededUnused)

freeUpSize = currentlyUsedSpace
for i in range(len(s)):
    if s[i] >= neededFreeUp and s[i] < freeUpSize:
        freeUpSize = s[i]

print(f'Free {neededFreeUp} by deleting: {freeUpSize}')