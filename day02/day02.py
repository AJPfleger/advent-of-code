#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 07:16:48 2022

@author: AJPfleger

https://adventofcode.com/2022/day/2
"""

def RPS(p1,p2):
    if p1==p2: #(p2-p1)%3 == 0
        return 3
    if (p2-p1)%3 == 1:
        return 6
    return 0

def inverseRPS(p1,res):
    if res==0: # loss
        p2 = (p1-1)%3
        if p2 == 0:
            p2 = 3
        return p2
    if res==1: # draw
        return p1
    p2 = (p1+1)%3
    if p2 == 0:
        p2 = 3
    return p2

file = open('day02input.txt', 'r')
Lines = file.readlines()

totalScore = 0
for i in range(len(Lines)):
    p1 = ord(Lines[i][0])-64 #player1
    p2 = ord(Lines[i][2])-87 #player2
    
    totalScore += p2 + RPS(p1,p2)
    
print(f'Part1 - Expected Score = {totalScore}')

totalScore = 0
for i in range(len(Lines)):
    p1 = ord(Lines[i][0])-64 #player1
    res = ord(Lines[i][2])-88 #expected result 0/1/2
    
    totalScore += 3*res + inverseRPS(p1,res)
    
print(f'Part2 - Expected Score = {totalScore}')

