def blk1(y, x, f):
    f[y][x] = 1
    f[y-1][x-1] = 0
    f[y-1][x] = 1
    f[y-1][x+1] = 0
    f[y][x-1] = 1
    f[y][x+1] = 1
    f[y+1][x-1] = 0
    f[y+1][x] = 0
    f[y+1][x+1] = 0
    return(f)

def blk2(y, x, f):
    f[y][x] = 0
    f[y-1][x-1] = 1
    f[y-1][x] = 1
    f[y-1][x+1] = 1
    f[y][x-1] = 1
    f[y][x+1] = 0
    f[y+1][x-1] = 0
    f[y+1][x] = 0
    f[y+1][x+1] = 0
    return(f)

def glider(y, x, f):
    f[y][x] = 0
    f[y-1][x-1] = 0
    f[y-1][x] = 1
    f[y-1][x+1] = 0
    f[y][x-1] = 0
    f[y][x+1] = 1
    f[y+1][x-1] = 1
    f[y+1][x] = 1
    f[y+1][x+1] = 1
    return(f)
