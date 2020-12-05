#!/usr/bin/env python3
import re

LINES = []
with open('input.txt') as fd:
    for line in fd:
        LINES.append(line[:-1])

#the numbers are just binary with in funky code,
def convert_to_binary(w):
    w = re.sub('[FL]', '0', w)
    w = re.sub('[BR]', '1', w)
    return int(w, 2)


MAX = 0
for line in LINES:
    n = convert_to_binary(line)
    if n > MAX:
        MAX = n

print(MAX)
