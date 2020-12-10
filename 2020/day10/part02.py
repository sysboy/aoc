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


print(f'Numbers = {numbers}')
# store the paths in a dict
p = defaultdict(int)
p[0] = 1

for a in range(1, len(numbers)):
    print(f'a = {a}')
    print(f'numbers = {numbers[:a+1]}')
    print(f'    range = {range(a)} ')
    print(f'    range = {range(a)[::-1]} ')
    #check from the end, work out how many paths before we get over 3 diff
    for z in range(a)[::-1]:
        print(f'        z = {z}')
        print(f'        a - z  {numbers[a]} - {numbers[z]} = {numbers[a] - numbers[z]}')
        if numbers[a] - numbers[z] > 3:
            print(f'        Paths for this number p[{a}] = {p[a]}')
            print(f'        ** end of chain **')
            # There are no more new paths, next!
            break
        print(f'        Paths p[{a}] = {p[a]}')
        print(f'        Add p[{z}] = {p[z]}')
        print(f'        Sum {p[a] + p[z]}')
        #add the number of the paths for the previous number to our total for
        #this one
        p[a] = p[a] + p[z]

print(p)
print(p[len(numbers)-1])
