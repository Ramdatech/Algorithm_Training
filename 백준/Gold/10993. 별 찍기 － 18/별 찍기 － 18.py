import sys
t = sys.stdin.readline
n = int(t())
r = 2**n-1
c = 2*r-1
msk = [[' '] * c for i in range(r)]

def f(x, y, n) :
    nr = 2**n-1
    nc = 2*nr-1

    if n == 1 :
        msk[x][y] = '*'
        return

    if n % 2 == 0 :
        for i in range(nr) :
            tx = x+i
            msk[tx][y+i] = '*'
            msk[tx][y+nc-1-i] = '*'

            if i == 0 :
                for j in range(1, nc-1) :
                    msk[x][y + j] = '*'

        nx, ny = x+1, y+2**(n-1)
    else :
        for i in range(nr-1,-1,-1) :
            tx = x+nr-i-1
            msk[tx][y+i] = '*'
            msk[tx][y+nc-1-i] = '*'
            if i == 0 :
                for j in range(1, nc-1) :
                    msk[x + nr - 1][y + j] = '*'
        nx, ny = x+2**(n-1)-1, y+2**(n-1)
    f(nx, ny, n-1)

f(0, 0, n)
for i in msk :
    print(''.join(i).rstrip())