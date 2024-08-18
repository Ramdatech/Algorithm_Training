A, B = [sum(i) for i in zip(*[[1,0] if x>y else [0,1] for x, y in zip(*[map(int, input().split()) for _ in range(2)]) if x!=y])]
if A > B :
    print("A")
elif A < B :
    print("B")
else :
    print("D")