#!/usr/bin/env python3.7
""" AOC day 11 """

import sys

grid = []
with open(sys.argv[1]) as fd:
    for line in fd:
        # seat and change
        grid.append([[char, "."] for char in line[:-1]])


ROWLEN = len(grid)
COLLEN = len(grid[0])


def occupation(g, row, col):
    neighbours = 0
    # top
    if row != 0:
        if g[row - 1][col][0] == "#":
            neighbours += 1
    # bottom
    if row != ROWLEN - 1:
        if g[row + 1][col][0] == "#":
            neighbours += 1
    # left
    if col != 0:
        if g[row][col - 1][0] == "#":
            neighbours += 1
    # right
    if col != COLLEN - 1:
        if g[row][col + 1][0] == "#":
            neighbours += 1
    # topleft
    if row != 0 and col != 0:
        if g[row - 1][col - 1][0] == "#":
            neighbours += 1
    # topright
    if row != 0 and col != COLLEN - 1:
        if g[row - 1][col + 1][0] == "#":
            neighbours += 1
    # bottomleft
    if row != ROWLEN - 1 and col != 0:
        if g[row + 1][col - 1][0] == "#":
            neighbours += 1
    # bottomright
    if row != ROWLEN - 1 and col != COLLEN - 1:
        if g[row + 1][col + 1][0] == "#":
            neighbours += 1

    return neighbours


def update(g):
    for row in range(ROWLEN):
        for col in range(COLLEN):
            seat = g[row][col][0]
            # floor is never occupied
            if seat == ".":
                g[row][col][1] == seat
                continue

            o = occupation(g, row, col)
            if o == 0:
                g[row][col][1] = "#"
            if o >= 4 and g[row][col][0] == "#":
                g[row][col][1] = "L"


def check(g):
    changes = 0
    for row in range(ROWLEN):
        for col in range(COLLEN):
            if g[row][col][0] != g[row][col][1]:
                changes = changes + 1
                g[row][col][0] = g[row][col][1]
    return changes


def show(g):
    s = 0
    for row in range(ROWLEN):
        print("".join([s[0] for s in g[row]]))
        s += "".join([s[0] for s in g[row]]).count("#")
    print(f"{s} occupied seats")


show(grid)
runs = 1
while True:
    update(grid)
    runs = runs + 1
    show(grid)
    changes = check(grid)
    if changes == 0:
        break

show(grid)
print(f"{runs} runs.")
