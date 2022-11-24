def solution(participant, completion):
    participant, completion = sorted(participant), sorted(completion)+[""]
    for i,j in zip(participant, completion):
        if i != j :
            return i