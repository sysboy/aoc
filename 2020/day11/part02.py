#!/usr/bin/env python3.7
""" AOC day 11 """

import sys
grid = []
with open(sys.argv[1]) as fd:
    for line in fd:
        # seat and change
        grid.append([[char,'.'] for char in line[:-1]])


ROWLEN=len(grid)
COLLEN=len(grid[0])

def occupation(g,row,col):
    neighbours = 0
    testr = -99
    testc = -99
    # top
    if row == testr and col == testc:
        print(f'[{row}][{col}] Testing top')
    for r in range(row-1,-1,-1):
        if g[r][col][0] == 'L':
            break
        if g[r][col][0] == '#':
            if row == testr and col == testc:
                print(f'   occupied at [{r}{col}]')
            neighbours += 1
            break
    # bottom
    if row == testr and col == testc:
        print(f'[{row}][{col}] Testing bottom')
    for r in range(row+1,ROWLEN):
        if g[r][col][0] == 'L':
            break
        if g[r][col][0] == '#':
            if row == testr and col == testc:
                print(f'   occupied at [{r}{col}]')
            neighbours += 1
            break
    # left
    if row == testr and col == testc:
        print(f'[{row}][{col}] Testing left')
    for c in range(col-1,-1,-1):
        if g[row][c][0] == 'L':
            break
        if g[row][c][0] == '#':
            if row == testr and col == testc:
                print(f'   occupied at [{row}{c}]')
            neighbours += 1
            break
    # right
    if row == testr and col == testc:
        print(f'[{row}][{col}] Testing right')
    for c in range(col+1,COLLEN):
        if g[row][c][0] == 'L':
            break
        if g[row][c][0] == '#':
            if row == testr and col == testc:
                print(f'   occupied at [{row}{c}]')
            neighbours += 1
            break
    # topleft
    if row == testr and col == testc:
        print(f'[{row}][{col}] Testing topleft')
    for r,c in zip(range(row-1,-1,-1),range(col-1,-1,-1)):
        if g[r][c][0] == 'L':
            break
        if g[r][c][0] == '#':
            if row == testr and col == testc:
                print(f'   occupied at [{r}{c}]')
            neighbours += 1
            break
    # topright
    if row == testr and col == testc:
        print(f'[{row}][{col}] Testing topright')
    for r,c in zip(range(row-1,-1,-1), range(col+1,COLLEN)):
        if g[r][c][0] == 'L':
            break
        if g[r][c][0] == '#':
            if row == testr and col == testc:
                print(f'   occupied at [{r}{c}]')
            neighbours += 1
            break
    # bottomleft
    if row == testr and col == testc:
        print(f'[{row}][{col}] Testing bottom left')
    for r,c in zip(range(row+1,ROWLEN),range(col-1,-1,-1)):
        if g[r][c][0] == 'L':
            break
        if g[r][c][0] == '#':
            if row == testr and col == testc:
                print(f'   occupied at [{r}{c}]')
            neighbours += 1
            break
    # bottomright
    if row == testr and col == testc:
        print(f'[{row}][{col}] Testing bottom right')
    for r,c in zip(range(row+1,ROWLEN),range(col+1,COLLEN)):
        if g[r][c][0] == 'L':
            break
        if g[r][c][0] == '#':
            if row == testr and col == testc:
                print(f'   occupied at [{r}{c}]')
            neighbours += 1
            break

    if row == testr and col == testc:
        print(f'Score for [{row}][{col}] = {neighbours}')

    return neighbours


def update(g):
#    print("Starting update")
    for row in range(ROWLEN):
#        print('-----------')
        for col in range(COLLEN):
#            print(f'Testing [{row},{col}][{g[row][col][0]}]')
            seat = g[row][col][0]
            # floor is never occupied
            if seat == '.':
                g[row][col][1] == seat
                continue

            o = occupation(g,row,col)
#            print(f'score for [{row},{col}] = {o}')
            if o == 0:
#                print(f'occupying [{row},{col}]')
                g[row][col][1] = '#'
            if o >= 5 and g[row][col][0] == '#':
#                print(f'vacating [{row},{col}]')
                g[row][col][1] = 'L'

def check(g):
    changes = 0
    for row in range(ROWLEN):
        for col in range(COLLEN):
            if g[row][col][0] != g[row][col][1]:
                changes = changes + 1
                g[row][col][0] = g[row][col][1]
    return g,changes

def show(g):
    s = 0
    for row in range(ROWLEN):
        print("".join([s[0] for s in g[row]]))
#        print("".join([s[0] for s in g[row]]), " ---> ", "".join([s[1] for s in g[row]]))
        s += "".join([s[0] for s in g[row]]).count('#')
    print(f'{s} occupied seats')


runs = 1
while True:
    print("Run", runs)
    update(grid)
    runs = runs + 1
    grid,changes = check(grid)
    print(f'Changes = {changes}')
    if changes == 0:
        break


show(grid)
print(f'{runs} runs.')
    


