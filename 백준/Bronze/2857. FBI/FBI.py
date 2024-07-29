tmp = [i+1 for i in range(5) if "FBI" in input()]
if tmp == [] :
    print("HE GOT AWAY!")
else : 
    print(*tmp, sep=" ")