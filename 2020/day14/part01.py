#!/usr/bin/env python3
""" AOC day 14 """
import sys
import itertools
from collections import defaultdict

import re

ins = []
mask_re = re.compile(r'mask = (?P<mask>\w+)')
mem_re = re.compile(r'mem\[(?P<location>\d+)\]\s=\s(?P<value>\d+)')
f = 0
vals = []
mask = ""
with open(sys.argv[1]) as fd:
    #first line
    line = fd.readline()
    res = mask_re.match(line[:-1])
    mask = res.group('mask')
    #rest
    for line in fd:
        res = mask_re.match(line[:-1])
        if res:
            ins.append([mask,vals])
            vals = []
            mask = res.group('mask')
        res = mem_re.match(line[:-1])
        if res:
            vals.append([int(res.group('location')),int(res.group('value'))])
    ins.append([mask,vals])


def mask_it(mask,num):
    out = ''
    n = f'{num:036b}'
    print(f'number : {n:>36}')
    print(f'mask   : {mask:>36}')
    for i in range(1,len(mask)+1):
        if mask[-i] == 'X':
            out = f'{n[-i]}{out}'
        elif mask[-i] == '1':
            out = f'1{out}'
        elif mask[-i] == '0':
            out = f'0{out}'
        else:
            print(f'wtf - {mask[-i]}')

    print(f'result : {out:>36}\n')
    if out == '':
        return 0
    return int(out,2)

results = defaultdict(int)
for i in ins:
    for v in i[1]:
        loc = v[0]
        val = v[1]
        results[loc] = mask_it(i[0],val)
        
sum = 0
for k in results.keys():
    sum = sum + results[k]
print(sum)

