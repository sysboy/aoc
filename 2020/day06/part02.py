#!/usr/bin/env python3

with open('input.txt') as fd:
    DATA = fd.read().strip()

GROUPS = DATA.split('\n\n')

count = 0
for g in GROUPS:
    f = g.split('\n') # this time split rather than join
    a = map(set,f) # make a set out the string

    count = count + len(set.intersection(*a)) # stupid *

print(f'Counts = {count}')
