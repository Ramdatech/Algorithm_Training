def solution(n):
    prime = set([2,3])
    for i in range(4, int(n)+1):
        ch = True
        for j in prime :
            if i%j == 0:
                ch = False
                break
        if ch :
            prime.add(i)
    
    answer = set()
    for i in range(2,n+1):
        if n%i == 0:
            answer.add(i)
        
    
    return sorted(list(prime&answer))