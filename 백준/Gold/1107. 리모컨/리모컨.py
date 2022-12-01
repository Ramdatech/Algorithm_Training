import sys
input = sys.stdin.readline
channel = int(input().strip())
n = int(input().strip())
if n == 0 :
    ls = []
else :
    ls = list(input().split())

push = -1
result = [abs(100-channel)]
while 1:
    push += 1
    if set(str(channel + push)) & set(ls) == set() and push + len(str(channel+push)) < result[-1]:
        result.append(push + len(str(channel+push)))
    if channel-push >= 0 and set(str(channel - push)) & set(ls) == set() and push + len(str(channel-push)) < result[-1]:
        result.append(push + len(str(channel-push)))
    if push > abs(100-channel):
        break
print(min(result))