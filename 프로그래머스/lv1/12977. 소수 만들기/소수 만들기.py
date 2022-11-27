def solution(nums):
    n = 3000
    numbers = set([x for x in range(2, n+1)])
    for i in range(2, int(n**0.5)+1):
        numbers -= set([i*x for x in range(2, (n//i)+1)])
    
    answer = 0
    for x in range(len(nums)) :
        for y in range(x+1, len(nums)) :
            for z in range(y+1 ,len(nums)) :
                if nums[x]+nums[y]+nums[z] in numbers :
                    answer += 1
        
    return answer