
def get_prime(n):
    ls = [False]*2 + [True]*(n-1)
    primes = []
    for i in range(2, n+1):
        if ls[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                ls[j] = False
    return primes

from itertools import permutations
def solution(numbers):
    answer = 0
    primes = get_prime(int(''.join(sorted(list(numbers), reverse=True))))
    ls = sum([list(permutations(list(numbers),i)) for i in range(1, len(numbers)+1)], [])
    nums = set([int(''.join(list(i))) for i in ls])
    for i in nums :
        if i in primes:
            answer+=1
    return answer