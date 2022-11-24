def selfnum(a):
	num = 0
	targetnum = a
	for i in str(targetnum):
		num += targetnum%10
		targetnum = targetnum//10
	targetnum = a + num
	return targetnum
	

c = list(range(1, 10000))
arr =set()

num = 0
while 1 :
	try:
		a = c[num]
		num += 1
		while (1):
			a = selfnum(a)
			if a < 10000 and a in c:
				c.remove(a)
			else :
				break
	except:
		break

res = c
for i in res:
	print(i)