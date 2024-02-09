#!/bin/bash

# --- Day 2: I Was Told There Would Be No Math ---
# https://adventofcode.com/2015/day/2
#
# https://github.com/AJPfleger

echo "--- Day 2: I Was Told There Would Be No Math ---"

filename=input.txt

# lxwxh
# area = 2*l*w + 2*w*h + 2*h*l

area=0
length=0
while read line; do

  l=$(echo "${line}" | cut -d "x" -f 1)
  w=$(echo "${line}" | cut -d "x" -f 2)
  h=$(echo "${line}" | cut -d "x" -f 3)

  lw=$((l*w))
  wh=$((w*h))
  hl=$((h*l))

  smallface=$lw
  if [[ smallface -gt wh ]]
  then
    smallface=$wh
  fi
  if [[ smallface -gt hl ]]
  then
    smallface=$hl
  fi

  longside=$l
  if [[ longside -lt w ]]
  then
    longside=$w
  fi
  if [[ longside -lt h ]]
  then
    longside=$h
  fi

  # length = 2 * (l+w+h - longside)
  area=$((area+2*(lw+wh+hl)+smallface))
  length=$((length+2*(l+w+h-longside)+l*w*h))
done < $filename

echo "Part 1: Total area is ${area} square feet."
echo "Part 2: Total length is ${length} feet."
