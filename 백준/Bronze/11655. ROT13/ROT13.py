def alphab(string):
    var = ord(string)
    if ord("a") <= var <= ord("z"):
        var = var - ord('a') + 13
        var = var%26 + ord('a')
    elif ord("A") <= var <= ord("Z"):
        var = var - ord('A') + 13
        var = var%26 + ord('A')
    return chr(var)

import sys
input = sys.stdin.readline
text = input()
for i in text:
    if i.isalpha() :
        print(alphab(i), end="")
    else :
        print(i, end="")