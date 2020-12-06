#!/usr/bin/env python3

with open('input.txt') as fd:
    DATA = fd.read().strip()

GROUPS = DATA.split('\n\n')

count = 0
for g in GROUPS:
    f = g.replace('\n', '')
    count = count + len(set(f))

print(f'Counts = {count}')
