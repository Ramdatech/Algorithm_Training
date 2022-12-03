import sys
input = sys.stdin.readline
price = int(input())
price_ls = []
for i in range(9) :
    price_ls.append(int(input()))
print(price - sum(price_ls))