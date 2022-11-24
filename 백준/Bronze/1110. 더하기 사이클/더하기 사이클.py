var1 = int(input())
res = var1
num = 1
while(1):
	a = var1//10
	b = var1%10
	c = b*10 + (a+b)%10
	if res == c :
		break
	else :
		var1 = c
		num += 1
print(num)