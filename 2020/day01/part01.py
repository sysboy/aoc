#!/usr/bin/env python3
""" AOC day 1 """
TOT=2020

def check(a,b):
    # if the numbers are too big, return
    if min(a) > TOT/2 and min(b) > TOT/2:
        return None
    for num in a:
        MAX=TOT-num
        for num2 in b:
            if num2 > MAX:
                break
            if num + num2 == TOT:
                print(f'RES: {num*num2}')
                return[num,num2]

raw = []
with open('input.txt') as fd:
    for line in fd:
        raw.append(int(line))

TOT=2020
print(f'There are {len(raw)} lines')
print(f'Min is {min(raw)}')
print(f'Max is {max(raw)}')

MAXPOSSIBLE=TOT-min(raw)

bucket={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
for num in sorted(raw):
    if num <= MAXPOSSIBLE:
        bucket[num%10].append(num)

import pprint
pprint.pprint(bucket)

#0's
print(check(bucket[0],bucket[0]))
#1's
print(check(bucket[1],bucket[9]))
#2's
print(check(bucket[2],bucket[8]))
#3's
print(check(bucket[3],bucket[7]))
#4's
print(check(bucket[4],bucket[6]))
#5's
print(check(bucket[5],bucket[5]))



