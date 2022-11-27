import sys
input = sys.stdin.readline
n = int(input())
answer = []
for i in range(n):
    answer.append(" "*i+"*"*(2*(n-i)-1))
answer = answer + answer[:-1][::-1]
print("\n".join(answer))
    