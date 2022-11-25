class deque() :
    def __init__(self):
        self.list = []

    def push(self, num) :
        self.list =  self.list + [num]

    def empty(self) :
        if self.list :
            print(0)
        else :
            print(1)

    def sel(self, string) :
        if self.list and string == 'front':
            print(self.list[0])
        elif self.list and string == 'back':
            print(self.list[-1])
        else :
            print(-1)

    def pop(self) :
        self.sel('front')
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
        z.sel(x)