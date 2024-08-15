n = int(input())
ls = sorted(list(map(int, input().split())))
print(sum(ls[:n//2]), sum(ls[n//2:]))