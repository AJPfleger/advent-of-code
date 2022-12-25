#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 07:34:00 2022

@author: AJPfleger

https://adventofcode.com/2022/day/25
"""


def parse_file(filename):
    file = open(filename, "r")
    lines = file.readlines()

    numbers = []

    for l in lines:
        numbers.append(l.strip())

    return numbers


def b11_to_b10(n_b11):
    n_digits = len(n_b11)
    n_b10 = 0
    for d in reversed(range(n_digits)):

        digit = n_b11[n_digits - 1 - d]

        if digit.isnumeric():
            digit = int(digit)
        else:
            if digit == "-":
                digit = -1
            else:
                digit = -2

        converted_digit = 5 ** d * digit

        n_b10 += converted_digit

    return n_b10


def b10_to_b11(n_b10):
    n_b5 = b10_to_b5(n_b10)

    l_b11 = []
    overflow = 0
    for d in reversed(range(len(n_b5))):

        d5 = n_b5[d] + overflow

        if d5 < 3:
            l_b11.append(str(d5))
            overflow = 0
        elif d5 == 3:
            l_b11.append("=")
            overflow = 1
        else:  # d5 == 4:
            l_b11.append("-")
            overflow = 1

    while l_b11[-1] == "0":
        l_b11.pop(-1)

    n_b11 = "".join(l_b11)[::-1]

    return n_b11


def b10_to_b5(n_b10):
    n_digits = 0
    while int(n_b10 / 5 ** n_digits) > 0:
        n_digits += 1

    n_b5 = [0]

    for d in reversed(range(n_digits)):
        n_b5.append(int(n_b10 / 5 ** d))
        n_b10 = n_b10 % 5 ** d

    return n_b5


def sum_b11_list(numbers_b11):
    sum_b10 = 0
    for n_b11 in numbers_b11:
        sum_b10 += b11_to_b10(n_b11)

    return b10_to_b11(sum_b10)


filename = "input.txt"

print("\n*** Part 1 ***")
numbers_b11 = parse_file(filename)
sum_b11 = sum_b11_list(numbers_b11)
print(f"SNAFU number: {sum_b11}")

print("\n*** Part 2 ***")
print("SPOILER: There is no part 2")
