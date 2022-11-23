def solution(numbers):
    numbers.sort()
    answer = [numbers[-1] * numbers[-2], numbers[0] * numbers[1]]
    return max(answer)