import sys
input = sys.stdin.readline
a = int(input())
li = sorted(list(map(int,input().strip().split())))
b = int(input())
target_list = list(map(int,input().strip().split()))


for target in target_list :
    start = 0
    end = a
    while 1 :
        calc = li[(start+end)//2]
        if end-start > 1:
            if calc > target :
                end = (start+end)//2
            elif calc <= target :
                start = (start+end)//2
        else :
            if li[start] == target :
                print(1)
                break
            else :
                print(0)
                break