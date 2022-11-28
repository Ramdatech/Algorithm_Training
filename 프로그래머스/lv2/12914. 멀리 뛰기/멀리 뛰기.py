def solution(n):
    fib = [1,1]
    for i in range(1, n+1):
        fib.append(sum(fib[-2:]))
    return fib[n]%1234567