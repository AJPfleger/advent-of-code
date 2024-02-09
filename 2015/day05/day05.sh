#!/bin/bash

# --- Day 2: I Was Told There Would Be No Math ---
# https://adventofcode.com/2015/day/2
#
# https://github.com/AJPfleger

echo "--- Day 2: I Was Told There Would Be No Math ---"

filename=input.txt

nicecount=0
while read line; do

  # skip ab, cd, pq, or xy
  if [[ $line == *"ab"* ]] || [[ $line == *"cd"* ]] || [[ $line == *"pq"* ]] || [[ $line == *"xy"* ]]
  then
    continue
  fi

  res="${line//[^a]}"

  ((vowels=${#${line//[^a]}}+${#${line//[^e]}}+${#${line//[^i]}}+${#${line//[^o]}}+${#${line//[^u]}}))
  if [[ $vowels -lt 3 ]]
  then
    continue
  fi

#  if ! [[ $line =~ ([a-z])\1 ]]
#  then
#    continue
#  fi

  if ! echo "$line" | grep -Eq '([a-z])\1'
  then
    continue
  fi

  ((nicecount+=1))
done < $filename

echo "Part 1: ${nicecount} nice strings."
