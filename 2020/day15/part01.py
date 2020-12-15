#!/usr/bin/env python3.7
""" AOC day 15 """

from collections import defaultdict
from itertools import count

numbers = []
with open('input.txt') as fd:
    for line in fd:
        for n in line.split(','):
            numbers.append(int(n))
        
print( numbers)

data = defaultdict(list)

for i in count(1):

    if i <= len(numbers):
        n = numbers[i-1]

    elif len(data[last]) == 1:
        n = 0

    else:
        n = data[last][-1] - data[last][-2]

    if i == 30000000:
        break
    data[n].append(i)
    last = n
    #print(i+3,data)


print(n)
