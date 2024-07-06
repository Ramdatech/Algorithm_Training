a, b = input().split()
a, n = a.lower(), len(a)

segments, i = [], 0
vst, res = set(), ""

while i < n:
    start = i
    while i < n and a[i] == a[start]:
        i += 1
    segments.append((a[start], i - start))

for c, lt in segments:
    if c in vst : continue
    if lt >= int(b):
        res += '1'
    else:
        res += '0'
    vst.add(c)

print(res)