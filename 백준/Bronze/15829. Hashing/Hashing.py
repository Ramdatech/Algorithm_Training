import sys
input = sys.stdin.readline
n = int(input())
text = input().strip()
answer = 0
for idx, i in enumerate(text):
    var = ord(i)-ord('a')+1
    answer += var * (31**idx)
print(answer%1234567891)