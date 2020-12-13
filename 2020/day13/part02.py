#!/usr/bin/env python3.7
""" AOC day 13 """
import sys
import itertools

earliest = 0
bus_times = []
with open(sys.argv[1]) as fd:
    earliest = int(fd.readline())
    times = fd.readline()
    c = 0 # This is how much offset we need from the first bus
    for t in times.split(','):
        if t != 'x':
            bus_times.append([c,int(t)])
        c = c - 1

# stolen from
# https://github.com/TheAlgorithms/Python/blob/master/blockchain/chinese_remainder_theorem.py
def euclid(a,b):
    if b == 0:
        return(1,0)
    (x,y) = euclid(b, a%b)
    k = a // b
    return(y,x-k*y)


def crt(n,r):
    x,y = euclid(n[0],n[1])
    print(x,y)
    m = n[0]*n[1]
    n = r[1] * x * n[0] + r[0] * y * n[1]
    return (n % m + m) % m, m

offsets = [x[0] for x in bus_times]
busses = [x[1] for x in bus_times]
print(busses)
print(offsets)

a,b = crt(busses[:2], offsets[:2])

print(a,b)
# loop through the rest of the numbers as any earlier one will be a factor of
# too.
for i in range(2,len(bus_times)):
    c,d = crt([b,busses[i]],[a,offsets[i]])
    print(c,d)
    a = c
    b = d
