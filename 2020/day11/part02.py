#!/usr/bin/env python3.7
""" AOC day 11 """

import sys
from tkinter import *
import time


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

    for r in range(row - 1, -1, -1):
        if g[r][col][0] == "L":
            break
        if g[r][col][0] == "#":
            neighbours += 1
            break
    # bottom

    for r in range(row + 1, ROWLEN):
        if g[r][col][0] == "L":
            break
        if g[r][col][0] == "#":
            neighbours += 1
            break
    # left

    for c in range(col - 1, -1, -1):
        if g[row][c][0] == "L":
            break
        if g[row][c][0] == "#":
            neighbours += 1
            break
    # right
    for c in range(col + 1, COLLEN):
        if g[row][c][0] == "L":
            break
        if g[row][c][0] == "#":
            neighbours += 1
            break
    # topleft
    for r, c in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if g[r][c][0] == "L":
            break
        if g[r][c][0] == "#":
            neighbours += 1
            break
    # topright
    for r, c in zip(range(row - 1, -1, -1), range(col + 1, COLLEN)):
        if g[r][c][0] == "L":
            break
        if g[r][c][0] == "#":
            neighbours += 1
            break
    # bottomleft
    for r, c in zip(range(row + 1, ROWLEN), range(col - 1, -1, -1)):
        if g[r][c][0] == "L":
            break
        if g[r][c][0] == "#":
            neighbours += 1
            break
    # bottomright
    for r, c in zip(range(row + 1, ROWLEN), range(col + 1, COLLEN)):
        if g[r][c][0] == "L":
            break
        if g[r][c][0] == "#":
            neighbours += 1
            break

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
            if o >= 5 and g[row][col][0] == "#":
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





def plot(row, col, colour):
    offx = row * 10
    offy = col * 10
    points = [offx, offy, offx, offy + 10, offx + 10, offy + 10, offx + 10, offy]
    w.create_polygon(points, outline="#cccccc", fill=colour)


def show_tk(g):
    for row in range(ROWLEN):
        for col in range(COLLEN):
            if g[row][col][0] == ".":
                colour = "black"
            if g[row][col][0] == "#":
                colour = "red"
            if g[row][col][0] == "L":
                colour = "green"
            plot(row, col, colour)


canvas_width = 1000
canvas_height = 1100
tk = Tk()
w = Canvas(tk, width=canvas_width, height=canvas_height)
w.pack()

#show(grid)
show_tk(grid)
tk.update_idletasks()
tk.update()
time.sleep(10)
#tk.update_idletasks()
#tk.update()
#time.sleep(100)
#sys.exit(1)
runs = 1
while True:
    update(grid)
    runs = runs + 1
    #show(grid)
    show_tk(grid)
    tk.update_idletasks()
    tk.update()
    changes = check(grid)
    if changes == 0:
        break
show_tk(grid)
#show(grid)
print(f"{runs} runs.")
time.sleep(100)