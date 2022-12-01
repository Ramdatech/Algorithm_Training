import sys
input = sys.stdin.readline
n = int(input().strip())
ls = list(map(int,input().strip().split()))
m = int(input().strip())
ls2 = list(map(int,input().strip().split()))
ls.sort()
answer = []
dicty = {}
for goal in sorted(list(set(ls))):
    start, end = 0, n-1
    while 1 :
        mid = (start+end)//2
        if ls[mid] >= goal :
            end = mid
        elif ls[mid] < goal :
            start = mid+1
        if start >= end :
            answer.append([ls[end], n-end])
            break
for i in range(1, len(answer)) :
    dicty[answer[i-1][0]] = answer[i-1][1] - answer[i][1]
else :
    dicty[answer[-1][0]] = answer[-1][1]
for i in ls2:
    print(dicty.get(i,0), end=" ")