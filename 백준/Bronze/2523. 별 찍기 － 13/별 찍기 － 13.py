n = int(input())
for i in range(1,2*n):
    print("*"*(2*n-i) if i > n else "*"*i)