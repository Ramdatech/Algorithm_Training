def solution(num_list, n):
    answer = [num_list[x*n:(x+1)*n] for x in range(len(num_list)//n)]
    return answer