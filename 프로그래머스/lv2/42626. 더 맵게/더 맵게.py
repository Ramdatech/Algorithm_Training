import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    heap = scoville
    while len(heap) > 1 :
        temp = heapq.heappop(heap)
        if temp >= K :
            break
        elif temp < K :
            temp2 = heapq.heappop(heap)
            scoville = heapq.heappush(heap, temp + temp2*2)
            answer += 1
    if heap[0] < K :
        return -1
    else :
        return answer