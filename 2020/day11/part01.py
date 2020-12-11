#!/usr/bin/env python3.7
""" AOC day 11 """

grid = []
with open('input.txt') as fd:
    for line in fd:
        # seat and change
        grid.append([[char,'.'] for char in line[:-1]])


ROWLEN=len(grid)
COLLEN=len(grid[0])

def occupation(g,row,col):
    neighbours = 0
    # top
    if row != 0:
#        print("Testing top")
        if g[row-1][col][0] == '#':
#            print("top")
            neighbours += 1
    # bottom
    if row != ROWLEN-1:
#        print(f'[{row}][{col}] Testing bottom')
        if g[row+1][col][0] == '#':
#            print("   bottom")
            neighbours += 1
    # left
    if col != 0:
#        print(f'[{row}][{col}] Testing left')
        if g[row][col-1][0] == '#':
#            print("  left")
            neighbours += 1
    # right
    if col != COLLEN-1:
#        print(f'[{row}][{col}] Testing right')
        if g[row][col+1][0] == '#':
#            print("  right")
            neighbours += 1
    # topleft
    if row !=0 and col !=0:
        if g[row-1][col-1][0] == '#':
#            print("topleft")
            neighbours += 1
    # topright
    if row !=0 and col != COLLEN-1:
        if g[row-1][col+1][0] == '#':
#            print("topright")
            neighbours += 1
    # bottomleft
    if row != ROWLEN-1 and col !=0:
#        print(f'[{row}][{col}] Testing bottom left')
        if g[row+1][col-1][0] == '#':
#            print("   bottomleft")
            neighbours += 1
    # bottomright
    if row != ROWLEN-1 and col != COLLEN-1:
#        print(f'[{row}][{col}] Testing bottom right')
        if g[row+1][col+1][0] == '#':
#            print("  bottomright")
            neighbours += 1
#    print(f'Score for [{row}][{col}] = {neighbours}')
    if row == 0 and col == 0:
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
            if o >= 4 and g[row][col][0] == '#':
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


show(grid)
runs = 1
while True:
    print("Run", runs)
    update(grid)
    runs = runs + 1
#    show(grid)
    grid,changes = check(grid)
    print(f'Changes = {changes}')
    if changes == 0:
        break


show(grid)
print(f'{runs} runs.')
    


