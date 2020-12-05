#!/usr/bin/env python3
import re

LINES = []
with open('input.txt') as fd:
    for line in fd:
        LINES.append(line[:-1])

#the numbers are just binary with some funky code,
#just convert them
def convert_to_binary(w):
    w = re.sub('[FL]', '0', w)
    w = re.sub('[BR]', '1', w)
    return int(w, 2)


SEAT_IDS = []
for line in LINES:
    SEAT_IDS.append(convert_to_binary(line))

# our seat is not in the list so make a list of all
ALL_SEATS = range(min(SEAT_IDS), max(SEAT_IDS)+1)
print(set(ALL_SEATS) - set(SEAT_IDS))
