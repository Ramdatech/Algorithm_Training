R, C, a, b = map(int, input().split()+input().split())
for r in range(R*a) :
    print(*["X."[(r//a+c//b)%2] for c in range(C*b)], sep="")