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


def bag_count(rules,bag):
    sum = 1
    for n,s in rules[bag]:
        sum = sum + n*bag_count(rules,s)
    return sum


print(bag_count(rules,'shiny gold') -1)
