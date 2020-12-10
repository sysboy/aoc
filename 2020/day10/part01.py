#!/usr/bin/env python3
""" AOC day 10 """

from collections import Counter, defaultdict
import sys


numbers = []
with open('input.txt') as fd:
    for line in fd:
        numbers.append(int(line[:-1]))

#add the extra jolt thingy and the socket
numbers = [0] + sorted(numbers) + [max(numbers) + 3]

print(len(numbers))
pairs = zip(numbers, numbers[1:])

sums = []
for a, b in pairs:
    sums.append(b-a)

diff = Counter(sums)

print (f'{diff[1]} * {diff[3]} = {diff[1]*diff[3]}')
