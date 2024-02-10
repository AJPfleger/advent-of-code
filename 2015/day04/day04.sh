#!/bin/bash

# --- Day 4: The Ideal Stocking Stuffer ---
# https://adventofcode.com/2015/day/4
#
# https://github.com/AJPfleger

echo "--- Day 4: The Ideal Stocking Stuffer ---"

# This method is quite slow and needs a few hours.

# Part 1

i=0
while : ; do
  echo "${i}"

  # "MD5(stdin)= 000001dbbfa3a5c83a2d506429c7b00e"
  hash=$(echo -n "bgvyzdsv${i}" | openssl md5)

  if [ "${hash:12:5}" = "00000" ]
  then
    break
  fi

  ((i+=1))
done

echo "Part1: Lowest number is ${i}"


# Part 2

while : ; do
  echo "${i}"

  hash=$(echo -n "bgvyzdsv${i}" | openssl md5)

  if [ "${hash:12:6}" = "000000" ]
  then
    break
  fi

  ((i+=1))
done

echo "Part2: Lowest number is ${i}"
