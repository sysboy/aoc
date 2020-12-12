#!/usr/bin/env python3
""" AOC day 12 """
import sys

ins = []
with open(sys.argv[1]) as fd:
    for line in fd:
        ins.append([line[0],int(line[1:])])

location = [0,0]
waypoint = [10,1]
x = 0
y = 1

for i in ins:

    direction = i[0]
    steps = i[1]

#    print(f'Move {direction} {steps}')
    if direction == 'L':
        t = int(steps/90)
        if t == 1:
            waypoint = [-waypoint[y], waypoint[x]]
        if t == 2:
            waypoint = [-waypoint[x], -waypoint[y]]
        if t == 3:
            waypoint = [waypoint[y], -waypoint[x]]
    if direction == 'R':
        t = int(steps/90)
        if t == 1:
            waypoint = [waypoint[y], -waypoint[x]]
        if t == 2:
            waypoint = [-waypoint[x], -waypoint[y]]
        if t == 3:
            waypoint = [-waypoint[y], waypoint[x]]

    if direction == 'F':
        location[x] = location[x] + waypoint[x]*steps
        location[y] = location[y] + waypoint[y]*steps

    if direction == 'N':
        waypoint[y] = waypoint[y] + steps

    if direction == 'S':
        waypoint[y] = waypoint[y] - steps

    if direction == 'E':
        waypoint[x] = waypoint[x] + steps

    if direction == 'W':
        waypoint[x] = waypoint[x] - steps

#    print(f'Location   {location[x]},{location[y]}')
#    print(f'Waypoint   {waypoint[x]},{waypoint[y]}')

print(f'location = {location}, result = {abs(location[0]) + abs(location[1])}')
