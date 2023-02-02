import sys
x = {'-': 0,'\\': 1,'(': 2,'@': 3,'?': 4,'>': 5,'&': 6,'%': 7,'/': -1}
for input in sys.stdin :
    t = input.strip()
    if t == "#":
        break
    print(sum([x[s]*(8**idx) for idx, s in enumerate(list(t)[::-1])]))