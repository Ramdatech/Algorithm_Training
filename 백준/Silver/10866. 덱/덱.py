class deque() :
    def __init__(self):
        self.list = []

    def push(self, string, num) :
        if string == "push_front" :
            self.list = [num] + self.list
        else :
            self.list = self.list + [num]

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

    def pop(self, string) :
        self.sel(string)
        if self.list != [] and string == 'front':
            self.list.pop(0)
        elif self.list != [] and string == 'back':
            self.list.pop(-1)

    def size(self):
        print(len(self.list))

import sys
input = sys.stdin.readline
n = int(input().strip())
z = deque()
for _ in range(n) :
    li = list(map(str,input().strip().split()))
    x = li[0]
    if x[:4] == 'push' :
        z.push(x, int(li[1]))
    elif x == 'front' or x == 'back' :
        z.sel(x)
    elif x[:3] == 'pop' :
        z.pop(x[4:])
    elif x == 'size' :
        z.size()
    elif x == 'empty' :
        z.empty()