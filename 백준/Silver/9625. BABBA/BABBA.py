n = int(input())
arr = [1, 0]
for i in range(1, n+1) :
    arr = [arr[1], sum(arr)]
print(*arr)