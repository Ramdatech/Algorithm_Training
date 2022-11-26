a = input
n, m = map(int, a().split())
li = []
for _ in range(n*2):
    li += map(int, a().split())
ans = [str(li[x]+li[m*n+x]) for x in range(m*n)]
for i in range(n):
    print(" ".join(ans[m*i:m*(i+1)]))