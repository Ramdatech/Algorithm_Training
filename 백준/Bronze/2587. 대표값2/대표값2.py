import sys
res = []
for _ in range(5):
    res.append(int(sys.stdin.readline()))
res = sorted(res)
print(int(sum(res)/len(res)))
print(res[2])

    