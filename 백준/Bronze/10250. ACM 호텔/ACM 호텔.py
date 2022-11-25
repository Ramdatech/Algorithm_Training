n = int(input())
for _ in range(n):
    a,b,c = map(int, input().split())
    t = 0
    if c%a == 0 :
        x = a
        y = c//a
    else :
        x = c%a
        y = c//a +1
    
    print(f'{x}{str(y).zfill(2)}')