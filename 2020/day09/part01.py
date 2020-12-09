#!/usr/bin/env python3
""" AOC day 9 """

numbers = []
with open('input.txt') as fd:
    for line in fd:
        numbers.append(int(line[:-1]))

PRE=25
for i, num in enumerate(numbers):
    if i < PRE:
        continue
    pool = numbers[i-PRE:i]
    sums = []
    for a in pool:
        for b in pool:
            sums.append(a+b)
    if num not in sums:
        print(num)
        break
