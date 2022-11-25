import sys
input = sys.stdin.readline
text = input().strip()
n = int(input())
pre, post = list(text), []
for _ in range(n) :
    li = input().split()
    if li[0] == "P" :
        pre.append(li[1])
    elif li[0] == "L" and pre != []:
        post.append(pre.pop(-1))
    elif li[0] == "D" and post != []:
        pre.append(post.pop(-1))
    elif li[0] == "B" and pre != []:
        pre.pop(-1)

print(''.join(pre+post[::-1]))