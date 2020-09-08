import render, constructor, copy
from random import randint as r

# x is the width of the area, and y is the height ( x or y Max)
ym = 100
xm = round(3*ym)



# World Variables
# f -> Current Frame
f = []
fix = []
rValue = 1


# I don't know if this was working correctly
for i in range(xm):
    fix.append(0)

for i in range(ym):
    f.append(fix.copy())



# Initialize next frame. Deepcopy required
    # because "If the list contains objects and you want to copy them as well, use generic copy.deepcopy()"
fn = copy.deepcopy(f)

# Define a cell at the center of the grid
f = constructor.blk2(int(ym/2), int(xm/2), f)


render.Figure.plot(f)
input('Initial shown: ')

def ran():
    # Randomly spawn cells
    for i in range(ym):
        for j in range(xm):
            if r(1,1000) > (1000-rValue):
                f[i][j] = 1

def count(y, x):
    # Number of surrounding cells surrounding current cell
    c = 0

    # Lower bound
    ya = y - 1
    xa = x - 1

    # Upper bound
    yb = y + 1
    xb = x + 1

    # Check lower bounds

    if ya <= 0:
        ya = 0
        c -= 1
    if xa <= 0:
        xa = 0
        c -= 1
    if yb >= ym:
        yb = ym - 1
        c -= 1
    if xb >= xm:
        xb = xm -1
        c -= 1

    # Count surrounding cells
    if f[ya][xa] == 1:
        c +=1

    if f[ya][x] == 1:
        c +=1

    if f[ya][xb] == 1:
        c +=1

    if f[y][xa]  == 1:
        c +=1

    if f[y][xb] == 1:
        c +=1

    if f[yb][xa] == 1:
        c +=1

    if f[yb][x] == 1:
        c +=1

    if f[yb][xb] == 1:
        c +=1

    # Set current cell value based off of count
    if c == 2 and f[y][x] == 1:
        fn[y][x] = 1
    elif c == 3 and f[y][x] == 1:
        fn[y][x] = 1
    elif c == 3 and f[y][x] == 0:
        fn[y][x] = 1
    else:
        fn[y][x] = 0



def loop():
    global f
    global fn
    # Iterate through a frame
    for i in range(ym):
        for j in range(xm):
            count(i,j)
    f = copy.deepcopy(fn)
    render.Figure.plot(f)

run = True
while run == True:
    loop()
    ran()
