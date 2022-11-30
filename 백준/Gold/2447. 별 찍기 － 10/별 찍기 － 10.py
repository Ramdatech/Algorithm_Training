def print_star(number):
    if number == 1 :
        return ["*"]

    list = print_star(number//3)
    array = [] 
    for i in list :
        array.append(i*3)
    for i in list :
        temptext = i + " "*len(list) + i
        array.append(temptext)
    for i in list :
        array.append(i*3)
    return array

import sys
input = int(sys.stdin.readline())
li = print_star(input)
print("\n".join(li))