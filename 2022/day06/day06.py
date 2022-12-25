#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 07:29:37 2022

@author: AJPfleger

https://adventofcode.com/2022/day/5
"""

def findMarker(sequence, markerLength):
    
    marker = [sequence[0]]*markerLength
    
    for s in range(len(sequence)):
        marker[s%markerLength] = sequence[s]
        
        if len(set(marker)) == markerLength:
            print(f'marker at {s+1}')
            return


file = open('input.txt', 'r')
Lines = file.readlines()

sequence = Lines[0][0:-1]

print('*** Part 1 ***')
findMarker(sequence, 4)

print('*** Part 2 ***')
findMarker(sequence, 14)