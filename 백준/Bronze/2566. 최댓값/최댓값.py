li = -1
n = 0
m = 0
for i in range(1, 10):
    a = list(map(int, input().split()))
    b = max(a)
    if b > li:
        li = b
        n = i
        m = a.index(b)+1

print(li)
print(f"{n} {m}")