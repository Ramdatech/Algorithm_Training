a = [x for x in [int(input()) for i in range(7)] if x%2 == 1]
if len(a) == 0 :
    print(-1)
else :
    print(sum(a), min(a), sep='\n')