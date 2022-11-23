def solution(my_str, n):
    return [my_str[x*n:(x+1)*n] for x in range(len(my_str)) if my_str[x*n:(x+1)*n] != ""] 