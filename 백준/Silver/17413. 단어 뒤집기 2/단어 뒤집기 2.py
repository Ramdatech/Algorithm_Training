import sys
a = sys.stdin.readline().strip()
a = ">" + a + "<"
pre, post = 0, 0
while 1 :
    pre = a.find(">", pre)+1
    post = a.find("<", post+1)
    if pre == -1 or post == -1 :
        break
    text = a[pre:post][::-1]
    text = text.split(" ")[::-1]
    a = a[:pre] + ' '.join(text) + a[post:]

print(a[1:-1])