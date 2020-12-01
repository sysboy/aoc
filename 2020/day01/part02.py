#!/usr/bin/env python3
""" AOC day 1 """
import sys
TOT=2020
raw = []
with open('input.txt') as fd:
    for line in fd:
        raw.append(int(line))

# clever doesn't win...
MAXPOSSIBLE=TOT-min(raw)

for a in sorted(raw):
    for b in sorted(raw):
        if a + b > MAXPOSSIBLE:
            break
        for c in sorted(raw):
            if a + b + c > TOT:
                break
            if a + b + c == 2020:
                print(f'{a},{b},{c}, {a+b+c}, {a*b*c}')
                sys.exit(0)

