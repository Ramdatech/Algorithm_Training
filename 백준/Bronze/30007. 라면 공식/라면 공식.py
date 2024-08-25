n = int(input())
for _ in range(n):
    a, c, b = map(int, input().split())
    print(a*(b-1)+c)