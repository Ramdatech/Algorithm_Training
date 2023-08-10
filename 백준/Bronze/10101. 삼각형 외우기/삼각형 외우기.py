ls = [int(input()) for i in range(3)]
t = "Error Equilateral Isosceles Scalene".split()
if sum(ls) != 180 :
    print(t[0])
else :
    print(t[len(set(ls))])