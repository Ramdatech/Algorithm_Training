num = 0
maxvar = [0, 0]
while 1:
	num += 1
	try:
		a = int(input())
		if maxvar[0] < a:
			maxvar[0] = a
			maxvar[1] = num
	except:
		break

print(maxvar[0])
print(maxvar[1])
