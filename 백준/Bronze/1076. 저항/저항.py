import sys
tab = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
t = sys.stdin.readline
def f(a,b,c):
    return (a*10+b)*10**c
print(f(*[tab[t().strip()] for _ in range(3)]))