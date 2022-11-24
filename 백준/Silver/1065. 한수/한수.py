import sys
a = int(sys.stdin.readline().strip())
res = [(x//100+x%10==x%100//10*2)|(x<100) for x in range(1, a+1)]      
print(sum(res))