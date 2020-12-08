#!/usr/bin/env python3
""" AOC day 8 """
import sys
import copy

code = []
with open('input.txt') as fd:
    for line in fd:
        p = line[:-1].split()
        code.append([p[0],int(p[1]),0])


INS=0
VAL=1
SEEN=2

def process(c):
    pc = 0
    acc = 0

    while True:
        
        if pc > len(c)-1:
            print("Overflow")
            print(acc)
            sys.exit(1)
            return acc

        if c[pc][SEEN] == 1:
            print("Seen")
            return acc

        c[pc][SEEN] = 1

        if c[pc][INS] == "nop":
            pc = pc + 1

        if c[pc][INS] == "acc":
            acc = acc + c[pc][VAL]
            pc = pc + 1

        if c[pc][INS] == "jmp":
            pc = pc + c[pc][VAL]


for i in range(len(code)):
    copied = copy.deepcopy(code)
    if copied[i][INS] == 'jmp':
        copied[i][INS] = 'nop'
    print(process(copied))

