import sys
input = sys.stdin.readline
ls = sorted([input().strip() for x in range(3)] , key = lambda x: (len(x), x.isdecimal()))
o = ls.pop(0)
if o == "*" :
    print("1" + "0"*(sum([len(x)-1 for x in ls])))
else:
    res = list(map(int, list(ls[1])))
    res[-1*len(ls[0])] += 1
    print(''.join(map(str,res)))