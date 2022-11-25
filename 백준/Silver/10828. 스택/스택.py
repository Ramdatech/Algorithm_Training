class deque() :
    def __init__(self):
        self.list = []

    def push(self, num) :
        self.list = [num] + self.list

    def empty(self) :
        if self.list :
            print(0)
        else :
            print(1)

    def sel(self) :
        if self.list :
            print(self.list[0])
        else :
            print(-1)

    def pop(self) :
        self.sel()
        if self.list != []:
            self.list.pop(0)

    def size(self):
        print(len(self.list))

import sys
input = sys.stdin.readline
n = int(input().strip())
z = deque()
for _ in range(n) :
    li = list(map(str,input().strip().split()))
    x = li[0]
    if x == 'push' :
        z.push(int(li[1]))
    elif x == 'pop' :
        z.pop()
    elif x == 'size' :
        z.size()
    elif x == 'empty' :
        z.empty()
    else :
        z.sel()