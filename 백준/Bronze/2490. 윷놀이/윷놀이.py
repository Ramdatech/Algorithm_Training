for i in range(3):
    match sum(map(int, input().split())) :
        case 0 : print("D")
        case 1 : print("C")
        case 2 : print("B")
        case 3 : print("A")
        case 4 : print("E")