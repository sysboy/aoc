#!/usr/bin/env python3.7

rules = {}
with open('input.txt') as fd:
    for line in fd:
        words = line[:-1].split()
        this_bag = words[0]+ " " + words[1]
        rules[this_bag] = []
        b = line[:-1].split('contain')
        bags = b[1].split(',')
        for bag in bags:
            words = bag.split()
            count = 0
            try:
                count = int(words[0])
            except:
                break
            new_bag = [count,words[1]+" "+words[2]]
            rules[this_bag].append(new_bag)


def contains(rules, find):
    res = []
    for f in find:
        for rule in rules:
            for bag in rules[rule]:
                if f in bag:
                    res.append(rule)
    return res

search_for = ['shiny gold']
final = {}
while True:
    res = contains(rules,search_for)
    if res == []:
        break
    for bag in res:
        final[bag] = 1
    search_for = res

print(final.keys())
print(len(final))
