_, a, b = map(int, input().split())
mx=0
while a!=b: a,b=(a+1)//2,(b+1)//2; mx+=1
print(mx)