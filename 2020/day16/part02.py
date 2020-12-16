#!/usr/bin/env python3.7
""" AOC day 16 """

import sys,re,copy,time


#departure location: 26-715 or 727-972
m = re.compile(r'^(?P<rule>[class]+): (?P<l1>\d+)\-(?P<h1>\d+]) or (?P<l2>\d+)\-(?P<h2>\d+])')
m = re.compile(r'(?P<rule>[departure location]+): (?P<l1>[0-9]+)=(?P<h1>[0-9]+) or (?P<l2>[0-9]+)-(?P<h2>[0-9]+)')

ranges = {}
myticket = []
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
            t = []
            for n in line[:-1].split(','):
                t.append(int(n))
            nearby.append(t)
            continue
        if inticket:
            for n in line[:-1].split(','):
                myticket.append(int(n))
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
    v1 = set(range(ranges[r][0], ranges[r][1] + 1))
    v2 = set(range(ranges[r][2], ranges[r][3] + 1))
    ranges[r].append(v1)
    ranges[r].append(v2)
    valid |= v1
    valid |= v2

s = 0
valid_tickets = []
for ticket in nearby:
    good = 1
    for num in ticket:
        if num not in valid:
            s = s + num
            good = 0
    if good:
        valid_tickets.append(ticket)

print(f'Sum = {s}')
#valid_tickets.append(myticket)

print()
field_order = {}
fields = []
rgs = copy.deepcopy(ranges)
# dict of the columns
columns = {}
for f in range(0,len(myticket)):
    columns[f] = set(x[f] for x in valid_tickets)

while True:
    for c in columns.keys():
        possible_matches = 0
        matching_range = 0
        matching_column = 0
        print('----------------------------------------------')
        column = columns[c]
        print(f'    column {c}, ranges left = {len(rgs.keys())}')
        print(f'    ranges to choose: {rgs.keys()}')
        print(f'    columns to choose: {columns.keys()}')
        for r in rgs.keys():
            if column.issubset( (ranges[r][4] | ranges[r][5] )):
                print(f'match {r},{c}')
                possible_matches = possible_matches + 1
                matching_range = r
                matching_column = c

        print(f'    possible ranges matched = {possible_matches}')
        if possible_matches == 1:
            print(f'    ****MATCH**** popping')
            field_order[matching_range] = matching_column
            print(f'        cols now : {field_order}')
            rgs.pop(matching_range)
            columns.pop(matching_column)
            break
        else:
            print(f'    NO MATCH, next column')
    if len(columns) == 0:
        break


print(field_order)

s = 1
for k in field_order.keys():
    if k.find('departure') != -1:
        print(f'{k} = {myticket[field_order[k]]}')
        s = s * myticket[field_order[k]]

print(s)
