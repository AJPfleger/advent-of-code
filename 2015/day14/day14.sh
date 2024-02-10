#!/bin/bash

# --- Day 14: Reindeer Olympics ---
# https://adventofcode.com/2015/day/14
#
# https://github.com/AJPfleger

echo "--- Day 14: Reindeer Olympics ---"

filename=input.txt

# Part 1
tmax=2503
maxdistance=0
while read line; do

  if [[ $line =~ [A-Za-z]+\ can\ fly\ ([0-9]+)\ km/s\ for\ ([0-9]+)\ seconds,\ but\ then\ must\ rest\ for\ ([0-9]+)\ seconds\. ]]
  then
      v=${BASH_REMATCH[1]}
      tmove=${BASH_REMATCH[2]}
      twait=${BASH_REMATCH[3]}
  else
      echo "Pattern not found in the string."
      continue
  fi

  ((tcycle=tmove+twait))
  ((cycles=tmax/tcycle))
  ((tremainder=tmax-cycles*tcycle))
  ((tmoverremain=tremainder>tmove ? tmove : tremainder))
  ((dist=cycles*v*tmove+v*tmoverremain))
  ((maxdistance=dist>maxdistance ? dist : maxdistance))

done < $filename

echo "Part 1: Max distance is ${maxdistance}."
