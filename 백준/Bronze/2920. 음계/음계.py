import sys
li = list(map(int, sys.stdin.readline().split()))
if li == sorted(li) :
    print('ascending')
elif li == sorted(li)[::-1] :
    print('descending')
else :
    print("mixed")