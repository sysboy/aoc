#!/usr/bin/env python3
""" AOC day 3 """

import sys

DX = int(sys.argv[1])
DY = int(sys.argv[2])
ROWS = []
MAX = 0

with open('input.txt') as fd:
    for line in fd:
        ROWS.append(line[:-1])

MAX = len(ROWS[0])
X = 0 # X pos in the row
Y = 0 # Y number of row
COUNT = 0

while True:
    MODX = X%MAX # I hope the rows are all the same
    if ROWS[Y][MODX] == '#':
        print(f'{ROWS[Y][:MODX]}X{ROWS[Y][MODX+1:]} {Y},{MODX}')
        COUNT = COUNT + 1
    else:
        print(f'{ROWS[Y][:MODX]}O{ROWS[Y][MODX+1:]} {Y},{MODX}')

    X = X + DX
    Y = Y + DY

    if Y >= len(ROWS):
        break
    
print(f'Tree count = {COUNT}')


