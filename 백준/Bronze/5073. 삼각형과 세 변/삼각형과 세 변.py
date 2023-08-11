a = "Invalid Equilateral Isosceles Scalene".split()
while (t:=list(map(int,input().split()))) != [0, 0, 0] :
    t = sorted(t)
    if sum(t[:2]) <= t[2] :
        print("Invalid")
    else :
        print(a[len(set(t))])