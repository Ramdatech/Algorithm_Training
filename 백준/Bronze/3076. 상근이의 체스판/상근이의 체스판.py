R, C = map(int, input().split())
a, b = map(int, input().split())
for r in range(R*a) :
    for c in range(C*b) :
        print("X."[(r//a+c//b)%2], end="")
    print()