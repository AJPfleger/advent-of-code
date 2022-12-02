#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 07:16:48 2022

@author: AJPfleger

https://adventofcode.com/2022/day/2
"""

def RPS(p1,p2):
    return (p2-p1+1)%3

# returns what p2 needs to play to get to res
def inverseRPS(p1,res):
    return (p1+res-1)%3

def pointsRound(p,res):
    return p+1 + 3*res

file = open('day02input.txt', 'r')
Lines = file.readlines()

totalScore = 0 
for i in range(len(Lines)):
    p1 = ord(Lines[i][0])-65 #player1
    p2 = ord(Lines[i][2])-88 #player2
    res = RPS(p1,p2)
    
    totalScore += pointsRound(p2,res)
    
print(f'Part1 - Expected Score = {totalScore}')

totalScore = 0
for i in range(len(Lines)):
    p1 = ord(Lines[i][0])-65 #player1
    res = ord(Lines[i][2])-88 #expected result 0/1/2
    p2 = inverseRPS(p1,res)
    
    totalScore += pointsRound(p2,res)
    
print(f'Part2 - Expected Score = {totalScore}')