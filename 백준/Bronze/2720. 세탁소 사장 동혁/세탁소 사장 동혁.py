n = int(input())
for i in range(n) :
	p = int(input())
	res = []
	for j in [25, 10, 5, 1]:
		res.append(p//j)
		p = p%j
	print(*res)