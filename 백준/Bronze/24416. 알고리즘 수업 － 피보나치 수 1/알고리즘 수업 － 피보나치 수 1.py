dp = {1:1, 2:1}
def fib(n) :
	if n in dp.keys() :
		return dp[n]
	else :
		dp[n] = fib(n-1) + fib(n-2)
		return dp[n]

def fibo(n):
	res = 0
	ls = [0, 1, 1]
	
	for i in range(3, n+1):
		ls.append(ls[i-1] + ls[i-2])
		res += 1
	return res
	
import sys
t = int(sys.stdin.readline())
print(fib(t), fibo(t))