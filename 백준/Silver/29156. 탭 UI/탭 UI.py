import sys 
t = sys.stdin.readline
N = int(t().strip())
ls = []
sum_ls = [0]
for _ in range(N) :
	n = int(t().strip())
	ls.append(n)
	sum_ls.append(sum_ls[-1]+n)
L = int(t().strip())
Q = int(t().strip())
for _ in range(Q) :
	click = int(t().strip()) - 1
	total_dist = min(sum_ls[click] + ls[click]/2 -L/2, sum_ls[-1]-L)
	pos = max(0, total_dist)
	print(f"{pos:.2f}")