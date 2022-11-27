import sys
t = sys.stdin.readline()
t = int(t)
li = [0, 1]

p = 2
if t < 2 : 
	print(li[t])
else :
    while 1:
    	li=[li[1], li[0]+li[1]]
    	if p == t :
    		break
    	p += 1 
    
    print(li[-1])