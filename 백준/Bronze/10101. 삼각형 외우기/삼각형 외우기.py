ls = [int(input()) for i in range(3)]
if sum(ls) != 180 :
    print("Error")
else :
    match len(set(ls)) :
        case 1 : print("Equilateral")
        case 2 : print("Isosceles")
        case 3 : print("Scalene")