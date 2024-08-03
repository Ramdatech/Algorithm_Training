n, d = int(input()), int(input())
for i in range(100):
    if (n//100*100 + i)%d == 0 :
        print(str(i).zfill(2))
        break