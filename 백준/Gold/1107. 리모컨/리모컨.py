import sys
input = sys.stdin.readline
channel = int(input().strip())
n = int(input().strip())
if n == 0 :
    ls = []
else :
    ls = list(input().split())

answer = -1
result = [abs(100-channel)]
while 1:
    answer += 1
    if set(str(channel + answer)) & set(ls) == set() :
        result.append(answer + len(str(channel+answer)))
    if channel-answer >= 0 and set(str(channel - answer)) & set(ls) == set() :
        result.append(answer + len(str(channel-answer)))
    if answer > abs(100-channel):
        break
print(min(result))