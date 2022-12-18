from collections import deque

def solution(bridge_length, weight, truck_weights):        
    answer = 0
    ls = deque([0 for x in range(bridge_length)])
    truck_weights = deque(truck_weights)
    totalweight = 0
    while len(truck_weights) > 0:
        if len(ls) > bridge_length-1 :
            w = ls.popleft()
            totalweight -= w
        if totalweight+truck_weights[0] <= weight :
            truck = truck_weights.popleft()
            totalweight += truck
            ls.append(truck)
            answer+=1
        else :
            ls.append(0)
            answer+=1

    while totalweight > 0 :
        totalweight -= ls.popleft()
        answer += 1    
    return answer