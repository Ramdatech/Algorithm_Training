a = int(input())
a = [" "*(a-i)+"*"*(2*i-1) for i in range(1,a+1)]
t = a+a[-2::-1]
print(*t, sep="\n")