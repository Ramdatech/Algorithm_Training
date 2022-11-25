def solution(n):
    a = bin(n)[2:].count("1")
    for i in range(n+1, 2*n):
        if a == bin(i)[2:].count("1"):
            return i