def solution(num_list):
    answer = [x for x in num_list if x%2 == 0]
    return [len(answer), len(num_list)-len(answer)]