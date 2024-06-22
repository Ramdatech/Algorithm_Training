n = int(input())
s = 1
for _ in range(n):
    a, b = map(int, input().split())
    if s in [a, b] :
        if s == a : 
            s = b 
        else : 
            s = a
print(s)