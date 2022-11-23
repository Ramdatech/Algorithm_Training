def solution(s):
    return ''.join(sorted([x for x in set(s) if s.count(x) == 1]))