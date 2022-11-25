num = int(input())
res = 0
for _ in range(num) :
    a = input().strip()
    b = sorted(a)
    li = [0, 0]

    for i in range(1, len(a)) :
        if a[i] != a[i-1] :
            li[0] += 1
        if b[i] != b[i-1] :
            li[1] += 1

    if li[0] == li[1] :
        res += 1

print(res)