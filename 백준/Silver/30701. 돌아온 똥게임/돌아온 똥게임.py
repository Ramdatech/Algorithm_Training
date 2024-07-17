import sys
t = sys.stdin.readline
n, m = map(int, t().split())
M = [[], []]
AS=BS=0
for _ in range(n) :
    a, b = map(int, t().split())
    if a == 1 and m > b :
        m += b
    else :
        M[a-1]+=[b]
(A, AL), (B, BL) = [[sorted(x), len(x)] for x in M]
while 1 :
    while AS < AL and m > A[AS]:
        m += A[AS]
        AS += 1
    while AS < AL and BS < BL and m <= A[AS]:
        m *= B[BS]
        BS += 1
    if AS == AL or A[AS] >= m :
        break
print(n-(AL-AS))