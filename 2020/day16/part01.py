#!/usr/bin/env python3.7
""" AOC day 16 """

import sys,re


#departure location: 26-715 or 727-972
m = re.compile(r'^(?P<rule>[class]+): (?P<l1>\d+)\-(?P<h1>\d+]) or (?P<l2>\d+)\-(?P<h2>\d+])')
m = re.compile(r'(?P<rule>[departure location]+): (?P<l1>[0-9]+)=(?P<h1>[0-9]+) or (?P<l2>[0-9]+)-(?P<h2>[0-9]+)')

ranges = {}
tickets = []
nearby = []
inticket = 0
innearby = 0
with open(sys.argv[1]) as fd:
    for line in fd:
        if line[:-1] == '':
            continue
        if line.find("your ticket") != -1:
            inticket = 1
            continue
        if line.find("nearby tickets") != -1:
            innearby = 1
            continue
        
        if innearby:
            for n in line[:-1].split(','):
                nearby.append(int(n))
            continue
        if inticket:
            for n in line[:-1].split(','):
                tickets.append(int(n))
            continue
        a = line[:-1].split(':')
        rule = a[0].strip()
        b = a[1].split(' or ')
        l1,h1 = b[0].split('-')
        l2,h2 = b[1].split('-')
        ranges[rule]= [int(l1),int(h1),int(l2),int(h2)]


# build a list of all the valid numbers
valid = set()
for r in ranges.keys():
    valid |= set(range(ranges[r][0], ranges[r][1] + 1))
    valid |= set(range(ranges[r][2], ranges[r][3] + 1))

s = 0
for num in nearby:
    if num not in valid:
        print(num)
        s = s + num
print(f'Sum = {s}')

