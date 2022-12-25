#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: AJPfleger

https://adventofcode.com/2022/day/8
"""


def generateForest(Lines):
    nRows = len(Lines)
    nCols = len(Lines[0])-1 # -1 to account for ending \n
    
    forest = [ [ [] for _ in range(nRows) ] for _ in range(nCols) ]
    
    for r in range(nRows):
        for c in range(nCols):
            forest[r][c] = int(Lines[r][c])
    
    return forest

def unblockedView(forest,r,c):
    nRows = len(forest)
    nCols = len(forest[0])
    h = forest[r][c]
    views = []
    
    # top
    for v in range(r-1,-1,-1):
        if h <= forest[v][c]:
            break
    views.append(abs(v-r))
    
    # bottom
    for v in range(r+1,nRows):
        if h <= forest[v][c]:
            break
    views.append(abs(v-r))
    
    # left
    for v in range(c-1,-1,-1):
        if h <= forest[r][v]:
            break
    views.append(abs(v-c))
    
    # right
    for v in range(c+1,nCols):
        if h <= forest[r][v]:
            break
    views.append(abs(v-c))
    
    return views

def getScore(views):
    s = 1
    for v in views:
        s *= v
    return s
    
def isVisible(forest,r,c):
    nRows = len(forest)
    nCols = len(forest[0])
    
    h = forest[r][c]
    
    # top
    for v in range(r-1,-1,-1):
        if h <= forest[v][c]:
            break
    if v == 0 and h > forest[v][c]:
        return True
    
    # bottom
    for v in range(r+1,nRows):
        if h <= forest[v][c]:
            break
    if v == nRows-1 and h > forest[v][c]:
        return True
    
    # left
    for v in range(c-1,-1,-1):
        if h <= forest[r][v]:
            break
    if v == 0 and h > forest[r][v]:
        return True
    
    # right
    for v4 in range(c+1,nCols):
        if h <= forest[r][v4]:
            break
    if v4 == nCols-1 and h > forest[r][v4]:
        return True
    
    return False


file = open('input.txt', 'r')
Lines = file.readlines()

forest = generateForest(Lines)

nRows = len(forest)
nCols = len(forest[0])


print('\n*** Part 1 ***')

visible = 0

# from the outside
visible += 2*nRows + 2*nCols - 4

# make map of visible trees? needs numpy I think
for r in range(1,nRows-1):
    for c in range(1,nCols-1):
        if isVisible(forest,r,c):
            visible += 1

print(f'Number of visible trees = {visible}')


print('\n*** Part 2 ***')
    
# assuming, that border trees are not the best
maxScore = 0
for r in range(1,nRows-1):
    for c in range(1,nCols-1):
        
        views = unblockedView(forest,r,c)
        score = getScore(views)
        
        if score > maxScore:
            maxScore = score

print(f'Max Score = {maxScore}')
