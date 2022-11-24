def solution(numbers):
    return sorted(list(set(sum([[numbers[x]+numbers[y] for y in range(x+1, len(numbers))] for x in range(0, len(numbers))],[]))))