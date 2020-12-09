#!/usr/bin/env python3
""" AOC day 9 """
import sys

numbers = []
with open('input.txt') as fd:
    for line in fd:
        numbers.append(int(line[:-1]))

PRE=25
MYNUM=0
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
        MYNUM=num
        break

#1,2,3,4,5
#add all the pairs, triples, quads etc
for a in range(2, len(numbers)): #  3,4,5...
    for b in range(len(numbers) - a): # 1,2 [1:3] [2:4]
        pool = numbers[b:b+a]
        #print(f'>>{len(pool)}: {pool}')
        if MYNUM == sum(pool):
            print(f'{min(pool)},{max(pool)},{min(pool)+max(pool)}')
            sys.exit(0)
