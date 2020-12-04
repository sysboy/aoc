#!/usr/bin/env python3
import re
import sys
import pprint


PASSPORTS = []
with open('tidy.data') as fd:
    for line in fd:
        codes = re.findall(r'(\w+):(\S+)', line[:-1])
        PASSPORTS.append({c[0]: c[1] for c in codes})

def check(passport):
    try:
        byr = int(pp['byr'])
        if byr < 1920 or byr > 2002:
            return 0

        iyr = int(pp['iyr'])
        if iyr < 2010 or iyr > 2020:
            return 0

        eyr = int(pp['eyr'])
        if eyr < 2020 or eyr > 2030:
            return 0

        hgt = pp['hgt']
        m = re.match(r'(\d+)(cm|in)', hgt)
        height, unit = int(m[1]), m[2]
        if unit == 'cm':
            if height < 150 or height > 193:
                return 0
        elif unit == 'in':
            if height < 59  or height > 76:
                return 0
        else:
            return 0 # no units

        hcl = pp['hcl']
        if hcl[0] != '#' or len(hcl) != 7:
            return 0
        # convert from hex to check if valid
        int(hcl[1:],16)

        ecl = pp['ecl']
        if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return 0

        pid = pp['pid']
        if not pid.isdigit() or len(pid) != 9:
            return 0

        return 1 # made it
    except:
        return 0
    

count = 0
for pp in PASSPORTS:
    count = count + check(pp)

print(f'Valid = {count}')
