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
    print()
    out = ['']
    n = f'{num:036b}'
    print(f'number : {n:>36} {int(n,2)}')
    print(f'mask   : {mask:>36}')
    for i in range(1,len(mask)+1):
        if mask[-i] == 'X':
            for j in range(0,len(out)):
                o = out[j]
                out[j] = f'1{o}'
                out.append(f'0{o}')
        elif mask[-i] == '1':
            for j in range(0,len(out)):
                out[j] = f'1{out[j]}'
        elif mask[-i] == '0':
            for j in range(0,len(out)):
                out[j] = f'{n[-i]}{out[j]}'
        else:
            print(f'wtf - {mask[-i]}')

    for j in range(0,len(out)):
        print(f'result : {out[j]:>36} {int(out[j],2)}')
    return out

results = defaultdict(int)
for i in ins:
    for v in i[1]:
        loc = v[0]
        val = v[1]
        addrs = mask_it(i[0],loc)
        for a in addrs:
            results[a] = val
        
sum = 0
for k in results.keys():
    sum = sum + results[k]
print(sum)


