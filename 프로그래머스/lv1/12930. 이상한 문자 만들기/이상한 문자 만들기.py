def solution(s):
    answer = s.split(" ")
    return " ".join([''.join([x.upper() if idx%2==0 else x.lower() for idx, x in enumerate(y)]) for y in answer])