import sys
t = sys.stdin.readline
def f(n,m) :
    A, B = M = [[], []]
    AS=BS=0
    for _ in range(n) :
        a, b = map(int, t().split())
        if a-1 or m<=b : M[a-1]+=[b]
        else : m+=b
    A.sort(); B.sort()
    AL, BL =len(A),len(B)
    while 1 :
        while AS < AL and m > A[AS]:
            m += A[AS]; AS += 1
        while AS < AL and BS < BL and m <= A[AS]:
            m *= B[BS]; BS += 1
        if AS == AL or A[AS] >= m : return n-AL+AS
print(f(*map(int, t().split())))