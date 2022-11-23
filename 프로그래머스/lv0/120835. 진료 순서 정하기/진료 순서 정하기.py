def solution(emergency):
    return [sorted(emergency)[::-1].index(x)+1 for x in emergency]