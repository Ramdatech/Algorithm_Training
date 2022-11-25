import sys
input = sys.stdin.readline
n, m = map(int,input().strip().split())
li = [x for x in range(1, n+1)]
result = []
while li:
    var = m % len(li) -1
    result.append(str(li[var]))

    if li[var+1:] == li :
        li = li[:var]
    else :
        li = li[var+1:] + li[:var]
print(f'<{", ".join(result)}>')