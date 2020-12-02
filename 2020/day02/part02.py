#!/usr/bin/env python3
""" AOC day 2 """

import re
tot = 0
m = re.compile(r'(?P<low>\d+)\-(?P<high>\d+)\s(?P<char>[a-z]):\s(?P<password>[a-z]+).*')
raw = []
with open('input.txt') as fd:
    for line in fd:
        res = m.match(line[:-1])
        if res:
            low = int(res.group('low'))
            high = int(res.group('high'))
            target = res.group('char')
            password = res.group('password')
            count = password.count(target)
            good = 0
            if password[low-1] == target:
                good = good + 1

            if password[high-1] == target:
               good = good + 1

            if good == 1:
                tot = tot + 1
                print(f'Password wins {good}: {low} {high} {target} {password}')
            else:
                print(f'Password fails {good}: {low} {high} {target} {password}')
        else:
            print(f'Bad line: {line}')

print(f'There were {tot} good passwords')
