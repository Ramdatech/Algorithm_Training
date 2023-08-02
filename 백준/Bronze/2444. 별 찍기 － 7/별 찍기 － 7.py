a = int(input())
a = [" "*(a-i)+"*"*(2*i-1) for i in range(1,a+1)]
for i in a + a[-2::-1]:
    print(i)