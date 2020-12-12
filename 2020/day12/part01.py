#!/usr/bin/env python3
""" AOC day 12 """
from collections import deque
import sys

ins = []
with open(sys.argv[1]) as fd:
    for line in fd:
        ins.append([line[0],int(line[1:])])


facing = deque(['E','S','W','N'],maxlen=4)

location = [0,0]
x = 0
y = 1

for i in ins:

    direction = i[0]
    steps = i[1]

    if direction == 'L':
            facing.rotate(int(steps/90))
    if direction == 'R':
            facing.rotate(int(steps/-90))

    tempdir = direction

    if direction == 'F':
        tempdir = facing[0]

    if tempdir == 'N':
        location[y] = location[y] + steps

    if tempdir == 'S':
        location[y] = location[y] - steps

    if tempdir == 'E':
        location[x] = location[x] + steps

    if tempdir == 'W':
        location[x] = location[x] - steps

print(f'location = {location}, result = {abs(location[0]) + abs(location[1])}')
