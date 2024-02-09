#!/bin/bash

# --- Day 1: Not Quite Lisp ---
# https://adventofcode.com/2015/day/1
#
# https://github.com/AJPfleger

echo "--- Day 1: Not Quite Lisp ---"

filename=input.txt

# instructions="()())"
read -r instructions < $filename


# Part 1

floor=0
for (( i=0; i<${#instructions}; i++ )); do
  if [ "${instructions:$i:1}" = "(" ]
  then
    ((floor+=1))
  else
    ((floor-=1))
  fi
done

echo "Part 1: Final floor is ${floor}."


# Part 2

floor=0
for (( i=0; i<${#instructions}; i++ )); do
  if [ "${instructions:$i:1}" = "(" ]
  then
    ((floor+=1))
  else
    ((floor-=1))
  fi

  if [[ floor -eq -1 ]]
  then
    break
  fi
done

echo "Part 2: Reach basement after $((i+1)) instructions."
