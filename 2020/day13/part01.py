#!/usr/bin/env python3
""" AOC day 13 """
import sys
import itertools

earliest = 0
bus_times = []
with open(sys.argv[1]) as fd:
    earliest = int(fd.readline())
    times = fd.readline()
    for t in times.split(','):
        if t != 'x':
            bus_times.append(int(t))


for t in itertools.count(earliest):
    for b in bus_times:
        if t % b == 0:
            print(f'Bus {b} at {t}, after {t-earliest}, result = {b*(t-earliest)}')
            sys.exit(1)
   
